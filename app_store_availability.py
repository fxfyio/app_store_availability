import requests
import json

def fetch_app_store_availability(app_id):
    url = f"https://itunes.apple.com/lookup?id={app_id}"
    response = requests.get(url)
    data = json.loads(response.text)
    formatted_json = json.dumps(data, indent=4)
    print(f"json: {formatted_json}")

    if 'results' in data and len(data['results']) > 0:
        app_info = data['results'][0]
        print(f"App Name: {app_info.get('trackName', 'Unknown')}")

    else:
        print(f"No information found for App ID: {app_id}")

if __name__ == "__main__":
    app_id = "284882215"  # Facebook的App ID
    fetch_app_store_availability(app_id)
