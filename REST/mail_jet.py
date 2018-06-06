import os
from mailjet_rest import Client

from datetime import *

API_KEY = os.environ['MJ_APIKEY_PUBLIC']
API_SECRET = os.environ['MJ_APIKEY_PRIVATE']


def send_mail(serialized_data, recipient, subject, type):
    mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')


    name = serialized_data.get("name")
    phone = serialized_data.get("phone")
    email = serialized_data.get("email")
    date = serialized_data.get("date")
    try:
        birthday_date = serialized_data.get("birthday_date").strftime("%d.%m")
    except AttributeError:
        birthday_date = datetime.now().strftime("%d.%m")


    html_body = {
        "banket" : "<h4>Имя: {} </h4><h4>Телефон: {} </h4> <h4>Email: {} </h4> <br />дата заявки {}".format(name, phone, email, date),
        "birthday": "<h4>Имя: {} </h4> <h4>Телефон: {} </h4> <h4>День Рождения: {} </h4> <br />дата заявки {}".format(name, phone, birthday_date, date),
        "reserve": "<h4>Имя: {} </h4><h4>Телефон: {} </h4> <br />дата заявки {}".format(name, phone, date)

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
                        "Email": recipient,
                    }
                ],
                "Subject": subject,
                "TextPart": "заказ",
                "HTMLPart": html_body[type]
            }
        ]
    }

    result = mailjet.send.create(data=data)

