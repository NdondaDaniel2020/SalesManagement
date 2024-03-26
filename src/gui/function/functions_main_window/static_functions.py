import os
import random


def generate_barcode() -> str:
    codigo: str = ""
    for _ in range(13):
        codigo += str(random.randint(0, 9))

    return codigo


def reduce_url(url: str) -> str:
    if len(url) > 24:
        url = os.path.normpath(url).split('\\')
        url = (*url[:4], '....', url[-1])
        url = '\\'.join(url)

        return url

    return url
