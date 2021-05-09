import json
from setting.card import *
from setting.answer_main import answer

def restaurant_info(content):
    content = content['action']['detailParams']['restaurant']['value']
    content = ''.join(str(e) for e in content)
    content = content.replace(" ", "")
    try:
        json_data = open('./restaurant.json', 'r', encoding="utf-8").read()
        data = json.loads(json_data)
        data_arr = data["restaurant"]
        title = ""
        description = ""
        img_url = ""
        for i in data_arr:
            if content in i['title']:
                title = str(i['title']) + " MENU!!"
                img_url = str(i['img_url'])
                for j in i['menu']:
                    description += (str(j['name']) + " " + str(j['price']) + "원" + "\n")

        if title == "":
            response = insert_text("원하는 식당 정보를 찾지 못했어요 다시 검색해주세요!")
            response = answer(response)
        else:
            response = insert_card(title, description, img_url)
            response = answer(response)
        return response

    except:
        pass