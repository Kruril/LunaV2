import json
from datetime import datetime, timedelta

import requests
import os.path
import boto3
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file credentials.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

CREDENTIALS_FILE = 'credentials.json'

s3 = boto3.client("s3")
s3_bucket = os.environ["BUCKET"]


def create_event(event, context):
    month = datetime.now().month
    year = datetime.now().year
    service = get_calendar_service()

    phases = requests.get(f"https://www.icalendar37.net/lunar/api/?lang=fr&month={month}&year={year}").json()["phase"]

    for day_number in phases:
        phase = phases[day_number]["npWidget"]
        day = datetime(year, month, int(day_number))
        start = (day + timedelta(hours=18)).isoformat()
        end = (day + timedelta(hours=18, minutes=30)).isoformat()

        service.events().insert(calendarId='primary',
                                body={
                                    "summary": phase,
                                    "start": {"dateTime": start, "timeZone": 'Europe/Brussels'},
                                    "end": {"dateTime": end, "timeZone": 'Europe/Brussels'},
                                }
                                ).execute()


def get_calendar_service():
    creds = None
    obj = s3.get_object(Bucket=s3_bucket, Key=CREDENTIALS_FILE)
    creds = Credentials.from_authorized_user_info(json.load(obj['Body']), SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(
                json.load(obj['Body']), SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        s3.put_object(Bucket=s3_bucket, Key=CREDENTIALS_FILE, Body=creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    return service


if __name__ == '__main__':
    create_event("salut", "coucou")
    # Create credentials file
    # service = get_calendar_service()
