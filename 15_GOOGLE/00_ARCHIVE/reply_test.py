import base64
from email.message import EmailMessage
from auth_helper import get_service

def reply_to_test():
    try:
        service = get_service('gmail', 'v1')
        
        # Details of the test mail we found
        to_email = "braxmeier@protonmail.com"
        subject = "Re: [EXTERN] test"
        content = "Hallo, der Test hat geklappt."
        thread_id = "19bd1d51cb93ba91" # From the previous search

        message = EmailMessage()
        message.set_content(content)
        message['To'] = to_email
        message['Subject'] = subject
        message['In-Reply-To'] = thread_id
        message['References'] = thread_id

        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        create_message = {'raw': encoded_message, 'threadId': thread_id}

        send_message = service.users().messages().send(userId="me", body=create_message).execute()
        print(f'Antwort gesendet! Message Id: {send_message["id"]}')
        return send_message

    except Exception as e:
        print(f'Fehler beim Antworten: {e}')
        return None

if __name__ == "__main__":
    reply_to_test()
