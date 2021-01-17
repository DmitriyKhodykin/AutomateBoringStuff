# Импорты
import psycopg2 as psql     # Базы данных
import pandas as pd         # Таблицы и фильтры


def insert_into_db(data: pd.DataFrame, db_name: str,
                  usr_name: str, pswd: str, host_name: str):
    """Вставляет данные из data в table БД"""

    # Авторизация в базе данных
    conn = psql.connect(
        dbname=db_name,
        user=usr_name,
        password=pswd,
        host=host_name
    )

    cursor = conn.cursor()
    print('Создано подключение к БД:', auth.psql_db)
    print('Выполнение запроса...')    

    for index, row in data.iterrows():
        values = (
            row['col1'],
            row['col2'],
            f"{row['col_date']}"
        )

        cursor.execute(
            """
            INSERT INTO 
            table_name (col1, col2, col_date) 
            VALUES (%s, %s, %s)
            """, values
        )

    conn.commit()

    cursor.close()
    print('Подключение к БД завершено')

    conn.close()
    print('Соединение с БД закрыто')
