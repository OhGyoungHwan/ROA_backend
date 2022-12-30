import pytesseract
import cv2
import matplotlib.pyplot as plt
import re
import numpy as np
import pandas as pd
import optioncompiler
import logging


def imgfile_preprocessing(imgfile):
    """
    Input: bytes (image)
    Output: numpy.ndarray (image)

    읽혀진 이미지파일을 전처리 후 노이즈가 제거된 2진 이미지파일로 돌려준다.
    """
    image_nparray = np.asarray(bytearray(imgfile), dtype=np.uint8)
    # binary이미지 파일을 numpy array로 변환
    org_image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
    # numpy array를 이미지로 디코딩
    hsv_image = cv2.cvtColor(org_image, cv2.COLOR_BGR2HSV)
    # 이미지를 BGR에서 HSV로 변환
    binary_image = cv2.threshold(
        hsv_image[:, :, 2], 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # 흑백이미지를 2진 이미지로 변환
    return binary_image


def text_separateoption(text, type, rarity):
    compile_RE = optioncompiler.DICT_OPTION_COMPILER[type+rarity]
    option_compiler = re.compile(r'{0}'.format(compile_RE))
    matchobj = option_compiler.findall(text)
    option_list = [i.replace(' ', '') for i in matchobj]
    option_figure_list = ["/".join(re.findall(r'\d+', i)) for i in option_list]
    option_name_list = ["".join(re.findall(r'[^0-9+%(){}\-]+', i))
                        for i in option_list]
    return dict(zip(option_name_list, option_figure_list))


def img2text(img, type, rarity):
    """
    Input: bytes (image), type (text: enum), rarity (text: enum)
    Output: json

    들어온 이미지를 분석해 아이템 옵션을 추출하고 json형태로 돌려준다.
    """
    processed_img = imgfile_preprocessing(img)

    text = pytesseract.image_to_string(
        processed_img, lang='kor', config="--psm 4")
    text = text.replace("7|", "기")
    logging.info(text)

    return text_separateoption(text, type, rarity)
