from setting.card import insert_text, make_reply, insert_replies


# 퀵 리플라이 메인
def answer(response):
    reply = make_reply('🚍 시내버스 도착정보', '시내버스 도착정보')
    response = insert_replies(response, reply)
    reply = make_reply('🏫 강의실 검색', '강의실 검색')
    response = insert_replies(response, reply)
    reply = make_reply('📅 학사일정', '학사일정 뭐야?')
    response = insert_replies(response, reply)
    reply = make_reply('📞 연락처 검색', '부서 연락처 뭐야?')
    response = insert_replies(response, reply)
    reply = make_reply('오류😰 및 건의사항🤔 제보', '오류제보')
    response = insert_replies(response, reply)

    # 2021.07.08 서비스 종료
    # reply = make_reply('⛅ 대구대 현재 날씨', '대구대 날씨')
    # response = insert_replies(response, reply)
    # reply = make_reply('📢 학사공지', '학사공지 뭐야?')
    # response = insert_replies(response, reply)
    # reply = make_reply('🔗 학과사이트 조회', '학과사이트 조회')
    # response = insert_replies(response, reply)
    # reply = make_reply('☕ 편의시설 검색', '대구대 편의시설 정보')
    # response = insert_replies(response, reply)
    # reply = make_reply('🚌 교내셔틀버스', '교내셔틀버스 정보')
    # response = insert_replies(response, reply)

    return response
