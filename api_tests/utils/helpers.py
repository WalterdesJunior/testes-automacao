import random
import string


def random_suffix():
    return "".join(random.choices(string.ascii_lowercase, k=6))


def pet_payload(status="available"):
    return {
        "id": random.randint(100000, 999999),
        "name": f"pet_{random_suffix()}",
        "status": status,
        "photoUrls": ["https://example.com/photo.jpg"],
        "category": {"id": 1, "name": "Dogs"},
        "tags": [{"id": 1, "name": "friendly"}],
    }


def user_payload():
    suffix = random_suffix()
    return {
        "id": random.randint(100000, 999999),
        "username": f"user_{suffix}",
        "firstName": "Test",
        "lastName": "User",
        "email": f"user_{suffix}@test.com",
        "password": "senha123",
        "phone": "11999999999",
        "userStatus": 1,
    }
