import requests
import json
from setting.card import *
from setting.answer_main import answer
from datetime import datetime

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36",
    "Accept-Language": "ko",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
}


# tools
# 버스 실시간 정보 조회
# 'forwardPosition': [{'NODER': 1, 'BUSID': '081909', 'BUSDIRECTCD': '1', 'RCVTIME': '20210429162519',
#                      'GISY_5181': None, 'BUSSTOPID': '360054800', 'NGISX': 181860.7624, 'NGISY': 267756.9926,
#                      'BUSTYPE': 'N', 'CARNO': '1909', 'NODEID': '3609554800', 'GISX_5181': None},
# "forwardStation": [{"NODEORDER": 1, "GISY_5181": null, "BUSSTOPID": "360054800", "NGISX": 181860.7624,
#                     "NGISY": 267756.9926, "BUSSTOPNAME": "경일대종점", "GISX_5181": null },
def get_bus_line_node_list(bus_line_id: str):
    r = requests.post("http://its.gbgs.go.kr/bus/getBusLineNodeList/", headers=headers, data={
        "BUSLINEID": bus_line_id,
    })

    response_json = r.json()

    if response_json["success"] is not True:
        raise ValueError

    return {
        'forwardPosition': response_json["result"]["forwardPosition"],
        "reversePosition": response_json["result"]["reversePosition"],
        "forwardStation": response_json["result"]["forwardStation"],
        "reverseStation": response_json["result"]["reverseStation"],
    }


# 차 번호를 이용하여 노선의 방향을 반환한다.
def get_bus_direction(car_no, line_node_list):
    for car in line_node_list["forwardPosition"] + line_node_list["reversePosition"]:
        if car_no == car["CARNO"]:
            return car["BUSDIRECTCD"]

    return None


