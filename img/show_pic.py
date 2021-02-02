# Импорты
import pandas as pd                 # Фреймы данных
import matplotlib.pyplot as plt     # ДатаВиз
import numpy as np                  # Массивы и вычисления
import urllib.request as urllib     # Обработка url-ссылок
import cv2                          # OpenCV


def show_pic(addr_pic: str):
    """Визуализирует единичное изображение
    по адресу на локальном ПК
    """
    img_cb = cv2.imread(addr_pic, cv2.IMREAD_GRAYSCALE)
    plt.title('id_pic')
    plt.imshow(img_cb);


def show_pic_bylink(url: str):
    """Визуализирует единичное изображение
    по адресу из url
    """
    resp = urllib.urlopen(url)
    img = np.asarray(bytearray(resp.read()), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)
    plt.title('id_pic')
    plt.imshow(img);


def random_sample(df: pd.DataFrame, negative=False, rows=3, columns=4):
    """
    Возвращает примеры изображений лиц
    в фигуре размерностью row*col по ссылкам
    адресов изображений из df.

    negative - возвращает негатив изображения.

    color:
        IMREAD_UNCHANGED - как есть
        IMREAD_GRAYSCALE - оттенки серого
        IMREAD_COLOR - 3-канальное цветное изображение BGR
        IMREAD_ANYDEPTH - 16-битное / 32-битное
        IMREAD_LOAD_GDAL - драйвер gdal для загрузки изображения
        IMREAD_REDUCED_COLOR_2 - BGR и уменьшить размер на 1/2
        IMREAD_IGNORE_ORIENTATION - не поворачивать с флагом ориентации EXIF
    """
    sns.set_theme()
    # Размер фигуры
    fig = plt.figure(figsize=(rows * 4, columns * 3))
    # Чтение изображений для фигуры в цикле
    for i in range(1, columns * rows + 1):
        x = np.random.choice(df.index)
        img = cv2.imread(df['addr'][x], cv2.IMREAD_GRAYSCALE)
        # При необходимости возвращения негатива
        if negative == True:
            img = np.copy(img)
            w = img.shape[0]
            h = img.shape[1]
            difference = np.reshape([255 for x in range(w * h)], (w, h))
            img = difference - img
        else:
            img = img

        fig.add_subplot(rows, columns, i)
        plt.imshow(img)
        plt.title(f"Id:{x}")
        plt.axis('off')
    plt.show()
    
    
def random_sample_bylink(df: pd.DataFrame, rows=3, columns=4):
    """
    Возвращает примеры изображений лиц
    в фигуре размерностью row*col по url-ссылкам
    адресов изображений из df. Столбец - link (str).

    color:
        IMREAD_UNCHANGED - как есть
        IMREAD_GRAYSCALE - оттенки серого
        IMREAD_COLOR - 3-канальное цветное изображение BGR
        IMREAD_ANYDEPTH - 16-битное / 32-битное
        IMREAD_LOAD_GDAL - драйвер gdal для загрузки изображения
        IMREAD_REDUCED_COLOR_2 - BGR и уменьшить размер на 1/2
        IMREAD_IGNORE_ORIENTATION - не поворачивать с флагом ориентации EXIF
    """
    sns.set_theme()
    # Размер фигуры
    fig = plt.figure(figsize=(rows * 4, columns * 3))
    # Чтение изображений для фигуры в цикле
    for i in range(1, columns * rows + 1):
        x = np.random.choice(df.index)
        resp = urllib.urlopen(df['link'][x])
        img = np.asarray(bytearray(resp.read()), dtype="uint8")
        img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)
        # Добавление изображений к созданной фигуре
        fig.add_subplot(rows, columns, i)
        plt.imshow(img)
        plt.title(f"Id:{x}")
        plt.axis('off')
    plt.show()
