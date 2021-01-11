# Импорты

## Базы данных
import psycopg2 as psql

## Регистрационные данные
from auth import auth


def insert_into_db(data: PandasDataFrame, col_list: list, table_db: str):
    """Вставляет в таблицу базы данных PostgreSQL N-строк из внешнего 
    фрейма данных - data - по строковым наименованиям столбцов - col_list"""

    # Авторизация в базе данных
    conn = psql.connect(
        dbname=auth.psql_db,
        user=auth.psql_user,
        password=auth.psql_passwd,
        host='localhost'
    )

    cursor = conn.cursor()
    print('Создано подключение к БД:', auth.psql_db)
    print('Выполнение запроса...')    

    for index, row in data.iterrows():
        for i in col_list:
            values = (
                row[i]
            )

        cursor.execute(
            f"INSERT INTO {table_db} ({col_list}) VALUES ({'s,' * len(col_list)})",
            values
        )

    conn.commit()

    cursor.close()
    print('Подключение к БД завершено')

    conn.close()
    print('Соединение с БД закрыто')
