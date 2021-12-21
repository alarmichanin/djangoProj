from django.core.mail import EmailMessage
from django.template.loader import get_template


def send_email_info(ticket):

    message = get_template("order_ticket/send_ticket_info.html").render({
                    "ordered_ticket" : ticket})

    mail = EmailMessage(
        subject="Dear customer",
        body=message,
        from_email="nonreply@demo.com",
        to=[ticket.email],
    )
    mail.content_subtype = "html"
    mail.send()    