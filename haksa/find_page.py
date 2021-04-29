import json
from setting.card import *
from setting.answer_main import answer

# 학과 페이지 찾기
def search_page_Parser(content):
    # 강의실 번호 입력
    content = content['action']['detailParams']['hakgwa ']["value"]
    content = ''.join(str(e) for e in content)
    content = content.replace(" ", "")
    try:
        # 강의실 데이터 접근
        json_data = open('hakgwa.json', 'r', encoding="utf-8").read()
        data = json.loads(json_data)
        title = ""
        location_URL = ""
        description = ""
        # 학과 데이터에서 강의실 찾기
        # 정확한 검색으로만 가능
        for i in data['data']:
            # 강의실 번호 혹은 교수 이름
            if content == i['name']:
                title = i['id']
                description = i['name']
                URL = i['url']
                break;

        if title == "":
            response = insert_text("해당 학과를 찾지 못했어요\n 아래와 같은 양식으로 검색해주세요❗ \n * 직업재할학과\n * 컴퓨터정보공학부(컴퓨터공학전공)\n* 보건행정학과(야간) 😊")
            response = answer(response)
        else:
            response = insert_card(title, description)
            response = insert_button_url(response, "학과 바로가기", URL)
            response = answer(response)
        return response

    except:
        pass