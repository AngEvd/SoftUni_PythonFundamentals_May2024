class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    line = input()
    if line == "Stop":
        break
    sender, receiver, content = line.split()
    email = Email(sender, receiver, content)
    emails.append(email)


sent_emails = [int(number) for number in input().split(", ")]

for i in sent_emails:
    emails[i].send()

for email in emails:
    print(email.get_info())
