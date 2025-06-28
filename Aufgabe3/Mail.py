class Mail:
    def __init__(self, sender, subject, message, datetime):
        self.sender = sender
        self.subject = subject
        self.message = message
        self.datetime = datetime
        self.read = False

    def __str__(self):
        return f"{self.subject} from {self.sender} on {self.datetime}: {self.message}"

    def mark_as_read(self):
        self.read = True

    def print_header(self):
        print(f"{self.subject} from {self.sender} on {self.datetime}")

    def print_full(self):
        print(f"From: {self.sender}")
        print(f"Subject: {self.subject}")
        print(f"Date: {self.datetime}")
        print(f"Message: {self.message}")
        print(f"Read: {'Yes' if self.read else 'No'}")
