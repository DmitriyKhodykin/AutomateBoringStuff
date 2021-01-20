# Импорты
import imaplib
import base64
import re


def read_mail(folder_name: str, server_name: str,
             usr_name: str, passwd: str) -> list:
    """Выгрузка тела каждого письма из почтовой папки.
    Предварительно, на почтовом сервере должна быть создана
    папка folder_name, в которую приходят сообщения.
    """
    
    decode_list = []
    print(f"Подключение к серверу {server_name}...")
    imap = imaplib.IMAP4_SSL(server)
    print(f"Подключено! Пользователь {usr_name}...")
    imap.login(usr_name, passwd)
    print("Чтение сообщений...")

    status, select_data = imap.select(folder_name)
    select_data[0].decode('utf-8')  # Количество писем в ящике
    status, search_data = imap.search(None, 'ALL')

    for msg_id in search_data[0].split():
        status, msg_data = imap.fetch(msg_id, '(RFC822)')
        msg_text = (msg_data[0][-1]).decode('utf-8')
        encode_body = msg_text.split('base64')
        decode_body = base64.b64decode(encode_body).decode('utf-8')
        decode_body = re.sub(r"'", "", decode_body)
        decode_list.append(decode_body)
        imap.store(msg_id, '+FLAGS', '\\Deleted')
    imap.expunge()
    imap.logout()
    print("Выполнено. Выход из учетной записи...")
    return decode_list
