import numpy as np


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
    
