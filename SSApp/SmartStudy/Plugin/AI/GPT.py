import requests 
from ...Sundry import Json, cutContent

config = Json().load("SSApp\SmartStudy\Json\data.json")

def GPT(sender_id, message) -> list | None:
    try:
        account = Json().load("SSApp/SmartStudy/Json/accounts.json") or {}
        
        len_sender_text = len(account[sender_id]) < 2000
        text = account[sender_id] if len_sender_text else ""
    
        url = "https://api.openai.com/v1/chat/completions"
        header = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {config["Token_OpenAI"]}'
        }
        
        data = {
            "model": "gpt-3.5-turbo-1106",
            "messages": [{
                    "role": "system",
                    "content": "Tên tôi là SmartStudy. Bạn có thể gọi tôi là AI hoặc Chat-Bot. Tôi được tạo ra bởi Duy Khang, Hoàng Nguyên, Minh Tuấn. Tôi được tạo ra nhằm mục đích giúp mọi người học tập và giải đáp các thắc mắc."
                },
                {"role": "assistant", "content": f'{text}'},
                {"role": "user", "content": f'{message}'}
            ]
        }
    
        response = requests.post(url=url, headers=header, json=data).json()
        GPT_answer = response['choices'][0]['message']['content']

        return cutContent(GPT_answer)


    except Exception as e:   
        import traceback, sys
        name_error = str(sys.exc_info()[1])
        tb = sys.exc_info()[2]
        line_number = traceback.extract_tb(tb)[-1][1]
        
        print(f"""ĐÃ CÓ LỖI XÃY RA!!!
        Tên Lỗi: {name_error} -> limited request
        Tên file: {__name__}
        """)
        return



