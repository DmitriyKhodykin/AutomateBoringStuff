import numpy as np      # Массивы и вычисления
import cv2              # OpenCV


def psa_img(img):
    """
    Проецирует матрицу изображения
    на одну ось пространства (вектор)
    методом главных компонент - PSA
    """
    covmat = np.cov(img)
    _, vecs = np.linalg.eig(covmat)
    v = -vecs[:, 1]
    vec = np.dot(v, img)
    return vec
    

def psa_pic(addr: str) -> np.array:
    """
    Проецирует матрицу изображения
    на одну ось пространства (вектор).
    addr - локальный путь к файлу.
    """
    img = cv2.imread(addr, cv2.IMREAD_GRAYSCALE)
    covmat = np.cov(img)
    _, vecs = np.linalg.eig(covmat)
    v = -vecs[:, 1]
    vec = np.dot(v, img)
    return vec
