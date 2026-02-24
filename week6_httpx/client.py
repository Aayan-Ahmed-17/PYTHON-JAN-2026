import httpx

def get_data():
    response = httpx.get("https://httpbin.org/get")
    print(f"Status Code: {response.status_code}")
    print(f"Headers: {response.headers}")
    print(f"Content: {response.text}")
    return response
    
if __name__ == "__main__":
    print(get_data())
