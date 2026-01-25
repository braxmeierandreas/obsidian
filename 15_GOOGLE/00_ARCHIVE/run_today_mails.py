from gmail_client import get_todays_emails

def show_todays_emails():
    print("--- Mails von heute ---")
    emails = get_todays_emails()
    
    if not emails:
        print("Keine Mails von heute gefunden.")
        return

    for i, email in enumerate(emails, 1):
        print(f"\n[{i}] Von: {email['sender']}")
        print(f"    Betreff: {email['subject']}")
        print(f"    Zeit: {email['date']}")
        print(f"    Vorschau: {email['snippet'][:100]}...")

if __name__ == "__main__":
    show_todays_emails()
