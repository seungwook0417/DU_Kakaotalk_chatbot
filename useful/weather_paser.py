# 대구대학교 날씨 서비스 제공 예정
from setting.card import *
from setting.answer_main import *
import requests
from bs4 import BeautifulSoup

def naver_weather_parser():
    try:
        url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B2%BD%EC%82%B0+%EB%82%A0%EC%94%A8&tqi=h4Q7blp0JXossg%2F2UxGssssssgN-252128"
        # 경산시 날씨 url

        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        full_text = ""

        curr_temp = soup.find('span', class_='todaytemp').get_text() + "℃"
        summary = soup.find('p', class_='cast_txt').get_text()
        min_temp = soup.find('span', class_='min').get_text()
        max_temp = soup.find('span', class_='max').get_text()
        feel_temp = soup.find('span', class_='sensible').get_text()
        dust_degree = soup.find('dl', class_='indicator').get_text().split(" ")[2].replace("㎍/㎥", "㎍/㎥ ")

        full_text += ("🔉" + summary + "\n" + "🌡" + "현재온도 " + curr_temp
                      + "\n" + "🌡" + feel_temp
                      + "\n" + "🌡" + "최저/최고온도 " + min_temp + "/" + max_temp
                      + "\n" + "😷" + "미세먼지 " + dust_degree)
        full_text = full_text.replace("˚", "℃")
        title = "[☀대구대 실시간 날씨 정보예요!!☀]"
        response = insert_card(title, full_text, image_url="https://i.esdrop.com/d/QsgT1vEadT.png")
        response = answer(response)
        return response
    except:
        pass