import json
from setting.card import *
from setting.answer_main import answer

# 편의시설 찾기
def facilities_parser(content):
    # 편의시설 종류 입력
    content = content['action']['detailParams']['facilities']["value"]
    content = ''.join(str(e) for e in content)
    content = content.replace(" ", "")

    try:
        # 편의시설 데이터 접근
        json_data = open('./facil_info.json', 'r', encoding="utf-8").read()
        data = json.loads(json_data)
        title = ""
        description = ""
        location_URL = ""
        facil_list = []
        response = {'version': '2.0', 'template': {'outputs': [{"carousel": {"type": "basicCard", "items": []}}], 'quickReplies': []}}
        # 편의시설 종류에 대한 여러 개의 값에 대비하여 2개 이상의 데이터 검색 시 carousel형태 출력
        for i in data['facilities']:
            # 편의시설 종목
            if content in i['sectors']:
                title = str(i['name']) + " 입니다."
                str_f = ""
                str_op = ""
                str_pn = ""
                if(i['floor'] == "지하"):
                    str_f += i['floor']
                else:
                    str_f += (str(i['floor']) + "층")

                str_op += ("\n" + "사무실 번호 " + str(i['office_phone']))
                str_pn += ("\n" + "휴대폰 번호 " + str(i['phone_number']))

                description = i['id'] +" " + str_f +"에 있어요!" + str_op + str_pn
                location_URL = 'https://map.kakao.com/link/to/' + str(i['type']) + '/'
                # 검색 결과값을 리스트에 저장
                facil_list.append(title)
                facil_list.append(description)
                facil_list.append(location_URL)



        if len(facil_list)==0:
            response = insert_text("해당 편의시설을 찾지 못했어요\n ex)편의점 혹은 매점, 복사\n\n혹시 편의시설 검색이 안되나요?😢\n오류제보 통해 제보해주세요!😊")
            response = answer(response)
        else:
            # 반복 횟수만큼 카드 개수 증가
            for t in range(0, int(len(facil_list) / 3)):
                # 케로셀 카드 방식 추가
                response = insert_carousel_card(new_response=response, title=facil_list[(t * 3)], description=facil_list[(t * 3 + 1)])
                response = insert_carousel_button_url(new_response=response, label="길찾기", web_url=facil_list[(t * 3 + 2)])
                # 카드 최대개수 7개 제한
                if t == 6:
                    break
            response = answer(response)

        return response
    except:
        pass

    #cache dict방식
    #facil_dict = {}
    #for i in data['facilities']:
    #    if i["sectors"] not in facil_dict:
    #        facil_dict[str(i["sectors"])] = []

    #response = {'version': '2.0',
    #            'template': {'outputs': [{"carousel": {"type": "basicCard", "items": []}}], 'quickReplies': []}}

    #for i in data['facilities']:
    #    facil_dict[i["sectors"]].append([i["id"]+ " " + i["floor"]+"층에 있어요!\n" + "사무실 번호" + i['office_phone'] + "\n휴대폰 번호 " + i['phone_number']])

    #for key, value in facil_dict.items():
    #    value = '\n'.join(str(e) for e in value)
    #    print(key)
    #    print(value)