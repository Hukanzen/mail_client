#! /usr/bin/python
# -*- coding: utf-8 -*-
#
#   imap_get.py
#
#                       Nov/26/2017
#
# --------------------------------------------------------------------
import sys
import os
import imaplib
import email
from email.header import decode_header, make_header
# --------------------------------------------------------------------
sys.stderr.write("*** 開始 ***\n")
print("日本語")

server = "imap.mail.yahoo.co.jp"

print(str(os.environ["MUser"]))
print(str(os.environ["MPass"]))

user = str(os.environ["MUser"])
password = str(os.environ["MPass"])

try:
    Mm = imaplib.IMAP4_SSL(server)
    Mm.login(user, password)
    Mm.select()
    typ, data = Mm.search(None, 'ALL')
    mailIdList = data[0].split()
    mailIdList.reverse()
    for num in mailIdList:
        print(num)
        typ, data = Mm.fetch(num, '(RFC822)')
        email_message = email.message_from_string(
            data[0][1].decode('iso-2022-jp'))
        print(email_message)
        break
# #
# 		email_from = str(make_header(decode_header(email_message['From'])))
# 		print(email_from)
# 		subject = str(make_header(decode_header(email_message['Subject'])))
# 		print(subject)

# 		msg_encoding = 'iso-2022-jp'

# 		if email_message.is_multipart() == False: # シングルパート
# 			byt  = bytearray(email_message.get_payload(), msg_encoding)
# 			body = byt.decode(encoding=msg_encoding)
# 		else:   # マルチパート
# 			prt  = email_message.get_payload()[0]
# 			byt  = prt.get_payload(decode=True)
# 			body = byt.decode(encoding=msg_encoding)
# #
        # print(body)

    Mm.close()
    Mm.logout()
except Exception as ee:
    sys.stderr.write("*** error ***\n")
    sys.stderr.write(str(ee) + '\n')

sys.stderr.write("*** 終了 ***\n")
# --------------------------------------------------------------------
