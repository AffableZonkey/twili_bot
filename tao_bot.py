#!/usr/env/python3

"""import requests
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException

account_sid = 'AC9b4a5f48bb29a237a332a0edae356ea8'
auth_token = 'c2eb53dc6803a8f18a949fbfd0b71858'"""

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
            print(junk, line_len)
            if junk == False:
                tao_verse = tao_verse + line
                if line_len <= 1:
                    verse_list.append(tao_verse)
                    tao_verse = ''
    taotxt.close()
    return verse_list

tao_verses = get_tao()
for verse in tao_verses:
    print(verse)
