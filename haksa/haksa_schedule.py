import json
import requests

from setting.card import *
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36",
    "Accept-Language": "ko",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
}

# 학사 일정 일별, 월별, 이번달 구분
def haksa_chedule_Parser(content):
    content = content['action']['detailParams']
    # 사용자가 날짜 입력시
    if 'date' in content.keys():
        content = content['date']['value']
        content = json.loads(content)
        content = content['date']
        date = ''.join(str(e) for e in content)
        description = schedule_Parser(date)
    # 사용자가 월별로 입력시
    elif 'month' in content.keys():
        content = content['month']['value']
        content = json.loads(content)
        content = content['from']['date']
        date = ''.join(str(e) for e in content)
        month = date.replace("-", "")
        month = month[0:6]
        description = schedule_month_Parser(month)
    # 그외
    else:
        month = ""
        description = schedule_month_Parser(month)

    title = date + " 학사일정 안내"
    response = insert_card(title, description)
    response = insert_button_url(response,"전체 일정","https://daegu.ac.kr/schedule/detail?schedule_info_seq=1")
    return response

# 학사일정 일별 파싱
def schedule_Parser(date):
    try:
        url = 'https://daegu.ac.kr/main/schedule/data'
        response = requests.post(url=url, headers=headers, data={
            'schedule_start_date': date
        })
        schedule = response.json()
        data = []
        if schedule != []:
            for a in schedule:
                data.append(
                    "날짜 : " + a['schedule_start_date'] + "~" + a['schedule_end_date'] + "\n일정 : " + a[
                        'schedule_title'] + "\n")
            description = '\n'.join(str(e) for e in data)
        else:
            description = "검색된 일정이 없습니다."
        return description
    except:
        pass

# 학사일정 월별로 파싱
def schedule_month_Parser(month):
    try:
        url = 'https://portal.daegu.ac.kr/du/CollegeSchedule.do?yyyymm='+month
        response = requests.get(url=url)
        schedule = response.json()
        data = []
        for a in schedule['collegeScheduleList']:
            data.append(
                "날짜 : " + a['schedule_start_date'] + "~" + a['schedule_end_date'] + "\n일정 : " + a['schedule_title'] + "\n")
        description = '\n'.join(str(e) for e in data)
        return description
    except:
        pass