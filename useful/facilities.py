import json
from setting.card import *
from setting.answer_main import answer

def facilities_parser(content):
    # 강의실 번호 입력
    content = content['action']['detailParams']['facilities']["value"]
    content = ''.join(str(e) for e in content)
    content = content.replace(" ", "")
    url = ""

    try:
        json_data = open('./facil_info.json', 'r', encoding="utf-8").read()
        data = json.loads(json_data)
        title = ""
        description = ""
        for i in data['facilities']:
            if content in i['id'] or content in i['name'] or content in i['sectors']:
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
                break

        if title == "":
            response = insert_text("해당 편의시설을 찾지 못했어요\n ex)편의점 혹은 매점, 복사\n\n혹시 강의실이 검색이 안되나요?😢\n오류제보 통해 제보해주세요!😊")
            response = answer(response)
        else:
            response = insert_card(title, description, url)
            response = insert_button_url(response, "길찾기", location_URL)
            response = answer(response)
        return response

    except:
        pass