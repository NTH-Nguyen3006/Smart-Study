from .utils import Json
from ..Admin.block_user_on_update import *
from ..Action import *
from ..Plugin import *

config = Json().load("SSApp\SmartStudy\Json\data.json")
administrators = config["administrators"]


def run_postback(sender_id, payload):
  try:
    if payload in ["search", "conversion", "other"]:
        List(sender_id, payload)
    elif payload == "/list":
        List(sender_id)
    elif payload == 'get URL website':
       get_URL_website(sender_id=sender_id)
  
#------------------------------------------------------------------ play Connect Word
    elif payload == "Eng matching":
        tools = Json().load("SSApp\SmartStudy/config.json") or {}
        if sender_id not in tools["online_noitu"]["Eng"]:
            tools["online_noitu"]["Eng"] += [sender_id]
        if sender_id in tools["online_noitu"]["Vie"]:
            tools["online_noitu"]["Vie"].remove(sender_id)
        Json().save("SSApp\SmartStudy/config.json", tools)
        button_object_goes_ahead(sender_id)
    elif payload == "Vie matching":
        tools = Json().load("SSApp\SmartStudy/config.json") or {}
        if sender_id not in tools["online_noitu"]["Vie"]:
            tools["online_noitu"]["Vie"] += [sender_id]
        if sender_id in tools["online_noitu"]["Eng"]:
            tools["online_noitu"]["Eng"].remove(sender_id)
        Json().save("SSApp\SmartStudy/config.json", tools)
        button_object_goes_ahead(sender_id)
    elif payload == "helpplay":
        ConnectWord_Game().game_rules(sender_id)
    elif payload == "start":
        data = Json().load("SSApp/SmartStudy/Json/accounts.json") or {}
        data[sender_id] = "noitu_empty"
        Json().save("SSApp/SmartStudy/Json/accounts.json", data)
        mode_connect_words(sender_id)
    elif payload == "bot_start":
        ConnectWord(sender_id, word=None)
    elif payload == "user_start":
      data = Json().load("SSApp/SmartStudy/Json/accounts.json") or {}
      data[sender_id] = "noitu_empty"
      Json().save("SSApp/SmartStudy/Json/accounts.json", data)
      sendMessage(sender_id, "Mời bạn đi trước")
    elif payload == "mean word":
        word = Json().load("SSApp/SmartStudy/Json/accounts.json")[sender_id]
        vocabulary(sender_id, word)
    elif payload == "offgame":
      sendMessage(sender_id, "Đang xử lý...")
      offgame(sender_id)
      
#------------------------------------------------------------------ Create_QR
    elif payload.split()[0] == "QR_Clear":
      qr_clear(sender_id, " ".join(payload.split()[1:]))
    elif payload.split()[0] == "AI_Art_QR":
      AI_art_QR(sender_id, " ".join(payload.split()[1:]))
    elif payload.split()[0] == "Prompt_QR":
        accounts = Json().load("SSApp/SmartStudy/Json/accounts.json") or {}
        tools = Json().load("SSApp/SmartStudy/config.json")
        accounts[sender_id] = f"Prompt_to_AI_ART_QR {' '.join(payload.split()[1:])}"
        tools["Creating_QR"] += [sender_id]
        Json().save("SSApp/SmartStudy/config.json", tools)
        Json().save("SSApp/SmartStudy/Json/accounts.json", accounts)
        sendMessage(sender_id, 'Bạn nhập chủ đề bất kì cần vẽ QR Code. Bạn có thể gửi "not" để tôi tự tạo chủ đề.')
  
#--------------------------------------------------------------------- Admin
    elif sender_id in administrators:
        if payload[:6] == "accept":
            pass
        
        elif payload[:6] == "refuse":
            pass
        
        elif payload == "button admin":
            Buttons().btn_for_admin(sender_id)
        elif payload == "on update bot":
            on_block_user_on_update(sender_id)
        elif payload == "off update bot":
            off_block_user_on_update(sender_id)


  except Exception as e:
    import traceback, sys
    name_error = str(sys.exc_info()[1])
    tb = sys.exc_info()[2]
    line_number = traceback.extract_tb(tb)[-1][1]
    
    print(f"""ĐÃ CÓ LỖI XÃY RA!!!
    
    Tên Lỗi: {name_error}
    
    Tên file: {__name__} | Vị trí dòng thứ: {line_number}
    """)