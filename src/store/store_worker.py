import json
from typing import Any, NamedTuple

class User(NamedTuple):
    id: int
    username: str
    name: str
    photo_url: str
    wishlist: str
    hatelist: str

class Store(NamedTuple):
    users: dict[str, Any]
    on_secret_santa: dict[str, Any]

def open_store(filename: str = "src\\store\\store.json") -> Store:
    f = open(filename)
    data = json.load(f)
    return Store(users=data["users"], on_secret_santa=data["on_secret_santa"])

def write_store(new_data: Store, filename: str = "src\\store\\store.json") -> bool:
    print(new_data._asdict())
    try:
        with open(filename, "w") as outfile:
            outfile.write(
                json.dumps(new_data._asdict())
                )
        return True
    except:
        return False

def add_new_user_to_store(user: User) -> bool:
    store = open_store()
    store.users[str(user.id)] = user._asdict()
    return write_store(store)

def edit_user_props_in_store(user: User) -> bool:
    return add_new_user_to_store(user)

def get_user_by_id_from_store(user_id: int) -> User:
    store = open_store()
    user = store.users[str(user_id)]
    return User(
        id=user["id"],
        name=user["name"],
        photo_url=user["photo_url"],
        wishlist=user["wishlist"],
        hatelist=user["hatelist"],
        username=user["username"]
    )

if __name__ == "__main__":
    user = User(
        id=123,
        username="@mario",
        name="Mario",
        photo_url="asdasldkasld",
        wishlist="sadasdsad",
        hatelist="asdasdlkasdl"
    )
    print(add_new_user_to_store(user))