import base64
import datetime
from email.message import EmailMessage
from googleapiclient.errors import HttpError
from google_auth import get_service

def list_messages(query='is:unread', max_results=10):
    """Lists messages matching the query."""
    try:
        service = get_service('gmail', 'v1')
        results = service.users().messages().list(userId='me', q=query, maxResults=max_results).execute()
        messages = results.get('messages', [])
        
        if not messages:
            print('No messages found.')
            return []

        final_list = []
        for msg in messages:
            full_msg = service.users().messages().get(userId='me', id=msg['id'], format='metadata').execute()
            headers = full_msg['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
            sender = next((h['value'] for h in headers if h['name'] == 'From'), '(Unknown)')
            date = next((h['value'] for h in headers if h['name'] == 'Date'), '')
            
            final_list.append({
                'id': msg['id'],
                'sender': sender,
                'subject': subject,
                'date': date,
                'snippet': full_msg.get('snippet', '')
            })
            
        return final_list

    except HttpError as error:
        print(f'An error occurred: {error}')
        return []

def get_todays_emails():
    # Construct query for "newer_than:1d" effectively
    # Or strict date matching: after:YYYY/MM/DD
    today = datetime.date.today().strftime("%Y/%m/%d")
    query = f"after:{today}"
    print(f"Searching for emails with query: {query}")
    return list_messages(query=query, max_results=20)

def get_message_body(msg_id):
    """Gets the body of a specific message."""
    try:
        service = get_service('gmail', 'v1')
        message = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
        
        payload = message.get('payload')
        parts = payload.get('parts')
        data = None
        
        if parts:
            for part in parts:
                if part['mimeType'] == 'text/plain':
                    data = part['body']['data']
                elif part['mimeType'] == 'text/html':
                    # Prefer HTML if plain not found yet, or keep looking? 
                    # Usually we want plain for CLI.
                    if not data: 
                        data = part['body']['data']
        else:
            data = payload['body']['data']
            
        if data:
            text = base64.urlsafe_b64decode(data).decode('utf-8')
            return text
        return "(No text content found)"

    except HttpError as error:
        print(f'An error occurred: {error}')
        return None

def send_message(to_email, subject, content):
    """Sends an email."""
    try:
        service = get_service('gmail', 'v1')
        message = EmailMessage()
        message.set_content(content)
        message['To'] = to_email
        message['From'] = 'me' # Gmail API ignores this and uses the authenticated user
        message['Subject'] = subject

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {
            'raw': encoded_message
        }

        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        print(f'Message Id: {send_message["id"]}')
        return send_message

    except HttpError as error:
        print(f'An error occurred: {error}')
        return None

def create_label(label_name):
    """Creates a new label."""
    try:
        service = get_service('gmail', 'v1')
        label_body = {
            'name': label_name,
            'labelListVisibility': 'labelShow',
            'messageListVisibility': 'show'
        }
        label = service.users().labels().create(userId='me', body=label_body).execute()
        print(f"Label '{label_name}' created with ID: {label['id']}")
        return label['id']
    except HttpError as error:
        if error.resp.status == 409: # 409 Conflict means label already exists
            print(f"Label '{label_name}' already exists. Attempting to retrieve its ID.")
            labels = service.users().labels().list(userId='me').execute().get('labels', [])
            for existing_label in labels:
                if existing_label['name'] == label_name:
                    print(f"Found existing label '{label_name}' with ID: {existing_label['id']}")
                    return existing_label['id']
            print(f"Error: Label '{label_name}' exists but could not retrieve its ID.")
            return None
        print(f'An error occurred creating label: {error}')
        return None

def list_messages_by_query(query=''):
    """Lists message IDs matching the query."""
    try:
        service = get_service('gmail', 'v1')
        results = service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])
        return [msg['id'] for msg in messages]
    except HttpError as error:
        print(f'An error occurred listing messages by query: {error}')
        return []

def apply_label_to_messages(message_ids, label_id):
    """Applies a label to a list of messages."""
    if not message_ids:
        print("No messages to apply label to.")
        return
    try:
        service = get_service('gmail', 'v1')
        batch_modify_request = {
            'ids': message_ids,
            'addLabelIds': [label_id]
        }
        service.users().messages().batchModify(userId='me', body=batch_modify_request).execute()
        print(f"Applied label '{label_id}' to {len(message_ids)} messages.")
    except HttpError as error:
        print(f'An error occurred applying label: {error}')

def remove_label_from_messages(message_ids, label_id):
    """Removes a label from a list of messages."""
    if not message_ids:
        print("No messages to remove label from.")
        return
    try:
        service = get_service('gmail', 'v1')
        batch_modify_request = {
            'ids': message_ids,
            'removeLabelIds': [label_id]
        }
        service.users().messages().batchModify(userId='me', body=batch_modify_request).execute()
        print(f"Removed label '{label_id}' from {len(message_ids)} messages.")
    except HttpError as error:
        print(f'An error occurred removing label: {error}')

def delete_messages(message_ids):
    """Deletes a list of messages (moves to Trash)."""
    if not message_ids:
        print("No messages to delete.")
        return
    try:
        service = get_service('gmail', 'v1')
        batch_delete_request = {
            'ids': message_ids
        }
        service.users().messages().batchDelete(userId='me', body=batch_delete_request).execute()
        print(f"Moved {len(message_ids)} messages to Trash.")
    except HttpError as error:
        print(f'An error occurred deleting messages: {error}')

if __name__ == '__main__':
    # Simple CLI Test
    print("1. List Unread Messages")
    print("2. Send a Test Email")
    choice = input("Choose (1/2): ")
    
    if choice == '1':
        msgs = list_messages()
        for i, m in enumerate(msgs):
            print(f"[{i}] {m['sender']}: {m['subject']} - {m['snippet'][:50]}...")
            
        if msgs:
            idx = input("Read email # (or enter to skip): ")
            if idx.isdigit() and int(idx) < len(msgs):
                body = get_message_body(msgs[int(idx)]['id'])
                print("\n--- CONTENT ---\n")
                print(body)
                print("\n---------------")
                
    elif choice == '2':
        to = input("To: ")
        subj = input("Subject: ")
        body = input("Body: ")
        send_message(to, subj, body)
