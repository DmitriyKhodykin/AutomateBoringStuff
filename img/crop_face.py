# Импорты
import cv2
from mtcnn.mtcnn import MTCNN       # Детектор лиц
import warnings


def get_crop_face(addr_pic: str):
    """Определяет лицо на фото и возвращает
    срез аватара на фото.
    addr_pic = путь к локальному файлу исходного изображения.
    """

    detector = MTCNN()
    warnings.filterwarnings("ignore")
    # Чтение изображения
    image = cv2.imread(addr_pic, cv2.IMREAD_GRAYSCALE)
    # Копирование изображения
    image_copy = cv2.imread(addr_pic)
    # ================= Обрезка лица ===================
    # image_markup возвращает список словарей с границами
    # лица, а также его основных элеменов (глаз, носа, рта)
    image_markup = detector.detect_faces(image_copy)
    # coordinates возвращает четыре значения:
    ## x- и y- координаты верхней левой вершины лица, 
    ## ширину и высоту прямоугольника, содержащего лицо
    coordinates = image_markup[0]['box']
    # ==================================================
    # Обрезка лица,
    # срез картинки: crop_img = img[y:y+h, x:x+w]
    crop_im =  image[coordinates[1]:coordinates[1] + coordinates[3],
                     coordinates[0]-10:coordinates[0] + coordinates[2]+10]
    # Изменение размера изображения
    resize_im = cv2.resize(crop_im, (128, 128))
    return resize_im


def crop_and_psa_bylink(url: str):
    """
    Определяет лицо на фото (по url) и возвращает
    его вектор, полученный методом PSA
    """
    detector = MTCNN()

    # Чтение изображения
    try:
        resp = urllib.urlopen(url)
        img = np.asarray(bytearray(resp.read()), dtype="uint8")
        img = cv2.imdecode(img, cv2.IMREAD_UNCHANGED)

        try:
            warnings.filterwarnings("ignore")
            # image_markup возвращает список словарей с границами
            # лица, а также его основных элеменов (глаз, носа, рта)
            image_markup = detector.detect_faces(img)

            # coordinates возвращает четыре значения:
            ## x- и y- координаты верхней левой вершины лица, 
            ## ширину и высоту прямоугольника, содержащего лицо
            coordinates = image_markup[0]['box']

            # Срез картинки: crop_img = img[y:y+h, x:x+w]
            crop_im =  img[coordinates[1]:coordinates[1] + coordinates[3],
                         coordinates[0]-10:coordinates[0] + coordinates[2]+10]

            # Преобразование в оттенки серого
            try:
                gray_im = cv2.cvtColor(crop_im, cv2.COLOR_BGR2GRAY)
            except BaseException:
                print(f'Не удалось преобразовать в оттенки серого {url}')
                vec = None
                return vec

            # Изменение размера изображения
            resize_im = cv2.resize(gray_im, (128, 128))

            # Применение PSA
            vec = psa_img(resize_im)
            return vec

        except ValueError:
            print(f'Нет изображения {url}')
            vec = None
            return vec

        except IndexError:
            print(f'Не удалось обнаружить аватар {url}')
            vec = None
            return vec

    except HTTPError:
        print(f'Не удалось прочитать {url}')
        img = None
        return img

    return vec
