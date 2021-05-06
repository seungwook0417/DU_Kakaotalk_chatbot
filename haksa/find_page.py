import json
from setting.card import *
from setting.answer_main import answer

# 학과사이트 찾기
def search_page_Parser(content):
    # 학과사이트 입력
    content = content['action']['detailParams']['hakgwa']["value"]
    content = ''.join(str(e) for e in content)
    content = content.replace(" ", "")
    try:
        # 학과사이트 데이터 접근
        json_data = open('hakgwa.json', 'r', encoding="utf-8").read()
        data = json.loads(json_data)
        title = ""
        hakgwa_url = ""
        description = ""
        # 학과사이트 데이터에서 강의실 찾기
        # 정확한 검색으로만 가능, 특수문자X
        for i in data['hakgwa']:
            if content in i['name']:
                title = content+" 페이지를 찾았어요!"
                description = i['id']+"\n"+i['name']
                hakgwa_url = i['url']
                img_url = i['image_url']
                break

        if title == "":
            response = insert_text("해당 학과를 찾지 못했어요\n 아래와 같은 양식으로 검색해주세요❗ \n * 직업재할학과\n * 컴퓨터공학과\n * 보건행정학과😊")
            response = answer(response)
        else:
            response = insert_card(title, description,img_url)
            response = insert_button_url(response, "학과 사이트 바로가기", hakgwa_url)
            response = answer(response)
        return response

    except:
        pass