import vk
from getpass import getpass


def get_user_login():
    login = input("Login: ")
    return login


def get_user_password():
    password = getpass()
    return password


def get_online_friends_info(login, password, app_id):
    session = vk.AuthSession(
        app_id=app_id,
        user_login=login,
        user_password=password,
        scope="friends"
    )
    api = vk.API(session)
    online_friends_ids = api.friends.getOnline()
    online_friends = api.users.get(user_ids=online_friends_ids)
    return online_friends


def print_online_friends(friens_info):
    for user in friens_info:
        if user["online"]:
            print(user["first_name"], user["last_name"])


if __name__ == "__main__":
    login = get_user_login()
    password = get_user_password()
    vk_app_id = 5750748
    print("Getting friends info...")
    friends_info = get_user_friends_info(login, password, vk_app_id)
    print("Searching friends online...")
    print_online_friends(friends_info)
