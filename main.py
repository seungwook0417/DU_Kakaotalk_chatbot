# External Module
from flask import Flask, request, jsonify

# Internal Module
from haksa.haksa_schedule import *  # 학사일정 검색
from haksa.find_lecture_room import *  # 강의실 검색
from haksa.find_member import *  # 구성원 검색
from useful.bus_station import *  # 버스정류장 검색
from useful.error_report import *  # 오류보고 보고서

# 2021.07.08 서비스 종료
from setting.card import *  # 카카오톡 데이터 전송 양식
from setting.answer_main import *  # 퀵 리플라이 지정
from haksa.haksa_nofi import *  # 학사공지 검색
from haksa.find_page import *  # 학과 페이지 검색
from useful.weather_paser import *  # 날씨 검색
from useful.facilities import *

app = Flask(__name__)


# Route urls
# app.route는 flask의 기능으로, '/hello'와 같은 url로 요청이 들어오면 해당 함수만 호출한다.

# 학사일정
@app.route("/schedule", methods=['POST'])
def schedule():
    content = request.get_json()
    response = haksa_chedule_Parser(content)
    return jsonify(response)


# 버스정류장 검색
@app.route("/find_bus", methods=['POST'])
def find_bus():
    content = request.get_json()
    response = find_bus_Paser(content)
    return jsonify(response)


# 강의실 검색
@app.route("/find_lecture", methods=['POST'])
def find_lecture():
    content = request.get_json()
    response = lecture_Parser(content)
    return jsonify(response)


# 구성원 검색
@app.route("/search", methods=['POST'])
def search():
    response = search_Parser()
    return jsonify(response)


# 이름 연락처 찾기
@app.route("/search_member", methods=['POST'])
def search_member():
    content = request.get_json()
    response = search_member_Parser(content)
    return jsonify(response)


# 소속 연락처 찾기
@app.route("/search_buseo", methods=['POST'])
def search_buseo():
    content = request.get_json()
    response = search_buseo_Parser(content)
    return jsonify(response)


# 전화번호로 부서 찾기
@app.route("/search_telno", methods=['POST'])
def search_telno():
    content = request.get_json()
    response = search_telno_Parser(content)
    return jsonify(response)


# 오류보고 보고서
@app.route('/message', methods=['POST'])
def message():
    content = request.get_json()
    response = error_report_answer(content)
    return jsonify(response)


# 학사공지 2021.07.08 서비스 종료
# @app.route("/haksa", methods=['POST'])
# def haksa():
#     response = haksa_Parser()
#     return jsonify(response)

# 편의시설 검색 2021.07.08 서비스 종료
# @app.route("/find_building", methods=['POST'])
# def find_building():
#     content = request.get_json()
#     response = facilities_parser(content)
#     return jsonify(response)

# 학과 페이지 검색 2021.07.08 서비스 종료
# @app.route("/page", methods=['POST'])
# def page():
#     content = request.get_json()
#     response = search_page_Parser(content)
#     return jsonify(response)

# 날씨 검색 2021.07.08 서비스 종료
# @app.route('/weather', methods=['POST'])
# def weather():
#     response = naver_weather_parser()
#     return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="25000", debug=False)
    # app.run()
