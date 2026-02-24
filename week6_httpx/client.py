import httpx


# basic get request
def get_data():
    response = httpx.get("https://httpbin.org/get")
    print(f"Status Code: {response.status_code}")
    print(f"Headers: {response.headers}")
    print(f"Content: {response.text}")
    return response


# post request
def create_task():
    url = "https://httpbin.org/post"
    payload = {"title": "Learning httpx", "completed": False}

    response = httpx.post(url, json=payload)

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

    return response


# put request
def update_task():
    url = "https://httpbin.org/put"
    payload = {"title": "Learning httpx", "completed": True}

    response = httpx.put(url, json=payload)
    print(f"Status code {response.status_code}")
    print(f"Respnse {response.json()}")
    return response


if __name__ == "__main__":
    # print(get_data())
    # print(create_task())
    print(update_task())
