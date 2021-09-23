from datetime import datetime, timedelta

import requests
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

CREDENTIALS_FILE = 'credentials.json'


def create_event(event, context):
    month = datetime.now().month
    year = datetime.now().year
    service = get_calendar_service()

    phases = requests.get(f"https://www.icalendar37.net/lunar/api/?lang=fr&month={month}&year={year}").json()["phase"]
    print(phases)
    for day_number in phases:
        phase = phases[day_number]["npWidget"]
        day = datetime(year, month, day_number)
        start = (day + timedelta(hours=19)).isoformat()
        end = (day + timedelta(hours=19, minutes=30)).isoformat()

        service.events().insert(calendarId='primary',
                                body={
                                    "summary": phase,
                                    "start": {"dateTime": start, "timeZone": 'Europe/Brussels'},
                                    "end": {"dateTime": end, "timeZone": 'Europe/Brussels'},
                                }
                                ).execute()


def get_calendar_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service
