import json
from src.snowflake_client import SnowflakeClient
from src.elastic_client import ElasticClient
from src.validator import Validator
from src.alert import send_slack_alert
from src.retry import retry

# Load configs
with open("config/config.json") as f:
    config = json.load(f)

with open("config/rules.json") as f:
    rules = json.load(f)

sf = SnowflakeClient(config["snowflake"])
es = ElasticClient(config["elasticsearch"]["host"])

@retry
def get_sf_count(query):
    return sf.execute_query(query)

@retry
def get_es_count(index):
    return es.get_count(index)

def run():
    failures = []

    for table in rules["tables"]:
        name = table["name"]

        sf_count = get_sf_count(table["snowflake_query"])
        es_count = get_es_count(table["es_index"])

        result = Validator.count_match(sf_count, es_count)

        print(f"{name}: {result}")

        if not result["status"]:
            failures.append({
                "table": name,
                "sf_count": sf_count,
                "es_count": es_count
            })

    if failures:
        msg = f"Data Mismatch Detected:\n{failures}"
        send_slack_alert(config["slack_webhook"], msg)

if __name__ == "__main__":
    run()