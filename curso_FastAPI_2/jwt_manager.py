from jwt import decode, encode
from secret_key import secret_key


def create_token(data: dict) -> str:
    token: str = encode(payload=data, key=secret_key, algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    data: dict = decode(token, key=secret_key, algorithms=['HS256'])
    return data
