import telegram
import json
from setting.card import *
from setting.answer_main import answer


# 사용자 오류제보 및 건의사항 텔레그램 전송
def error_report_answer(content):
    title = content['action']['detailParams']['title']["value"]
    content = content['action']['detailParams']['content']["value"]
    title = ''.join(str(e) for e in title)
    content = ''.join(str(e) for e in content)
    send_telegram(title, content)
    text = "성공적으로 저장되었습니다. \n적극적으로 조치 하겠습니다.😀\n감사합니다.🙏"
    response = insert_text(text)
    response = answer(response)
    return response


# 텔레그램 전송
def send_telegram(title, content):
    config = json.load(open("./telegram_config.json"))
    bot = telegram.Bot(token=config["account"]["token"])
    bot.sendMessage(chat_id=config["account"]["chatID"], text="제목: " + title + "\n내용: " + content)
