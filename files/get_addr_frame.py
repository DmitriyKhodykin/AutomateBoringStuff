# Импорты
import os
import pandas as pd


def get_hierarchy_frame(data_dir: str) -> pd.DataFrame:
    """Возвращает датасет с путями до файлов
    в папке и ее подпапках. Папки помечаются
    как лейблы графических файлов.
    """
    
    folders = os.listdir(data_dir)
    files = []
    for i in folders:
        for j in os.listdir(f'{data_dir}/{i}'):
            files.append([i, data_dir+'/'+i+'/'+j])
    return pd.DataFrame(files, columns=['lbl', 'addr'],
                        index=None)


def get_flat_frame(data_dir: str) -> pd.DataFrame:
      """Возвращает датасет с путями до файлов
      в папке (неразмеченные данные).
      """
        
      files = []
      for i in os.listdir(data_dir):
          files.append([data_dir+'/'+i])
      return pd.DataFrame(files, columns=['addr'],
                          index=None)
