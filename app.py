from flask import Flask

from application.services.reading_a_file import get_file_string
from application.services.users_generator import users_generator_list, users_generator_string
from application.services.who_is_there import get_info_from_api, get_space_info_string
from application.services.average import read_google_sheets_pd_data, print_info, get_string_info

app = Flask(__name__)


@app.route("/")
def welcome():
    return f"<h3> Homework #8 (Kubarev Aleksey) </h2>"


@app.route("/get-content")
@app.route("/get-content/")
def get_content(namefile: str = "text.txt"):
    return get_file_string(namefile)


@app.route("/generate-users")
@app.route("/generate-users/")
def generator_users(amount_of_users: int = 100):
    users = users_generator_list(amount=amount_of_users)
    return users_generator_string(users=users, type_of_list="ol")


@app.route("/space")
@app.route("/space/")
def space():
    url = "http://api.open-notify.org/astros.json"
    data = get_info_from_api(url)
    return get_space_info_string(data)


@app.route("/mean")
@app.route("/mean/")
def mean():
    url2 = "https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt"
    df = read_google_sheets_pd_data(url2)
    print_info(df)
    string_info = get_string_info(df)
    return string_info


if __name__ == "__main__":
    app.run()
