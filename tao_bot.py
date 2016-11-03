#!/usr/env/python3

from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
from random import choice
from time import sleep
from os import environ


account_sid = environ.get('TWILIO_ACCOUNT_SID')
auth_token = environ.get('TWILIO_AUTH_TOKEN')
client = TwilioRestClient(account_sid, auth_token)

def parse_junk(tao_line):
    junk = False
    if tao_line.startswith('Chapter'):
        junk = True
    else:
        pass
    return(junk)

def get_tao():
    verse_list = []
    tao_verse = ''
    with open('/home/greyman/Factory/twili_bot/taote.mb.txt', 'r') as taotxt:
        for line in taotxt:
            junk = parse_junk(line)
            line_len = len(line)
            if junk == False:
                tao_verse = tao_verse + line
                if line_len <= 1:
                    verse_list.append(tao_verse)
                    tao_verse = ''
    taotxt.close()
    return verse_list

def rando_tao(verse_list):
    send_verse = choice(verse_list)
    return send_verse

def send_tao_verse(rand_verse):
    body = rand_verse
    sms_target = environ.get('TEN_DIG_CELL')
    sms_twili = environ.get('TWILI_NUM')
    try:
        message = client.messages.create(
            body = body,
            to = sms_target,
            from_ = sms_twili)
    except TwilioRestException as e:
        print(e)

def main():
    tao_verses = get_tao()
    rand_verse = rando_tao(tao_verses)
    send_tao_verse(rand_verse)

if __name__ == "__main__":
    main()


