from Inbox import Inbox
from Mail import Mail

def main():
    inbox = Inbox()

    mail1 = Mail("alice@example.com", "Meeting", "Dont forget our meeting at 10 AM", 10)
    mail2 = Mail("bob@example.com", "Lunch", "Wanna grab lunch today?", 10)
    mail3 = Mail("carol@example.com", "Project", "Please review the project plan.", 10)

    inbox.add_mail(mail1)
    inbox.add_mail(mail2)
    inbox.add_mail(mail3)

    # Einige Mails öffnen
    inbox.open(0)  # öffnet erste Mail
    inbox.open(2)  # öffnet dritte Mail

    # Alle Header anzeigen
    print("\nMailbox Headers:")
    inbox.print_headers()

    # Ungelesene zählen
    print(f"\nUnread emails: {inbox.count_unread()}")


if __name__ == "__main__":
    main()
