import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
     os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
     
     api_service_name = "youtube"
     api_version = "v3"
     client_secret_file = "client_secret_668444080395-ddaf2ktt51r766eak5vcdchqb7uk7she.apps.googleusercontent.com.json"
     
     flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secret_file, scopes)
     
     credentials = flow.run_console()
     youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)
     
     request = youtube.channels.list(
         part="snippet,contentDetails,statistics",
         id="UC_x5XG1OV2P6uZZ5FSM9Ttw"
         )
     
     response = request.execute()
     print(response)

main()