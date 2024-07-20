from .GPT import GPT
from .Gemini import get_answerImage, get_answerText
from .ConnectWord import ConnectWord_Game, connect_noitu, offgame, mode_connect_words, button_object_goes_ahead
# from ...Action import sendMessage
from .... import fbchat
from ...Sundry import Json

def GeminiAI(sender_id, message, thread_id, message_id, reply_message=None) -> None:
    try:
        accounts = Json().load("SSApp\SmartStudy\Json/accounts.json") or {}

        if sender_id in accounts:
            if "https://scontent.xx.fbcdn.net/" in accounts[sender_id]: 
                listContent = get_answerImage(message, accounts[sender_id])

            elif reply_message:
                if "https://scontent.xx.fbcdn.net/" in reply_message:
                    listContent = get_answerImage(message, reply_message[13:])
                else: # xử lý văn bản khi có sự kiện bắt 1 text
                    listContent = get_answerText(message)
            else:
                listContent = get_answerText(message) 

        else:
            if "https://scontent.xx.fbcdn.net/" in message:
                accounts[sender_id] = message
                Json().save(fileName="Json/accounts.json", data=accounts)

                # sendMessage(sender_id, "bạn muốn tôi giúp gì về bức ảnh này ?")
                # fbchat.Reply(te)
                return
            else:
                listContent = get_answerText(message)
        
        if not listContent:
            ChatGPT(sender_id=sender_id, message=message)

        accounts[sender_id] = " ".join(listContent)
        
        if 0 < len(listContent) < 2:
            # sendMessage(sender_id, listContent[0])
            fbchat.Reply(text=listContent[0], thread_id=thread_id, message_id=message_id)
        else:
            # sendMessage(sender_id, listContent[0])
            # sendMessage(sender_id, listContent[1])
            fbchat.Reply(text=listContent[0], thread_id=thread_id, message_id=message_id)
            fbchat.Reply(text=listContent[1], thread_id=thread_id, message_id=message_id)

        Json().save("SSApp\SmartStudy\Json/accounts.json", accounts)
    
    except Exception as e: 
        from Admin.block_user_on_update import on_block_user_on_update
        #sendMessage("6312817428801561", f'Có lỗi ở file tên "{__name__}", tên lỗi là {e}')
        #sendMessage("6169255926506657", f'Có lỗi ở file tên "{__name__}", tên lỗi là {e}')
        #on_block_user_on_update("6312817428801561")
        import traceback, sys
        name_error = str(sys.exc_info()[1])
        tb = sys.exc_info()[2]
        line_number = traceback.extract_tb(tb)[-1][1]
        
        print(f"""ĐÃ CÓ LỖI XÃY RA!!!
        
        Tên Lỗi: {name_error}
        
        Tên file: {__name__} | Vị trí dòng thứ: {line_number}
        """)


def ChatGPT(sender_id, message, thread_id, message_id) -> None:
    accounts = Json().load("SSApp\SmartStudy\Json/accounts.json") or {}
    if sender_id in accounts:
        if "https://scontent.xx.fbcdn.net/" in accounts[sender_id]:
            GeminiAI(sender_id, message, thread_id, message_id)
            return
    
    GPT_answer: list|None = GPT(sender_id, message)
    if GPT_answer:
        accounts[sender_id] = ' '.join(GPT_answer)

        for content in GPT_answer:
            # sendMessage(sender_id, content)
            fbchat.Reply(text=content, thread_id=thread_id, message_id=message_id)

        Json().save("SSApp\SmartStudy\Json/accounts.json", accounts)
    else:
        GeminiAI(sender_id, message, thread_id, message_id)
        return


def ConnectWord(sender_id, word, thread_id, message_id, prompt=None):
    connection = ConnectWord_Game()
    
    """ if prompt.lower() == 'bot start first':
        word = None """
        
    nextWord: str = connection.nextWord(sender_id=sender_id, word=word)#[0]
    # sendMessage(sender_id, nextWord)
    fbchat.Reply(text=nextWord, thread_id=thread_id, message_id=message_id)


    if nextWord == "bạn đã thua":
        accounts = Json().load("SSApp\SmartStudy\Json/accounts.json")
        accounts[sender_id] = "noitu_empty"
        Json().save("SSApp\SmartStudy\Json/accounts.json", data=accounts)
        ConnectWord(sender_id=sender_id, word=None)
        





            