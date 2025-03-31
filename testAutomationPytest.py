import requests

def test():
    url = "http://127.0.0.1:8000/add/2/2"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses (4xx, 5xx)
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

test()
