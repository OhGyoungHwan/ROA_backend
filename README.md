# ROA_backend

레저렉션 아이템 분석 사이트 백엔드입니다.

자세한사항: https://www.inven.co.kr/board/diablo2/5734/6189?my=post

OCR을 활용해 아이템을 분석해줍니다. 최대옵션을 바로 확인하고 거래 문구를 통해 바로 거래!

정상적인 실행은 위해서는 프론트엔드 서버도 실행해야합니다 -> https://github.com/OhGyoungHwan/ROA/edit/main/README.md

정상적인 백엔드 서버 구동을 위해 tesseract를 설치해야합니다 https://github.com/UB-Mannheim/tesseract/wiki

테서렉트 설치 후 환경변수 또한 등록합니다 https://playground.naragara.com/953

!환경변수 등록 후 꼭 IDE를 다시 켜주세요!

프로젝트설치
> pip install -r requirements.txt
> uvicorn main:app --reload
