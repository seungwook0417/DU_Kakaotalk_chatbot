import json
from setting.card import *

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
        # 강의실 데이터에서 강의실 찾기
        # 반복문으로 첫번째 값만 찾는데 학과가 여러개 검색될 경우 선택해서 정보가 나오게 변경 필요
        for i in data['data']:
            # 강의실 번호 혹은 교수 이름
            if content in i['id'] or content in i['name']:
                title = i['name'] + " 입니다."
                description = i['location'] + " " + i['floor'] + "\n"
                location_URL = '"https://map.kakao.com/link/to/' + str(i['type']) + '/"'
                break;

        if title == "":
            response = insert_text("해당 강의실을 찾지 못했어요\n ex)공7506 또는 000\n\n혹시 강의실이 검색이 안되나요?😢\n오류제보 통해 제보해주세요!😊")
        else:
            response = insert_card(title, description)
            response = insert_button_url(response, "길찾기", location_URL)

        return response

    except:
        pass