import os


def get_imlist(path):
    """Возвращает список имен всех jpg-фалов в каталоге"""
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
