# Импорты
import matplotlib.pyplot as plt
import cv2


def show_pic(addr_pic: str):
    """Возвращает изображение"""
    
    img_cb = cv2.imread(addr_pic, cv2.IMREAD_GRAYSCALE)
    plt.title(id_pic)
    plt.imshow(img_cb);
