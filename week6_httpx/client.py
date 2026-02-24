import httpx

def get_data():
    response = httpx.get("https://httpbin.org/get")
    return response.json()

if __name__ == "__main__":
    data = get_data()
    print(data)