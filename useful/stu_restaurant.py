import json
from setting.card import *
from setting.answer_main import answer

def restaurant_info(content):
    # 식당 건물 정보 입력
    content = content['action']['detailParams']['restaurant']['value']
    content = ''.join(str(e) for e in content)
    content = content.replace(" ", "")
    try:
        # 식당 데이터 접근
        json_data = open('./restaurant.json', 'r', encoding="utf-8").read()
        data = json.loads(json_data)
        data_arr = data["restaurant"]
        title = ""
        description = ""
        img_url = ""
        category1 = "========분식========" # 분식
        category2 = "========한식========" # 한식
        category3 = "========양식========" # 양식
        for i in data_arr:
            # 파람에 부합하는 데이터 찾기
            if content in i['title']:
                img_url = str(i['img_url'])
                for j in i['menu']:
                    if str(j['category']) =="분식":
                        category1 += ("\n" + str(j['name']) + " " + str(j['price']) + "원")
                    elif str(j['category']) =="한식":
                        category2 += ("\n" + str(j['name']) + " " + str(j['price']) + "원")
                    elif str(j['category']) == "양식":
                        category3 += ("\n" + str(j['name']) + " " + str(j['price']) + "원")
                    else:
                        continue
        description += category1+"\n"+category2+"\n"+category3

        if title == "":
            response = insert_text("원하는 식당 정보를 찾지 못했어요 다시 검색해주세요!")
            response = answer(response)
        else:
            response = insert_card(title, description, img_url)
            response = answer(response)
        return response

    except:
        pass

    # 판매중지 조건 코드
    #if (str(j['price']) == ""):
    #    description += (str(j['name']) + " " + "판매중지" + "\n")
    #else:
    #    description += (str(j['name']) + " " + str(j['price']) + "원" + "\n")