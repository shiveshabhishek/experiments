#!/usr/bin/python
from httplib2 import Http
from json import dumps
import datetime
import time

def main():
    matcher=0
    now = datetime.datetime.now()
    matcher= now.hour+1
    if(matcher==24):
        matcher=0
    curr_time=("{}".format(matcher))
    # ENTER YOUR WEBHOOK URL BELOW
    url = 'YOUR/WEBHOOK/URL/HERE'
    bot_message = {
        'text' : 'Ting Tong!! The time is `'+curr_time+'`',
        'mrkdwn' : True}

    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()
    while 1:
        time.sleep(60)
        now = datetime.datetime.now()
        if(now.hour==matcher):
            response = http_obj.request(
                uri=url,
                method='POST',
                headers=message_headers,
                body=dumps(bot_message),
            )
            # TO SEE THE RESPONSE UNCOMMENT THE BELOW LINE
            # print(response)
            main()

if __name__ == '__main__':
    main()

