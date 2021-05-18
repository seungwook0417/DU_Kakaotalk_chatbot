import json
from setting.card import *
from setting.answer_main import answer

# 강의실 찾기
def lecture_Parser(content):
    # 강의실 번호 입력
    content = content['action']['detailParams']['find_lecture']["value"]
    content = ''.join(str(e) for e in content)
    content = content.replace(" ", "")
    try:
        # 강의실 데이터 접근
        json_data = open('data.json', 'r', encoding="utf-8").read()
        data = json.loads(json_data)
        title = ""
        location_URL = ""
        description = ""
        response = {'version': '2.0','template': {'outputs': [{"carousel": {"type": "basicCard", "items": []}}], 'quickReplies': []}}
        # 강의실 데이터에서 강의실 찾기
        for i in data['data']:
            # 강의실 번호 혹은 교수 이름
            if content in i['id'] or content in i['name']:
                title = i['name'] + " 입니다."
                description = i['location'] + " " + i['floor'] + "\n"
                location_URL = 'https://map.kakao.com/link/to/' + str(i['type']) + '/'
                response = insert_carousel_card(new_response=response, title=title, description=description)
                response = insert_carousel_button_url(new_response=response, label="길찾기", web_url=location_URL)

        if title == "":
            response = insert_text("해당 강의실을 찾지 못했어요\n ex)공7506 또는 000\n     인1105\n혹시 강의실이 검색이 안되나요?\n오류제보 통해 제보해주세요!😊")
            response = puls_insert_image(response,"https://i.esdrop.com/d/hlogPZr3wi/Duz9RM7WDM.png","강의실 안내")
            response = answer(response)
        else:
            response = answer(response)

        return response

    except:
        pass