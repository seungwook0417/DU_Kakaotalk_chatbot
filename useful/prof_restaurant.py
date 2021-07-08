##교직원 식당 추가기능
# 개발 중단
# import json
# import time
# from setting.card import *
# from setting.answer_main import answer
#
#
# # 교직원 식당 식단 출력
# def pf_restaurant():
#     # 식단 데이터 접근
#     json_data = open('pf_restaurant.json', 'r', encoding="utf-8").read()
#     data = json.loads(json_data)
#
#     date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#
#     # 매일 변경되는 교직원 식당 한정
#     restaurant = ["복지관", "웅지관"]
#
#     response = {'version': '2.0', 'template': {
#         'outputs': [{"simpleText": {"text": "오늘의 식단"}},
#                     {"carousel": {"type": "basicCard", "items": []}}], 'quickReplies': []}}
#
#     # 리스트 삽입 및 출력 코드
#     for i in restaurant:
#         try:
#             a = data[str(date)][i]
#             price = a["price"]
#             menu_total = []
#             if a['menu'] != []:
#                 for menu in a['menu']:
#                     menu_total.append(menu)
#             else:
#                 menu_total.append("오늘 등록된 식단이 없습니다.")
#
#             menu = '\n'.join(str(e) for e in menu_total)
#             response = insert_carousel_card(response, i + "식단(" + price + ")", menu)
#             response = answer(response)
#         except:
#             continue
#     return response
