import requests, json
from ..Sundry import Json

token = Json().load("SSApp\SmartStudy\Json\data.json")['Token']

url = "https://graph.facebook.com/v3.0/me/messages"
params = {"access_token": token}
headers = {"Content-Type": "application/json"}

def seen(send_to_id):
  data = json.dumps({
    "recipient": {"id": send_to_id},
    "sender_action": "mark_seen"
  })
  requests.post(url, params=params, headers=headers, data=data).json()

def sendMedia(send_to_id, type_img, urlImage):
  typingon(send_to_id=send_to_id)
  
  data = json.dumps({
    "recipient": {"id": send_to_id},
    "message": {
      "attachment": {
        "type": type_img,
        "payload": {
          "is_reusable": True,
          "url": urlImage
        }}}})
  requests.post(url, params=params, headers=headers, data=data)
  typingoff(send_to_id=send_to_id)

def sendMessage(send_to_id, message_text):
  seen(send_to_id)
  data = json.dumps({
    "recipient": {"id": send_to_id},
    "message": {"text": message_text}
  })
  requests.post(url, params=params, headers=headers, data=data).json()  #["message_id"]
  
  typingoff(send_to_id)

def typingoff(send_to_id):
  data = json.dumps({
    "recipient": {"id": send_to_id},
    "sender_action": "typing_off"
  })
  requests.post(url, params=params, headers=headers, data=data)

def typingon(send_to_id):
  data = json.dumps({
    "recipient": {"id": send_to_id},
    "sender_action": "typing_on"
  })

  requests.post(url, params=params, headers=headers, data=data)
