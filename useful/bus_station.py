import requests
import json
from setting.card import *

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36",
    "Accept-Language": "ko",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
}

# !!! 시내버스 디자인 수정 예정

# 교내 시내버스 정류장 도착정보
# 내리리, 비호생활관, 비호생활관 건너, 점자도서관, 점자도서관 건너, 창파도서관, 창파도서관 건너,
# 성산홍, 성산홀 건너, 복지관, 복지관 건너, 대구대 종점, 대구대(정문1), 대구대(정문2), 대구대서문, 내리리입구

def find_bus_Paser(content):
    content = content['action']['detailParams']['find_bus']["value"]
    content = ''.join(str(e) for e in content)
    content = content.replace(" ", "")
    try:
        json_data = open('data.json', 'r', encoding="utf-8").read()
        data = json.loads(json_data)
        text = ""
        BUSSTOPID = ""
        for i in data["bus"]:
            if content in i['busstopName']:
                BUSSTOPID = i['BUSSTOPID']
                break

        if BUSSTOPID != "":
            url = 'http://its.gbgs.go.kr/bus/getMapBusstopInfo'
            response = requests.post(url=url, headers=headers, data={
                'BUSSTOPID': BUSSTOPID
            })
            bus_json = response.json()
            data = []
            # 정류소
            bus_json = bus_json['result']
            # 정류소 도착정보
            arriveInfo = bus_json['arriveInfo']
            # 정류소 이름
            busstopName = bus_json['busstopName']
            if arriveInfo != []:
                for a in arriveInfo:
                    if a['TIMEGAP'] == '전' or a['TIMEGAP'] == '전전' or a['TIMEGAP'] == '전전전':
                        data.append(
                            a['BUSLINENO'] + " 버스🚌" +
                            "\n지금 " + a['TIMEGAP'] + " 정류장에서 \n" + a['NOWBUSSTOPNAME'] + " 했어요" +
                            "\n----------------------------------")
                    else:
                        data.append(
                            a['BUSLINENO'] + " 버스🚌가" +
                            "\n도착 정보: " + a['TIMEGAP'] + "전" +
                            "\n지금 " + a['NOWBUSSTOPNAME'] + "에 있어요" +
                            "\n----------------------------------")

                member_text = '\n'.join(str(e) for e in data)
                member_text = member_text.replace('<span style="color:#f26522;">(저상)</font>', "")
                text = member_text
                title = busstopName['BUSSTOPNAME'] + " 정류장 도착 정보입니다!\n----------------------------------\n"
            else:
                title = busstopName['BUSSTOPNAME'] + "\n정류장의 도착 예정 정보가 없습니다."
        else:
            title = "찾으시는 " + content + " 정류장 정보가 없습니다.\n교내 버스정류장 이름 확인후 재검색 부탁드립니다."

        if text == "":
            response = insert_text(title)
        else:
            response = insert_text(title + text)
    except:
        pass

    return response
