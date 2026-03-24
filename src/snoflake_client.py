import snowflake.connector

class SnowflakeClient:
    def __init__(self, config):
        self.conn = snowflake.connector.connect(
            user=config["user"],
            password=config["password"],
            account=config["account"],
            warehouse=config["warehouse"],
            database=config["database"],
            schema=config["schema"]
        )

    def execute_query(self, query):
        cur = self.conn.cursor()
        try:
            cur.execute(query)
            return cur.fetchone()[0]
        finally:
            cur.close()