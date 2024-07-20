from .Morse import Morse_toText, Text_toMorse, allMorse
from .Roman import Num_toRoman, Roman_toNum
from .Binary import binary_toNumber, binary_toText, toBinary
from .QR_Code import qr_clear, AI_art_QR, Prompt_QR_Code
# from ...Action import sendMessage
from .... import fbchat

def textToMorse(thread_id, mid, text, send_to_id=None):
    strMorse = Text_toMorse(textInput=text)
    # sendMessage(send_to_id, strMorse)
    fbchat.Reply(text=strMorse, thread_id=thread_id, message_id=mid)

def numToRoman(thread_id, mid, number, send_to_id=None):
    roman = Num_toRoman(str(number))
    if roman:
        # sendMessage(
        #     send_to_id, 
        #     f'Đây là số la mã của số {number}\n → {roman}')
        fbchat.Reply(text=f'Đây là số la mã của số {number}\n → {roman}', 
                     thread_id=thread_id, message_id=mid)
    else:
        # sendMessage(send_to_id, )
        fbchat.Reply(text='Có vẻ bạn nhập sai không phải là 1 số. Xin hãy nhập lại', 
                     thread_id=thread_id, message_id=mid)
    
def ToNum(thread_id, mid, _input, send_to_id=None):
    if _input[0].isdigit():
        number = binary_toNumber(binary=str(_input))
        if number:
            # sendMessage(send_to_id, )
            fbchat.Reply(text=f'Chuyển đổi thành công! \n→{number}', 
                     thread_id=thread_id, message_id=mid)
        else: 
            fbchat.Reply(text="Có vẻ dữ liệu bạn nhập vào xảy ra lỗi, hãy nhập lại nào.", 
                     thread_id=thread_id, message_id=mid)
    else:
        number = Roman_toNum(roman=_input)
        if number:
            # sendMessage(send_to_id, )
            fbchat.Reply(text=f'Đây là số của số la mã {_input}\n → {number} ', 
                     thread_id=thread_id, message_id=mid)
        else:
            # sendMessage(send_to_id, )
            fbchat.Reply(text='Có vẻ bạn nhập sai 1 kí tự không phải là số la mã.', 
                     thread_id=thread_id, message_id=mid)
        
def ToText(thread_id, mid, _input, send_to_id=None):
    if _input[0].isdigit():
        text = binary_toText(binary=str(_input))
    else:
        text = Morse_toText(morseInput=_input)
        if not text:

            fbchat.Reply(text='Có 1 kí tự nào đó không có trong bảng mã Morse', 
                     thread_id=thread_id, message_id=mid)
            return
    fbchat.Reply(text=text, thread_id=thread_id, message_id=mid)

def ToBinary(thread_id, mid, _input, send_to_id=None):
    if _input.isdigit():
        binary = toBinary(dataInput=_input)

        fbchat.Reply(text=f'Đây là mã nhị phân của số {_input}\n → {binary}', 
                     thread_id=thread_id, message_id=mid)
    else:
        binary = toBinary(dataInput=_input)
        fbchat.Reply(text=f'Đây là mã nhị phân của "{_input}"\n → {binary}', 
                     thread_id=thread_id, message_id=mid)

def QR_Code(sender_id, text):
    import json, requests
    with open("SSApp\SmartStudy\Json\data.json") as file:
        Token = json.load(file)["Token"]
    def connect_create_QR(sender_id, message_text):
        params = {"access_token": Token}
        headers = {"Content-Type": "application/json"}
        data = json.dumps({
            "recipient":{"id": sender_id},
            "message":{"attachment":{"type":"template", "payload":
            {"template_type":"button", "text": "Chọn kiểu QR", "buttons":[
                {"type":"postback", "title":"QR truyền thống", 
                    "payload": f"QR_Clear {message_text}"},
                {"type":"postback", "title":"AI tự vẽ QR", 
                    "payload": f"AI_Art_QR {message_text}"},
                {"type":"postback", "title":"Tạo chủ đề QR", 
                    "payload": f"Prompt_QR {message_text}"}
            ]}}}})
        requests.post("https://graph.facebook.com/v2.6/me/messages", 
                    params=params, headers=headers, data=data)

    connect_create_QR(sender_id, text)
    



