from jwt import encode, decode
import env_manager as em
import os

em.load_env_cred()
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

def create_token(data: dict) -> str:
    """Creates JWT token for user. Data is dict {"username":"passwd"}"""
    jwt_token = encode(payload=data, key=JWT_SECRET_KEY, algorithm="HS256")
    return jwt_token

def validate_token(token: str) -> dict:
    data = decode(jwt=token, key=JWT_SECRET_KEY, algorithms=["HS256"])
    return data

if __name__ == "__main__":
      __test_data = {"test":1}
      __test_token = create_token(__test_data)
      __result_data = validate_token(__test_token)
      assert __test_data == __result_data