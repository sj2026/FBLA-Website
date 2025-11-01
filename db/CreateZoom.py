import jwt
import requests
import json
from time import time
from datetime import datetime, timedelta, timezone

CLIENT_ID = 'G9bzrFw6SQuZXx5C70QjsQ'       # <--- REPLACE THIS
CLIENT_SECRET = 'EkulW67X2WCG90dLUKNdrvEnMHB1nU8Z'   # <--- REPLACE THIS
ACCOUNT_ID = 'oZrFptqKRwOFDYq5iPRX4w'     # <--- REPLACE THIS

# --- Function to obtain an Access Token using Server-to-Server OAuth ---
def get_server_to_server_oauth_token():
        """
        Obtains an access token using the Server-to-Server OAuth flow.
        This token is valid for 1 hour.
        """
        token_url = "https://zoom.us/oauth/token"
        params = {
            "grant_type": "account_credentials",
            "account_id": ACCOUNT_ID
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        try:
            # The Client ID and Client Secret are sent as Basic Authentication
            response = requests.post(token_url, params=params, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
            response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
            token_info = response.json()
            return token_info.get("access_token")
        except requests.exceptions.RequestException as e:
            print(f"Error obtaining Server-to-Server OAuth token: {e}")
            if response.status_code:
                print(f"Status Code: {response.status_code}")
                print(f"Response Body: {response.text}")
            return None


class CreateZoom:
    # --- Function to create a Zoom meeting ---
    def create_zoom_meeting(self, title, start_time_str):
        """
        Creates a new Zoom meeting using the Zoom API with a Server-to-Server OAuth token.

        Args:
            topic (str): The meeting topic/title.
            start_time_str (str): The meeting start time in ISO 8601 format (e.g., "2025-07-01T10:00:00").
                                The timezone for this string should match the `timezone_str` parameter.
            duration_minutes (int): The meeting duration in minutes.
            timezone_str (str): The timezone of the meeting (e.g., "America/New_York", "UTC", "Europe/London").
                                Defaults to "America/New_York".
            agenda (str): The meeting agenda (optional).

        Returns:
            dict: A dictionary containing the meeting details (join_url, password, etc.)
                or an error message if the API call fails.
        """
        access_token = get_server_to_server_oauth_token()
        if not access_token:
            return {"error": "Failed to obtain access token."}

        # Zoom API endpoint for creating meetings for the current user ('me')
        # 'me' refers to the user associated with the API key/account ID.
        api_url = f"https://api.zoom.us/v2/users/me/meetings"

        # Set the request headers, including the Authorization token
        headers = {
            'authorization': f'Bearer {access_token}',
            'content-type': 'application/json'
        }

        # Define the meeting details payload
        meeting_details = {
            "topic": title + " Interview",
            "type": 2,  # 2 for a scheduled meeting
            "start_time": start_time_str,
            "duration": 45,
            "timezone": "America/Chicago",
            "agenda": "Interview",
            "settings": {
                "host_video": True,
                "participant_video": True,
                "join_before_host": False,
                "mute_upon_entry": True,
                "watermark": False,
                "audio": "voip",
                "auto_recording": "none"  # "none", "local", or "cloud"
            }
        }

        try:
            # Send the POST request to the Zoom API
            response = requests.post(api_url, headers=headers, data=json.dumps(meeting_details))
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

            meeting_info = response.json()
            return meeting_info
        except requests.exceptions.RequestException as e:
            print(f"Error creating Zoom meeting: {e}")
            if response.status_code:
                print(f"Status Code: {response.status_code}")
                print(f"Response Body: {response.text}")
            return {"error": f"Failed to create meeting: {e}", "status_code": response.status_code, "response_body": response.text}


    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #print("Attempting to create a zoom meeting:")
    #current_time = datetime.now(tz=timezone.utc)
    #meeting_start_time = (current_time + timedelta(minutes=30)).strftime("%Y-%m-%dT%H:%M:%SZ")

    #zoomLink = create_zoom_meeting("CEO", meeting_start_time)
    #print(zoomLink['start_url'])