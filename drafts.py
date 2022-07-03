from __future__ import print_function

import base64,os 
from email.message import EmailMessage
from google.oauth2.credentials import Credentials

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://mail.google.com/']

creds = ''
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)


def gmail_create_draft(rece, send, subject, body):
    """Create and insert a draft email.
       Print the returned draft's message and id.
       Returns: Draft object, including draft id and message meta data.

      Load pre-authorized user credentials from the environment.
      TODO(developer) - See https://developers.google.com/identity
      for guides on implementing OAuth2 for the application.
    """
    # creds, _ = google.auth.default()

    try:
        # create gmail api client
        service = build('gmail', 'v1', credentials=creds)

        message = EmailMessage()

        message.set_content(body)

        message['To'] = rece
        message['From'] = send
        message['Subject'] = subject

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {
                'raw': encoded_message
        }
        # pylint: disable=E1101
        draft = service.users().drafts().create(userId="me",
                                                body= {'message' : {'raw' : encoded_message}}).execute()

        print(F'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        print(F'Message Id: {send_message["id"]}')

        


        

    except HttpError as error:
        print(F'An error occurred: {error}')
        draft = None
        send_message = None

    return draft, send_message



if __name__ == '__main__':
    gmail_create_draft("dhanush17raj@gmail.com", "dhanush10raj@gmail.com", "draft mail", "This ia draft mail from dhanush raj")

