import requests, json
from ..Sundry import Json

token = Json().load("SSApp\SmartStudy\Json\data.json")['Token']

params = {"access_token": token}
headers = {"Content-Type": "application/json"}

class Buttons:
    def __init__(self) -> None:
        self.API_URL = "https://graph.facebook.com/v2.6/me/messages"

    def btn_for_admin(self, sender_id):
        data = json.dumps({
            "recipient":{"id": sender_id},
            "message":{"attachment":{"type":"template", 
            "payload":{
                "template_type": "button", 
                "text": "Bật/tắt Bot trong việc bảo trì Bot", 
                "buttons":[
                    {"type":"postback", "title":"Bật chế độ update Bot", 
                        "payload": "on update bot"},
                    {"type":"postback", "title":"Tắt chế độ update Bot", 
                        "payload": "off update bot"},
            ]}}}})
        requests.post(self.API_URL, params=params, headers=headers, data=data)
        
        data = json.dumps({
            "recipient":{"id": sender_id},
            "message":{"attachment":{"type":"template", 
                "payload":{
                    "template_type": "button", 
                    "text": "Chế độ dưới quyền Admin", 
                    "buttons":[
                        {"type":"postback", "title":"Chế độ Giáo Viên",
                            "payload": "admin teacher"},
                        {"type":"postback", "title":"Chế độ Học Sinh", 
                            "payload": "admin student"},
                ]}}}})
        requests.post(self.API_URL, params=params, headers=headers, data=data)

    
