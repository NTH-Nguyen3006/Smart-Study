import json
from .Sundry import Json, save_user_for_upd
from .Action import seen, sendMessage, typingon
from .Plugin import Prompt_QR_Code
from mtranslate import translate
from ..models import UserID_FB

administrators = Json().load("SSApp\SmartStudy\Json\data.json")["administrators"]

def info(data_event):
    event_type = data_event["type"]
    if event_type in ["message", "message_reply"]:
        sender_id = data_event["sender_id"]
        thread_id = data_event["thread_id"]
        message_id = data_event["message_id"]
        message = data_event["body"]
        timestamp = data_event["timestamp"]

        if event_type == "message":
            if data_event['attachments']: # Photo
                print(1)
                if data_event['attachments'][0]["type"] == "photo":
                    image_url = data_event['attachments'][0]["url"]
                    image_id = data_event['attachments'][0]["id"]
                    print(image_id)
                    return json.dumps({
                        "attachments": [sender_id, image_id, image_url],
                        'message_id': message_id,
                        "thread_id": thread_id,
                        "timestamp": timestamp
                    })
                    
                elif data_event['attachments'][0]["type"] == "sticker":
                    sticker_id = data_event['attachments']["id"]
                    return json.dumps({
                        "attachments": [sender_id, sticker_id],
                        'message_id': message_id,
                        "thread_id": thread_id,
                        "timestamp": timestamp
                    })

                elif data_event['attachments'][0]["type"] == "video":
                    return json.dumps({})
                
            return json.dumps({
                "message": [sender_id, message],
                'message_id': message_id,
                "thread_id": thread_id,
                "timestamp": timestamp
            })
            

        elif event_type == "message_reply":
            message_reply = data_event['message_reply']

            mid_reply = message_reply["message_id"]
            timestamp_mes_reply = message_reply["timestamp"]

            if message_reply['attachments']:
                if message_reply['attachments']["type"] == "photo":
                    image_url = message_reply['attachments'][0]["url"]
                    image_id = message_reply['attachments'][0]["id"]
                    return json.dumps({
                        "message": [sender_id, message],
                        "reply": {'mid_repl': mid_reply, 
                                  "attachments": [image_id, image_url]},
                        'message_id': message_id,
                        "thread_id": thread_id,
                        "timestamp": timestamp
                    })
                
                elif message_reply['attachments']["type"] == "sticker":
                    sticker_id = message_reply['attachments']["id"]
                    return json.dumps({
                        "message": [sender_id, message],
                        "reply": {'mid_repl': mid_reply, 
                                  "attachments": [sticker_id]},
                        'message_id': message_id,
                        "thread_id": thread_id,
                        "timestamp": timestamp
                    })

            else: # reply tin dạng text
                text_reply = message_reply["body"]
                return json.dumps({
                    "message": [sender_id, message],
                    'message_id': message_id,
                    "thread_id": thread_id,
                    "reply": {'mid_repl': mid_reply, 
                                "message": [text_reply]},
                    "timestamp": timestamp
                })

        else:
            pass
