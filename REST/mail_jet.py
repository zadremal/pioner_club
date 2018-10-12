import os
from mailjet_rest import Client

from datetime import *
API_KEY = os.environ['MJ_APIKEY_PUBLIC']
API_SECRET = os.environ['MJ_APIKEY_PRIVATE']
EMAIL = os.environ['SUBMISSION_EMAIL']


def send_mail(serialized_data, subject, mail_type):

    mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')
    name = serialized_data.get("name")
    phone = serialized_data.get("phone")
    email = serialized_data.get("email")
    mail_date = serialized_data.get("date")
    message = serialized_data.get("text")
    try:
        birthday_date = serialized_data.get("birthday_date").strftime("%d.%m")
    except AttributeError:
        birthday_date = datetime.now().strftime("%d.%m")

    html_body = {
        "banket": "<h4> Имя: {} </h4>"
                  "<h4> Телефон: {} </h4>"
                  "<h4>Email: {} </h4>"
                  "<br />дата заявки {}".format(name, phone, email, mail_date),
        "birthday": "<h4> Имя: {} </h4> "
                    "<h4>Телефон: {} </h4>"
                    "<h4>День Рождения: {} </h4>"
                    "<br />дата заявки {}".format(name, phone, birthday_date, mail_date),
        "reserve": "<h4>Имя: {} </h4>"
                   "<h4>Телефон: {} </h4>"
                   "<br />дата заявки {}".format(name, phone, mail_date),
        "feedback": "<h4>Имя: {} </h4>"
                    "<h4>Email: {} </h4>"
                    "<h4> Сообщение:</h4>"
                    "<p> {} </p>".format(name, email, message),
        "newyear": "<h4>Имя: {} </h4>"
                   "<h4>Телефон: {} </h4>"
                   "<br />дата заявки {}".format(name, phone, mail_date),
        "newyear_corporate": "<h4>Имя: {} </h4>"
                             "<h4>Телефон: {} </h4>"
                             "<br />дата заявки {}".format(name, phone, mail_date),

    }
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "info@pioner-club.com",
                    "Name": "Ночной Клуб ПИОНЕР"
                },
                "To": [
                    {
                        "Email": EMAIL,
                    }
                ],
                "Subject": subject,
                "TextPart": "заказ",
                "HTMLPart": html_body[mail_type]
            }
        ]
    }

    mailjet.send.create(data=data)
