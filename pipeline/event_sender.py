import requests


def send_event(event):

    try:

        response = requests.post(
            "http://127.0.0.1:8000/events/ingest",
            json=[event],
            timeout=5
        )

        print(
            "API:",
            response.status_code
        )

        if response.status_code != 200:
            print(response.text)

        return response.status_code

    except Exception as e:

        print(
            "API ERROR:",
            e
        )

        return None
