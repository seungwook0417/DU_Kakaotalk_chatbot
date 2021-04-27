from setting.card import insert_text, make_reply, insert_replies

# 퀵 리플라이 메인
def answer():
    response = insert_text('원하는 정보를 선택해주세요.')
    reply = make_reply('🏫 강의실 검색', '강의실 검색')
    response = insert_replies(response, reply)
    reply = make_reply('🚍 시내버스 도착정보', '시내버스 도착정보')
    response = insert_replies(response, reply)
    reply = make_reply('📅 학사일정', '학사일정 뭐야?')
    response = insert_replies(response, reply)
    reply = make_reply('📢 학사공지', '학사공지 뭐야?')
    response = insert_replies(response, reply)
    reply = make_reply('🚌 교내셔틀버스', '교내셔틀버스 정보')
    response = insert_replies(response, reply)
    reply = make_reply('📞 연락처 검색', '부서 연락처 뭐야?')
    response = insert_replies(response, reply)
    reply = make_reply('오류😰 및 건의사항🤔 제보', '오류제보')
    response = insert_replies(response, reply)
    return response
