class Inbox:
    def __init__(self):
        self.mails = []

    def add_mail(self, mail):
        self.mails.append(mail)

    def print_headers(self):
        for i, mail in enumerate(self.mails):
            print(f"{i}: ", end="")
            mail.print_header()

    def open(self, index):
        if index < 0 or index >= len(self.mails):
            print("Error: Index out of bounds!")
            return
        mail = self.mails[index]
        mail.mark_as_read()
        mail.print_full()

    def count_unread(self):
        return sum(not mail.read for mail in self.mails)