# 시내버스 도착정보
def find_bus_Paser(content):
    # 버스 정보 입력
    content = content['action']['detailParams']['find_bus']["value"]
    content = ''.join(str(e) for e in content)
    content = content.replace(" ", "")
    # 버스정보 데이터 접근
    try:
        json_data = open('data.json', 'r', encoding="utf-8").read()
        data = json.loads(json_data)
        BUSSTOPID = ""
        for i in data["bus"]:
            if content in i['busstopName']:
                BUSSTOPID = i['BUSSTOPID']
                break

        # 경산시 교통정보센터 API 사용
        url = 'http://its.gbgs.go.kr/bus/getMapBusstopInfo'
        response = requests.post(url=url, headers=headers, data={
            'BUSSTOPID': BUSSTOPID
        })
        bus_json = response.json()
        # 정류소
        bus_json = bus_json['result']
        # 정류소 도착정보
        arriveInfo = bus_json['arriveInfo']
        # 정류소 이름
        busstopName = bus_json['busstopName']

        # 행선지를 표기할 리스트. 버스번호/line_id
        display_bus_dest_list = {
            "840": "3000840000"
        }

        # 행선지별 디스플레이 할 텍스트. "1" 이 정방향, "0"이 역방향
        bus_dest_text = {
            "840": {
                "1": "영남대",
                "0": "하양",
            }
        }

        # node_line_list 를 캐시 해 놓을 dict
        bus_line_node_list_cache = {

        }

        # 정렬할 버스 리스트. 버스번호
        display_bus_num_list = {
            "840(영남대)": [],
            "840(하양)": [],
            "818-1": [],
            "708": [],
            "818(대구대)": [],
            "818(황제)": [],
            "814": [],
            "급행5": [],
            "399": [],
            "진량1": []
        }
        # 캐시 리스트 방식 보류
        # display_bus_num_list = {
        #
        # }

        if arriveInfo != []:
            for a in arriveInfo:
                bus_name = a['BUSLINENO'].replace('<span style="color:#f26522;">(저상)</font>', "")
                bus_dest = ""
                print(bus_name)
                # 행선지 표기 대상이면 추가 텍스트 삽입
                if bus_name in display_bus_dest_list:
                    current_line_id = display_bus_dest_list[bus_name]

                    # 캐시에 node_line_list 가 있는지 확인 후 없으면 새로 가져온다.
                    if current_line_id not in bus_line_node_list_cache:
                        bus_line_node_list_cache[current_line_id] = get_bus_line_node_list(current_line_id)

                    # CARTERMID 끝 4자리로 버스 번호를 확인하고 버스의 방향을 구한다.
                    bus_dest_code = get_bus_direction(
                        car_no=a['CARTERMID'][-4:],
                        line_node_list=bus_line_node_list_cache[current_line_id]
                    )

                    # 버스 방향에 맞는 텍스트를 저장한다.
                    bus_dest = f"({bus_dest_text[bus_name][bus_dest_code]})"

                # 도착시간 정보 확인
                arrive_time = a['PREDICTTIME']
                arrive_time = datetime.strptime(arrive_time, "%Y%m%d%H%M%S")

                # 리스트에 들어있는 버스이면 동작
                if bus_name + bus_dest in display_bus_num_list:
                    # 가독성을 위한 문구수정
                    a['NOWBUSSTOPNAME'] = a['NOWBUSSTOPNAME'].replace("출발", "정류소 출발")
                    a['TIMEGAP'] = a['TIMEGAP'].replace("분", "분 후")

                    # 정렬할 버스 리스트 삽입
                    display_bus_num_list[bus_name + bus_dest].append(
                        f"- {a['TIMEGAP']}({arrive_time.strftime('%H시 %M분)도착 예정')} \n   Now: {a['NOWBUSSTOPNAME']}\n")

                    # 케로셀 카드 형식 지정
                    response = {'version': '2.0', 'template': {
                        'outputs': [{"simpleText": {"text": busstopName['BUSSTOPNAME'] + " 정류장 도착 정보"}},
                                    {"carousel": {"type": "basicCard", "items": []}}], 'quickReplies': []}}

                    # 여러 결과값 출력을 위한 carousel 카드 삽입
                    for key, value in sorted(display_bus_num_list.items(), reverse=True):
                        if value != []:
                            value = '\n'.join(str(e) for e in value)
                            response = insert_carousel_card(response, "🚌" + key, value)

                    response = answer(response)
                else:
                    title = busstopName['BUSSTOPNAME'] + "\n정류장의 도착 예정 정보가 없습니다."
                    response = insert_text(title)
                    response = answer(response)

                # 캐시 리스트 방식 보류
                # if bus_name + bus_dest not in display_bus_num_list:
                #     display_bus_num_list[bus_name + bus_dest] = []
                #
                # if a['NOWBUSSTOPNAME'] == "출발":
                #     a['NOWBUSSTOPNAME'] = "정류소 출발"
                #
                # a['TIMEGAP'] = a['TIMEGAP'].replace("분", "분 후")
                #
                # display_bus_num_list[bus_name + bus_dest].append(
                #     f"- {a['TIMEGAP']}({arrive_time.strftime('%H시:%M분)도착 예정')} \n   Now: {a['NOWBUSSTOPNAME']}\n")

                # response = {'version': '2.0', 'template': {
                #     'outputs': [{"simpleText": {"text": busstopName['BUSSTOPNAME'] + " 정류장 도착 정보"}},
                #                 {"carousel": {"type": "basicCard", "items": []}}], 'quickReplies': []}}
                #
                # for key, value in sorted(display_bus_num_list.items()):
                #     if value != []:
                #         value = '\n'.join(str(e) for e in value)
                #         response = insert_carousel_card(response, "🚌" + key, value)
                # response = answer(response)
                #                 else:
                #                     title = busstopName['BUSSTOPNAME'] + "\n정류장의 도착 예정 정보가 없습니다."
                #                     response = insert_text(title)
                #                     response = answer(response)
        else:
            title = busstopName['BUSSTOPNAME'] + "\n정류장의 도착 예정 정보가 없습니다."
            response = insert_text(title)
            response = answer(response)

            # 미안하지만 잠시 뺌(건우 버스 사이트)
            # response = plus_card(response,"전체 버스 보기","")
            # response = insert_button_url(response, "바로가기", "http://bus.dryrain.me:5000/bus.html#"+busstopName['BUSSTOPNAME']+"/"+BUSSTOPID)
            # response = answer(response)
    except:
        pass

    return response
