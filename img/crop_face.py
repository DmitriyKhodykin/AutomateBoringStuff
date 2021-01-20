# Импорты
import cv2
from mtcnn.mtcnn import MTCNN  # Детектор лиц
import warnings


def get_crop_face(df, id_pic):
  """
  Определяет лицо на фото и возвращает
  срез аватара на фото
  """
  
  detector = MTCNN()
  warnings.filterwarnings("ignore")
  # Чтение изображения
  image = cv2.imread(df['addr'][id_pic], cv2.IMREAD_GRAYSCALE)
  # Копирование изображения
  image_copy = cv2.imread(df['addr'][id_pic])
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
