# Импорты
import pandas as pd
from auth import auth
import imaplib
import base64
import time
import re


def read_mail():
    """Выгрузка тела каждого письма из почтовой папки.
    Предварительно, на почтовом сервере должна быть создана
    папка Vialon, в которую приходят системные уведомления.
    Формат уведомлений:
        Volvo о565ам31 вошел в ООО КДВ МЖД. 27 окт 2020 13:12:45 он двигался 
        со скоростью 27 км/ч около 'Володарского ул., Армавир, Краснодарский край, Россия'
    """
    
    decode_list = []
    print("Connecting to {}...".format(server))
    imap = imaplib.IMAP4_SSL(server)
    print("Connected! Logging in as {}...".format(login))
    imap.login(login, password)
    print("Logged in! Listing messages...")

    status, select_data = imap.select('Vialon')
    select_data[0].decode('utf-8')  # Количество писем в ящике
    status, search_data = imap.search(None, 'ALL')

    for msg_id in search_data[0].split():
        status, msg_data = imap.fetch(msg_id, '(RFC822)')
        msg_text = (msg_data[0][-1]).decode('utf-8')
        encode_body = msg_text.split('base64')[1][4:-45]
        decode_body = base64.b64decode(encode_body).decode('utf-8')
        decode_body = re.sub(r"'", "", decode_body)
        decode_list.append(decode_body)
        imap.store(msg_id, '+FLAGS', '\\Deleted')
    imap.expunge()
    imap.logout()
    return decode_list
