from requests import get

def fetch_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = get(url)
    data = response.json()

    if data["success"] and len(data["data"]):
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch userdata")

def main():
    try:
        username, country = fetch_user()
        print(f"The username is {username} and the country is {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()