from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
import img2option
import datetime


class Type(str, Enum):
    주얼 = "주얼"
    작은부적 = "작은부적"
    거대부적 = "거대부적"
    단도 = "단도"
    도검 = "도검"
    도끼 = "도끼"
    곤봉 = "곤봉"
    철퇴 = "철퇴"
    망치 = "망치"
    셉터 = "셉터"
    지팡이 = "지팡이"
    원드 = "원드"
    창 = "창"
    미늘창 = "미늘창"
    손톱 = "손톱"
    오브 = "오브"
    아마존창 = "아마존창"
    투척단도 = "투척단도"
    투척도끼 = "투척도끼"
    투창 = "투창"
    활쇠뇌 = "활/쇠뇌"
    아마존활 = "아마존활"
    서클릿 = "서클릿"
    투구 = "투구"
    갑옷 = "갑옷"
    장갑 = "장갑"
    방패 = "방패"
    허리띠 = "허리띠"
    신발 = "신발"
    바바투구 = "바바투구"
    드루가죽 = "드루가죽"
    네크토템 = "네크토템"
    팔라방패 = "팔라방패"
    반지 = "반지"
    목걸이 = "목걸이"


class Rarity(str, Enum):
    매직 = "매직"
    레어 = "레어"


app = FastAPI()

origins = [
    "http://172.27.0.1:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/uploadimg/")
async def create_upload_file(file: UploadFile, type: Type, rarity: Rarity):
    images = await file.read()
    option = img2option.img2text(images, type, rarity)
    print(datetime.datetime.now(), option)
    return option
