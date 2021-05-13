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
        description = ""
        facil_dict = {}

        # simpleText 방식과 carousel 방식을 추가한 값
        response = {'version': '2.0', 'template': {
            'outputs': [{"simpleText": {"text": content + " 위치 정보에요!"}},
                        {"carousel": {"type": "basicCard", "items": []}}], 'quickReplies': []}}

        # dictionary key값 저장
        for i in data['facilities']:
            if i["sectors"] not in facil_dict:
                facil_dict[str(i["sectors"])] = []

        # dictionary value값 리스트 형태로 저장
            facil_dict[i["sectors"]].append(
                [i["id"] + " " + i["floor"] + "층에 있어요!", "사무실 번호" + i['office_phone'] + "\n휴대폰 번호 " + i['phone_number'],
                 "https://map.kakao.com/link/to/" + str(i["type"]) + "/"])

        # key, value값 carousel 카드 형태로 삽입
        for key, value in facil_dict.items():
            if key == content:
                for i in value:
                    title = i[0]  # 층수 정보
                    description = i[1]  # 사무실 번호 및 담당자 번호
                    location_url = i[2]
                    response = insert_carousel_card(new_response=response, title=title, description=description)
                    response = insert_carousel_button_url(new_response=response, label="길찾기", web_url=location_url)

        # key값 정보가 없을 경우
        if description == "":
            title = content + " 위치정보가 없어요!! 다른 검색어를 입력해 주세요!!"
            response = insert_text(title)
            response = answer(response)
        else:
            response = answer(response)

        return response
    except:
        pass

