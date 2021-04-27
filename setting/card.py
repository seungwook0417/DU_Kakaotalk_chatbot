from copy import deepcopy

# 카카오톡 답변 양식 입니다.
# 기본 답변
base_response = {'version': '2.0', 'template': {'outputs': [], 'quickReplies': []}}


# 카카오톡 채널 - 텍스트 응답
def insert_text(text):
    new_response = deepcopy(base_response)
    new_response['template']['outputs'] = [{"simpleText": {"text": text}}]
    return new_response


# 카카오톡 채널 - 이미지 응답
def insert_image(image_url, alt_text):
    new_response = deepcopy(base_response)
    new_response['template']['outputs'] = [{"simpleImage": {"imageUrl": image_url, "altText": alt_text}}]
    return new_response


# 카카오톡 채널 - 카드 응답
def insert_card(title, description, image_url=None, width=None, height=None):
    new_response = deepcopy(base_response)
    if image_url is not None:
        if width is not None and height is not None:
            new_response['template']['outputs'] = [{'basicCard': {
                'title': title,
                'description': description,
                'thumbnail': {"imageUrl": image_url, 'fixedRatio': True, 'width': width, 'height': height},
                'buttons': []
            }}]
        else:
            new_response['template']['outputs'] = [{'basicCard': {
                'title': title,
                'description': description,
                'thumbnail': {"imageUrl": image_url},
                'buttons': []
            }}]
    else:
        new_response['template']['outputs'] = [{'basicCard': {
            'title': title,
            'description': description,
            'buttons': []
        }}]
    return new_response


# 카카오톡 채널 - 카드 url 버튼 추가
def insert_button_url(new_response, label, web_url):
    new_response['template']['outputs'][0]['basicCard']['buttons'].append({
        "action": "webLink",
        "label": label,
        "webLinkUrl": web_url
    })
    return new_response

# 카카오톡 채널 - 카드 message 버튼 추가
def insert_button_text(new_response, label, text):
    new_response['template']['outputs'][0]['basicCard']['buttons'].append({
        "action": "message",
        "label": label,
        "messageText": text
    })
    return new_response


# 카카오톡 채널 - 하단 버튼 추가
def insert_replies(new_response, reply):
    new_response['template']['quickReplies'].append(reply)
    return new_response


# 카카오톡 채널 - 하단 버튼 생성
def make_reply(label, message):
    return {'action': 'message', 'label': label, 'messageText': message}

# 카카오톡 채널 - 리스트 응답
def insert_list(title):
    new_response = deepcopy(base_response)
    new_response['template']['outputs'] = [{'listCard': {
        'header': {"title": title },
        'items': [],
        'buttons':[]
    }}]
    return new_response

# 카카오톡 채널 - 리스트 아이템 추가
def insert_list_item(new_response, title, description, imageUrl, web_url):
    new_response['template']['outputs'][0]['listCard']['items'].append({
        "title": title,
        "description": description,
        "imageUrl": imageUrl,
        "link": {"web": web_url}
    })
    return new_response

# 카카오톡 채널 - 리스트 버튼 추가
def insert_list_button(new_response, label, web_url):
    new_response['template']['outputs'][0]['listCard']['buttons'].append({
        "action": "webLink",
        "label": label,
        "webLinkUrl": web_url
    })
    return new_response