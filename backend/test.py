import requests
import json

def hit_backend_api(url, data):
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        result = response.json()
        print("✅ Response received successfully.")
        return result
    except requests.exceptions.RequestException as e:
        print("❌ Error during request:", e)
        return {"error": str(e)}

def main():
    url = "http://localhost:8000/generate"
    payload = {
        "description": "Sample description",
        "region": "US",
        "language": "English",
        "targetAudience": "General"
    }

    result = hit_backend_api(url, payload)

    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
        print("📝 Response saved to result.json")

if __name__ == "__main__":
    main()
