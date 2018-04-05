import requests
import time
from telegram.ext import Updater
updater = Updater(token='425230215:AAFeRok-eTd04tefgd4iETwq5awsenEKtsI')
dispatcher = updater.dispatcher

# body = {
#     "station_id_from": 2200001,
#     "station_id_till": 2204570,
#     "date_dep": "06.04.2018",
#     "time_dep": "00:00"
# }

body = {
    "from": 2200001,
    "to": 2204570,
    "date": "2018-04-06",
    "time": "00:00"
}

while True:
    response = requests.post('https://booking.uz.gov.ua/train_search/', data=body)

    data = response.json()

    train_nums = [(i['num'], i.get('types')) for i in data['data']['list']]
    print(train_nums)

    for i in train_nums:
        if (i[0] == '726К' and len(i[1]) > 0) or (i[0] == '720П' and len(i[1]) > 0):
            updater.bot.send_message('-268366786', '@bu_ol CHECK TICKETS!!!!!')
    #
    time.sleep(90)
