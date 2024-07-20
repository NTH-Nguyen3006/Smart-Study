import requests, json
from ...Action import sendMessage, Menus, token
from ...Sundry import Json
from ....models import Q, Eng_Dictionary, VieWord

class ConnectWord_Game:
    def __init__(self) -> None:
       self.vie_connect = Json().load("SSApp\SmartStudy/config.json")["online_noitu"]["Vie"]
       self.eng_connect = Json().load("SSApp\SmartStudy/config.json")["online_noitu"]["Eng"]

    class Next:
        def __init__(self) -> None:
            self.accounts = Json().load("SSApp\SmartStudy\Json/accounts.json")
            self.conditions = Q(word__icontains=' ') | Q(word__icontains='-')

        def EngWord(self, user_id, word):
            def get_word(char, start_char=True):
                if start_char:
                    return Eng_Dictionary.objects.filter(
                        Q(word__startswith=char) & ~self.conditions 
                    ).order_by('?').first()
                
                return Eng_Dictionary.objects.filter(
                        Q(word__endswith=char) & ~self.conditions 
                    ).order_by('?').first()

            user_word = word.lower()
            bot_word = self.accounts[user_id].lower()

            if word == '':
                res_word = get_word(char="") 
                res_word = res_word and res_word.word
                
                self.accounts[user_id] = res_word or "noitu_empty"

            # xét người dùng có nhập đúng hay không
            elif (bot_word == "noitu_empty" or 
                ((len(user_word.split()) == 1) and 
                (bot_word[-1] == user_word[0]))
                ):
                res_word = get_word(char=user_word[-1]) 
                res_word = res_word and res_word.word
                self.accounts[user_id] = res_word or "noitu_empty"
            else: 
                return "bạn đã thua"
            
            Json().save(
                "SSApp\SmartStudy\Json/accounts.json", self.accounts)
            return res_word or None
        
        def VieWord(self, user_id, word):
            def Vie(word, start_char=True):
                if start_char:
                    return VieWord.objects.filter(
                        Q(word__startswith=word) 
                    ).order_by('?').first()
                
                return VieWord.objects.filter(
                        Q(word__endswith=word) 
                    ).order_by('?').first()

            user_word = word.lower().split()
            bot_word = self.accounts[user_id].lower().split()

            if word == '':
                res_word = Vie(word="") 
                res_word = res_word and res_word.word
                self.accounts[user_id] = res_word or "noitu_empty"

            # xét người dùng có nhập đúng hay không
            elif (bot_word[0] == "noitu_empty" or (
            (len(user_word) == 2) and (bot_word[1] == user_word[0]))
            ):
                res_word = Vie(word=user_word[1]) 
                res_word = res_word and res_word.word
                self.accounts[user_id] = res_word or "noitu_empty"
            else: 
                return "bạn đã thua"
            
            Json().save(
                "SSApp\SmartStudy/Json/accounts.json", self.accounts)
            return res_word or None

    #----------------------play---------------------------------
    def nextWord(self, sender_id: str, word: str|None):
        if sender_id in self.vie_connect:
            if not word:
                word = ''
            nextWord = self.Next().VieWord(sender_id, word=word)
            
        elif sender_id in self.eng_connect:
            if not word:
                word = ''
            nextWord = self.Next().EngWord(sender_id, word=word)

        else: 
            print("Errol -> sender can not connection.")

        return nextWord or ("Bot hết từ...")
    
    
    def game_rules(self, sender_id: str):
        mode_Vie = f'''
    * Nối từ tiếng Việt:
    - Nếu bạn chọn Bot đi trước thì Bot sẽ đưa ra cho bạn 1 cụm từ (cụm này chỉ có 2 từ). Bạn sẽ phải tìm những cụm từ cũng chỉ được chập nhận 2 từ. Trong cụm từ đó, từ đầu tiên phải trùng với từ cuối của Bot vừa đưa ra và ngược lại.

        '''
        mode_Vie_1 = f'''
    * Ví dụ đúng luật của trò chơi:
        "xin chào" -> "chào bạn" -> "bạn thân" -> ...
    * Ví dụ không đúng luật của trò chơi:
        +> "con gà" -> "con heo" 
        +> "xin chào" -> "chào mọi người" -> ...
        +> "thua"
    => Sẽ bị thua
        '''
        
        mode_Eng = f'''
    * Nối từ tiếng And: 
    - Chế độ này khác với nối từ tiếng Việt. Nếu bạn chọn chọn bạn đi trước thì bạn hãy đưa ra 1 từ tiếng anh bất kì KHÔNG DẤU CÁCH. Nhiệm vụ của Bot sẽ tìm ra các từ có chữ cái đầu cùng với chữ cái cuối của bạn đưa ra và ngược lại bạn cũng tiếp diễn như vậy.
    * *Ví Dụ:* 
        "character" -> "relax" -> "xanthous" -> ...
        '''

        mode_Eng_1 = f'''
    * Ví dụ đúng luật của trò chơi:
        "character" -> "relax" -> "xanthous" -> ...
    * Ví dụ không đúng luật của trò chơi:
        +> "play" -> "love"
        +> "bus" -> "smart study"
    => Sẽ bị thua
        '''
        
        if sender_id in self.vie_connect:
            sendMessage(sender_id, mode_Vie)
            sendMessage(sender_id, mode_Vie_1)
        if sender_id in self.eng_connect:
            sendMessage(sender_id, mode_Eng)
            sendMessage(sender_id, mode_Eng_1)
        sendMessage(sender_id, "Chúc bạn chơi game vui vẻ 😊")

