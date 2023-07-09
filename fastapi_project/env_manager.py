import os

def load_env_cred() -> int:
    """Reads .env file from current folder to load env variables"""
    with open(".env", encoding="utf-8") as file:
        for line in file.readlines():
            key, value = line.split("=", maxsplit=1)
            os.environ[key] = value.strip()
if __name__ == "__main__":
    load_env_cred()
