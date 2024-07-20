import requests, json
from ..Sundry import Json
# from ...models import UserID_FB

token = Json().load("SSApp\SmartStudy\Json\data.json")['Token']

params = {"access_token": token}
headers = {"Content-Type": "application/json"}

class Menus:
    def __init__(self) -> None:
        self.API_URL = "https://graph.facebook.com/v17.0/me/custom_user_settings"

    def admin_menu(self, sender_id):
        data = json.dumps({"psid": sender_id, "persistent_menu": [
            {"locale": "default","composer_input_disabled": False,
            "call_to_actions": [
                {"type": "postback", "title": "Button quyền lực", 
                    "payload": "button admin"},
                {"type": "postback", "title": "Danh sách chức năng", 
                    "payload": "/list"},
                {"type": "postback", "title": "Truy cập Website", 
                    "payload": "get URL website"}
            ]}]})
        requests.post(self.API_URL, params=params, headers=headers, data=data)
    

    def basic_menu(self, sender_id):
        data = json.dumps({"psid": sender_id, "persistent_menu": [
            {"locale": "default","composer_input_disabled": False,
            "call_to_actions": [
                {"type": "postback", "title": "Danh sách chức năng", 
                    "payload": "/list"},
                {"type": "postback", "title": "Truy cập Website", 
                    "payload": "get URL website"}
            ]}]})
        requests.post(self.API_URL, params=params, headers=headers, data=data)

    
#for Admin
# setMenu: list[str] = []
# for _id in setMenu:
#     Menus().basic_menu(_id)

#Menus().setAdmStudent("6312817428801561")