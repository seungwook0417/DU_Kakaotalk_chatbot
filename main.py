# External Module
from flask import Flask, request, jsonify

# Internal Module
from setting.card import * # 카카오톡 데이터 전송 양식
from setting.welcome import * # 환영인사
from setting.answer_main import * # 퀵 리플라이 지정
from haksa.haksa_nofi import * # 학사공지 검색
from haksa.haksa_schedule import * # 학사일정 검색
from haksa.find_lecture_room import * # 강의실 검색
from haksa.find_building_room import * # 편의시설 검색
from haksa.find_member import * # 구성원 검색
from haksa.find_page import * # 학과 페이지 검색
from useful.bus_station import * # 버스정류장 검색
from useful.error_report import * # 오류보고 보고서
from useful.weather_paser import * # 날씨 검색

app = Flask(__name__)

# Route urls
# app.route는 flask의 기능으로, '/hello'와 같은 url로 요청이 들어오면 해당 함수만 호출한다.

# 환영인사
@app.route("/hello", methods=['POST'])
def hello():
    response = answer()
    return jsonify(response)

# 학사공지
@app.route("/haksa", methods=['POST'])
def haksa():
    response = haksa_Parser()
    return jsonify(response)

# 학사일정
@app.route("/schedule", methods=['POST'])
def schedule():
    content = request.get_json()
    response = haksa_chedule_Parser(content)
    return jsonify(response)

# 강의실 검색
@app.route("/find_lecture", methods=['POST'])
def find_lecture():
    content = request.get_json()
    response = lecture_Parser(content)
    return jsonify(response)

# 편의시설 검색 (추후 제작)
@app.route("/find_building", methods=['POST'])
def find_building():
    response = " "
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
    response = search_member_Parser(content)
    return jsonify(response)

# 학과 페이지 검색 (추후 제작)
@app.route("/page", methods=['POST'])
def page():
    response = " "
    return jsonify(response)

# 버스정류장 검색
@app.route("/find_bus", methods=['POST'])
def find_bus():
    content = request.get_json()
    response = find_bus_Paser(content)
    return jsonify(response)

# 오류보고 보고서
@ app.route('/message', methods=['POST'])
def message():
    content = request.get_json()
    response = error_report_answer(content)
    return jsonify(response)

# 날씨 검색 (제작중)
@ app.route('/weather', methods=['POST'])
def weather():
    dataSend = " "
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="25000", debug=False)
    #app.run()