def word_translation_button(sender_id: str, text: str):
    if not text: #nếu là rỗng
        return
    params = {"access_token": token}
    headers = {"Content-Type": "application/json"}
    data = json.dumps({
    "recipient": {"id": sender_id},
    "messaging_type": "RESPONSE",
    "message":{
        "text": text, "quick_replies":[
            {"content_type":"text", "title": "Dịch nghĩa", 
                "payload": "mean word"
            },
        ]}})
    requests.post("https://graph.facebook.com/v17.0/me/messages", 
                  params=params, headers=headers, data=data)
    return "answered"
  
def mode_connect_words(sender_id: str):
    params = {"access_token": token}
    headers = {"Content-Type": "application/json"}
    data = json.dumps({
        "recipient":{"id": sender_id},
        "message":{
            "attachment":{"type":"template",
            "payload":{
                "template_type":"button", "text": "Chế độ ngôn ngữ",
                "buttons":[
                {"type":"postback", "title": "Tiếng Anh",
                    "payload":"Eng matching"},
                {"type":"postback", "title": "Tiếng Việt",
                    "payload": "Vie matching"}
                ]}}}})
    requests.post("https://graph.facebook.com/v2.6/me/messages", params=params,headers=headers, data=data)


def connect_noitu(sender_id: str):
    from ...Action import sendMessage
    from ...Sundry import Json
    params = {"access_token": token}
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"psid": sender_id, "persistent_menu": [
        {"locale": "default", "composer_input_disabled": False, 
            "call_to_actions": [
                {"type": "postback", "title": "Nối từ tiếng Anh", 
                                    "payload": "Eng matching"},
                {"type": "postback", "title": "Nối từ tiếng Việt", 
                                    "payload": "Vie matching"},
                {"type": "postback", "title": "Kết thúc trò chơi", 
                                    "payload": "offgame"},
                {"type": "postback", "title": "Hướng dẫn chơi", 
                                    "payload": "helpplay"},
            ]}]})
    requests.post("https://graph.facebook.com/v17.0/me/custom_user_settings", 
                  params=params, headers=headers, data=data)
    
    sendMessage(sender_id, "Kết nối trò chơi thành công")
    tool = Json().load("SSApp\SmartStudy/config.json")
    tool["online_noitu"]["Vie"]+=[sender_id]
    Json().save("SSApp\SmartStudy/config.json", tool)
    
    data1 = json.dumps({
        "recipient": {"id": sender_id},
        "messaging_type": "RESPONSE",
        "message":{"text": "Bạn có thể ấn bắt đầu để bắt đầu chơi.", 
            "quick_replies":[
                {"content_type":"text", "title": "Bắt đầu", 
                    "payload": "start"},
        ]}})
    print(requests.post("https://graph.facebook.com/v17.0/me/messages", 
                    params=params, headers=headers, data=data1))

def offgame(sender_id: str):
    Menus().basic_menu(sender_id)
    
    tool = Json().load("SSApp\SmartStudy/config.json")
    if sender_id in tool["online_noitu"]["Vie"]:
        tool["online_noitu"]["Vie"].remove(sender_id)
    else:
        tool["online_noitu"]["Eng"].remove(sender_id)
    Json().save("SSApp\SmartStudy/config.json", tool)

    sendMessage(sender_id, "Bạn đã rời trò chơi nối từ thành công.")
    sendMessage(sender_id, "Cảm ơn bạn đã tham gia chơi với tôi.")

def button_object_goes_ahead(sender_id: str) -> None:
    params = {"access_token": token}
    headers = {"Content-Type": "application/json"}
    data = json.dumps({
        "recipient":{"id": sender_id},
        "message":{ "attachment": {
            "type":"template", 
            "payload":{
                "template_type":"button",
                "text": "Chọn người đi trước",
                "buttons":[
                {"type":"postback", "title": "SSBot",
                    "payload":"bot_start"},
                {"type":"postback", "title": "Tôi",
                    "payload": "user_start"}
                ]}}}})
    requests.post("https://graph.facebook.com/v2.6/me/messages", 
                    params=params,headers=headers, data=data)


def collect_text(text):
    texts_collect = Json().load("SSApp\SmartStudy/Json/textNoiTu.json")
    texts_collect.append(text)
    Json().save(fileName="Json/textNoiTu.json", data=texts_collect)

