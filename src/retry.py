import time

def retry(func, retries=3, delay=2):
    def wrapper(*args, **kwargs):
        for attempt in range(retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == retries - 1:
                    raise
                time.sleep(delay * (attempt + 1))
    return wrapper