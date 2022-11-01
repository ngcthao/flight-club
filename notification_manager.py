import smtplib as mail


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self, fd):
        self.text_body = f"Low price alert! Only £{fd['price']} to fly from {fd['from_city']}-{fd['from_code']} " \
                         f"to {fd['to_city']}-{fd['to_code']}, from {fd['from_date']} to {fd['to_date']}. "
        if fd['via_city']:
            self.text_body += f"There is {fd['stop_overs']} stopover at {fd['via_city']}."

    def send_emails(self, users, email, password):
        print(self.text_body)
        for user in users:
            with mail.SMTP("smtp.gmail.com") as connect:
                connect.starttls()
                connect.login(user=email, password=password)
                connect.sendmail(
                    from_addr=email,
                    to_addrs=user['email'],
                    msg=f"Subject: New Flight Deal!\n\nHello {user['lastName']},\n\n{self.text_body}".encode('utf-8')
                )