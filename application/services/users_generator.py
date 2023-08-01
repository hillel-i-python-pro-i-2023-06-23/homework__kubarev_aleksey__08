from faker import Faker
from typing import NamedTuple


class User(NamedTuple):
    name: str
    email: str


faker = Faker()


def user_generator() -> User:
    return User(
        name=faker.first_name(),
        email=faker.email(),
    )


def users_generator_list(amount: int = 100) -> User:
    for _ in range(1, amount + 1):
        yield user_generator()


def users_generator_string(users, type_of_list="ol"):
    formatted_list = []
    for user in users:
        formatted_user = f"<li> Name: <b>{user.name}</b> - <span>email:{user.email}</span></li>"
        formatted_list.append(formatted_user)
    _temp_line = "\n".join(formatted_list)
    return f"<{type_of_list}>{_temp_line}</{type_of_list}>"
