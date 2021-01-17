# Импорты
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(text: str, work_smtp: str, addr_from: str, 
              addr_to: str, paswd: str):
    """Отправка письма через SMTP-сервер, где:
        - work_smtp = почтовый сервер, например, mail.smtp.ru,
        - addr_from = адрес отправителя,
        - addr_to = адрес получателя,
        - paswd = пароль для входа на почтовый сервер
    """
    
    # Атрибуты письма
    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = addr_to
    msg['Subject'] = 'Тема письма'
    
    body = text
    msg.attach(MIMEText(body, 'plain'))

    # Настройки и статус сервера
    print('Подключение к серверу...')
    server = smtplib.SMTP_SSL(work_smtp, 465)
    print('Вход в учетную запись...')
    server.login(addr_from, paswd)
    print('Готов к отправке сообщения...')
    server.send_message(msg)
    server.quit()
    print('Сообщение отправлено')
