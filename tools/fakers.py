import time

def get_random_email() -> str:
    return f"test.{time.time()}@example.com"

def get_random_last_name() -> str:
    return f"test.{time.time()}-ов"

def get_random_first_name() -> str:
    return f"test.{time.time()}-а"

def get_random_middle_name() -> str:
    return f"test.{time.time()}-ович"