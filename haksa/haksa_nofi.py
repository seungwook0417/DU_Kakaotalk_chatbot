# 2021.07.08 서비스 종료
# import requests
# from setting.card import *
# from setting.answer_main import answer
# # 봇이 아닌 유저라고 알리는 헤더 값
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36",
#     "Accept-Language": "ko",
#     "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
# }
#
# # 학사공지 파싱
# def haksa_Parser():
#     try:
#         url = 'https://portal.daegu.ac.kr/du/Info.do?baordId=15'
#         response = requests.get(url=url)
#         schedule = response.json()
#         data = []
#         # 리스트 카드 형식 제작
#         response = insert_list("대구대학교 학사공지")
#         # 리스트 카드 버튼 추가
#         response = insert_list_button(response,"더보기","https://daegu.ac.kr/article/DG159/list")
#         for a in schedule['infoList']:
#             # 리스트 카드 아이템 추가(양식, 제목, 내용, 이미지, url)
#             response = insert_list_item(response,
#                                         a['subject'],
#                                         a['inpt_date'],
#                                         "https://daegu.ac.kr//resources//images/site/layout/chatbot.png",
#                                         "https://www.daegu.ac.kr/article/DG159/detail/"+a['article_seq'])
#
#         response = answer(response)
#     except:
#         response = insert_text("학교 서버에 문제가 있나봐요 \n 지금은 서비스를 이용하실수 없습니다.")
#         response = answer(response)
#     return response