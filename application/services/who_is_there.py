import requests


def get_info_from_api(url):
    return requests.get(url).json()


def get_list_astronauts(data):
    return [f"{a['craft']} - {a['name']}" for a in data["people"]]


def get_count_astronauts(data):
    return data["number"]


def get_space_info_string(data):
    count_astro = get_count_astronauts(data)
    list_astro = get_list_astronauts(data)
    list_items = "\n".join(f"<li>{astro}</li>" for astro in list_astro)
    return f"Now we have {count_astro} astronauts in space\n<ol>\n{list_items}\n</ol>"
