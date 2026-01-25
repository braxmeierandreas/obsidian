from gmail_client import send_message

def send_hannah_mail():
    to = "hanne.bornschein@gmx.de"
    subject = "Gute Heimfahrt ❤️"
    content = """Hey mein Schatz,

ich wollte dir nur schnell schreiben, dass ich mich riesig über unser gemeinsames Wochenende gefreut habe. Es war wirklich wunderschön mit dir.

Komm bitte gut in Freiburg an und schreib mir kurz, sobald du zu Hause bist. Ich freue mich schon sehr auf unser Telefonat später!

Ich liebe dich sehr und vermisse dich jetzt schon.

Kuss,
Dein Andreas"""

    print(f"Sende E-Mail an {to}...")
    result = send_message(to, subject, content)
    if result:
        print("E-Mail erfolgreich versendet!")
    else:
        print("Fehler beim Senden der E-Mail.")

if __name__ == "__main__":
    send_hannah_mail()
