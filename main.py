import requests
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# Global vars
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": None
}

def send_email_reply(ticket_id, user, body, authentication):
    """Function to automatically send email reply and internal note to ticket using Gorgias REST API
        Parameters:
        Ticket ID(int),
        Agent User(int),
        Email Text(string),
        Authentication(string)
        """
    url = f'https://dgexercise.gorgias.com/api/tickets/{ticket_id}'
    # formatted string to include expression {ticket_id}

    headers.update({'authorization': authentication})  # define authentication credentials
    payload = {
        "assignee_team": None,
        "assignee_user": None,
        "customer": {
            "id": None,
            "email": "kate_sorotos@live.co.uk"
        },
        "tags": [{"name": "urgent"}],
        "channel": "email",
        "closed_datetime": None,
        "external_id": "RETURN#4213",
        "from_agent": True,
        "is_unread": True,
        "language": "fr",
        "last_message_datetime": "2020-02-01T19:12:32.432197",
        "last_received_message_datetime": "2020-01-27T10:42:21.468912",
        "opened_datetime": "2019-07-05T15:22:46.472436",
        "snooze_datetime": None,
        "spam": False,
        "status": "open",
        "subject": "Can you help me with my order query?",
        "trashed_datetime": None,
        "updated_datetime": "2020-01-27T10:42:21.932637",
        "via": "email"
    }  # information sent when making api request
    payload.update({'messages': body})
    payload["customer"]["id"] = user

    response = requests.put(url, json=payload, headers=headers)

    print(response.text)

def leave_internal_note(ticket_id, user, body, authentication):
    """Function to automatically send email reply and internal note to ticket using Gorgias REST API
            Parameters:
            Ticket ID(int),
            Agent User(int),
            Email Text(string),
            Authentication (string),
            """

    payload = {
        "sender": {"id": None},
        "source": {"type": "internal-note"},
        "body_text": "This is an internal note test",
        "channel": "internal-note",
        "via": "api"
    }
    payload["sender"]["id"] = user
    payload.update({'body_text': body})
    url = f'https://dgexercise.gorgias.com/api/tickets/{ticket_id}/messages'

    headers.update({'authorization': authentication})

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)


leave_internal_note(13228870, 36331423, "This is an internal note test", os.environ.get("AUTHORISATION"))
send_email_reply(13228870, 36331423, "test", os.environ.get("AUTHORISATION"))
