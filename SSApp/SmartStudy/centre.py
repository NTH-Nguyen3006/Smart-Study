import json, importlib
from .info import info
from .Sundry import Json
from .Plugin import *
from .Action import sendMessage #, Menus
from .. import fbchat


def centre(data_event):
    try:
        data = json.loads(info(data_event=data_event))
        print(data)
        thread_id = data["thread_id"]
        message_id = data["message_id"]

        # gọi hàm get info xem nó trả về key và message hay attachments
        if data.get("message"):
            sender_id, message = data["message"]

            print(sender_id, message)

            cmd = message.split()[0].lower() # lấy cú pháp đầu
            # nếu cú pháp người dùng có trong kho cú pháp
            if commands.get(cmd):
                function = eval(commands[cmd]['func_name'])
                if function.__code__.co_argcount == 2: # kiểm tra số args 
                    function(thread_id, message_id)
                else:
                    _input = ' '.join(message.split()[1:])
                    function(thread_id, message_id, _input)
            else:
                ChatGPT(sender_id=sender_id, message=message, 
                        thread_id=thread_id, message_id=message_id)
        
        elif data.get("attachments"):
        # còn nếu người dùng gửi ảnh nó sẽ lấy url ảnh 
            sender_id, image_id, image_url = data["attachments"]
            print(image_url)
            accounts = Json().load(fileName='SSApp\SmartStudy\Json/accounts.json')
            accounts[sender_id] = image_url
            Json().save("SSApp\SmartStudy\Json/accounts.json", accounts)
            fbchat.Reply(text="Bạn muốn hỏi gì về bức ảnh này ?", 
                            thread_id=thread_id, message_id=message_id)

        # elif data.get("postback"):
        #     from .Sundry import run_postback
        #     run_postback(sender_id=data["postback"][0], payload=data["postback"][1])
        

    except Exception as e :
        #print(e)
        import traceback, sys
        name_error = str(sys.exc_info()[1])
        tb = sys.exc_info()[2]
        line_number = traceback.extract_tb(tb)[-1][1]
        content = f"""ĐÃ CÓ LỖI XÃY RA!!!
        Tên Lỗi: {name_error}
        
        Tên file: {__name__} | Vị trí dòng thứ: {line_number}
        """
        print(content)
        sendMessage("6312817428801561", content)
        sendMessage("6169255926506657", content)


