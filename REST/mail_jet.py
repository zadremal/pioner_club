import os
from mailjet_rest import Client

API_KEY = os.environ['MJ_APIKEY_PUBLIC']
API_SECRET = os.environ['MJ_APIKEY_PRIVATE']


def send_mail(serialized_data):
    mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')
    name = serialized_data.get("name")
    phone = serialized_data.get("phone")
    date = serialized_data.get("date")
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "info@pioner-club.com",
                    "Name": "Ночной Клуб ПИОНЕР"
                },
                "To": [
                    {
                        "Email": "anton.kamynin@gmail.com",
                    }
                ],
                "Subject": "Новое бронирование столика",
                "TextPart": "заказ",
                "HTMLPart": "<h4>Имя: {} </h4><h4>Телефон: {} </h4> <br />дата заявки {}".format(name, phone, date)
            }
        ]
    }
    result = mailjet.send.create(data=data)

