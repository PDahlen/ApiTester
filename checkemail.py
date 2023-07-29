import imaplib
import email
from email.header import decode_header
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("HOTMAIL_USERNAME")
password = os.getenv("HOTMAIL_PASSWORD")

imap = imaplib.IMAP4_SSL("imap-mail.outlook.com")

imap.login(username, password)

imap.select("Inbox")

status, messages = imap.search(None, 'UNSEEN')

messages = messages[0].split(b' ')
for mail in messages:
    try:
        _, msg = imap.fetch(mail, "(RFC822)")
        for part in email.message_from_bytes(msg[0][1]).walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode()
                print(body)
            # elif part.get_content_type() == "text/html":
            #     body = part.get_payload(decode=True).decode()
            #     soup = BeautifulSoup(body, "html.parser")
            #     print(soup.td + '\n')
            #     print(soup.b + '\n')
            #     print(soup.p + '\n')
            #     print(soup.a + '\n')
            #     print(soup.li + '\n')
            #     print(soup.div + '\n')
            #     print(soup.span + '\n')
            #     print(soup.h2 + '\n')
            #     print(soup.h4 + '\n')
            #     print(soup.mark + '\n')
    except:
        print('No emails')

imap.close()
imap.logout()
