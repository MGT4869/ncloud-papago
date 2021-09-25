# ncloud-papago

네이버 클라우드 플랫폼 파파고 번역 API 사용을 위한 코드입니다.

## Getting Started

다음을 설치해야 합니다.

- requirements.txt

이후 현재 디렉토리에 `text.txt` 파일을 넣고 `python3 main.py` 를 실행하시기 바랍니다.

## env

디렉토리 내에는 다음의 값을 담은 `.env` 파일이 있어야 합니다.

```shell
# .env
CLIENT_ID=<네이버 API client id>
CLIENT_SECRET=<네이버 API client secret>
```

## results

프로그램 실행 후 결과는 현 디렉토리에 `text_translated.txt` 로 생성됩니다.

예시

```shell
# text.txt

이사 오뚜기가 이제 여름 그 여름의 계절성을 줄이려고 비빔면 대륙의 출시를 하고 있었던 거죠
근데 다행이라면 시장과 같은경우는 최근에 어떤 흐름이냐면 하면 플레어가 농심 오뚜기 삼양 식품이잖아요
```

```shell
# text_translated.txt

This Ottogi was launching Bibimmyeon to reduce the summer seasonality.
Fortunately, the market trend is... Flare is Nongshim Ottogi Samyang food.
```

## reference

[ncloud guide](https://guide.ncloud-docs.com/docs/ko/naveropenapiv3-translation-nmt)
