# 개발중단
# import json
# from setting.card import *
# from setting.answer_main import answer
#
# def restaurant_info(content):
#     # 식당 건물 정보 입력
#     content = content['action']['detailParams']['restaurant']['value']
#     content = ''.join(str(e) for e in content)
#     content = content.replace(" ", "")
#     try:
#         # 식당 데이터 접근
#         json_data = open('./restaurant.json', 'r', encoding="utf-8").read()
#         data = json.loads(json_data)
#         data_arr = data["restaurant"]
#         title = ["분식", "한식", "양식"]
#         category =["", "", ""]
#         for i in data_arr:
#             # 파람에 부합하는 데이터 찾기
#             if content in i['title']:
#                 for j in i['menu']:
#                     category_index = title.index(j['category'])
#                     if (str(j['price']) == ""):
#                         category[category_index] += ("\n" + str(j['name']) + " " + "판매중지")
#                     else:
#                         category[category_index] += ("\n" + str(j['name']) + " " + str(j['price']) + "원")
#
#         for i in range(0, 3):
#             #현) 케로셀 카드방식, 변경예정) 케로셀 텍스트 방식
#             response = insert_carousel_card(new_response=response, title=title[i], description=category[i])
#         response = answer(response)
#         return response
#
#     except:
#         pass
#
#     # 일반 카드 적용 코드
#     # category_description = ["========분식========", "========한식========", "========양식========"]
#     # title = ["분식", "한식", "양식"]
#     # for i in data_arr:
#     #    # 파람에 부합하는 데이터 찾기
#     #    if content in i['title']:
#     #        img_url = str(i['img_url'])
#     #        for j in i['menu']:
#     #           category_index = title.index(j['category'])
#     #           category_description[category_index] += ("\n" + str(j['name']) + " " + str(j['price']) + "원")
#     # for t in category_description:
#     #   description += t
#     #if title == "":
#     #    response = insert_text("원하는 식당 정보를 찾지 못했어요 다시 검색해주세요!")
#     #    response = answer(response)
#     #else:
#     #    response = insert_card(title, description, img_url)
#     #    response = answer(response)
#     #return response