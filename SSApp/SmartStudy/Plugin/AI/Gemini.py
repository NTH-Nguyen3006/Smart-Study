import requests
import google.generativeai as geminiAI
from PIL import Image
from io import BytesIO
from ...Sundry import cutContent, Json

data = Json().load("SSApp\SmartStudy\Json\data.json")

def get_answerText(question: str, total_key=0) -> list:
    if total_key == 4:
        return
    
    geminiAI.configure(api_key=data["Token_GenAI"][total_key])
    try:
        model = geminiAI.GenerativeModel(model_name="gemini-pro")
        response = model.generate_content(question)

        return cutContent(response.text)
    
    except Exception as e:
        get_answerText(question=question, total_key=total_key+1)
        import traceback, sys, Action
        name_error = str(sys.exc_info()[1])
        tb = sys.exc_info()[2]
        line_number = traceback.extract_tb(tb)[-1][1]
        content = f"""ĐÃ CÓ LỖI XÃY RA!!!
        Tên Lỗi: {name_error}
        Tên file: {__name__} | Vị trí dòng thứ: {line_number}
        """
        print(content)
        Action.sendMessage("6312817428801561", content)


def get_answerImage(question:str, urlImage:str) -> list:
    try:
        resp = requests.get(urlImage)
        if resp.status_code == 200:
            image = Image.open(BytesIO(resp.content))
        else:
            print("request image 404, Gemini can't read image.")
            return
        model = geminiAI.GenerativeModel(model_name="gemini-pro-vision")
        response = model.generate_content([question, image])

        return cutContent(response.text)

    except Exception as e:
        import traceback, sys, Action
        name_error = str(sys.exc_info()[1])
        tb = sys.exc_info()[2]
        line_number = traceback.extract_tb(tb)[-1][1]
        content = f"""ĐÃ CÓ LỖI XÃY RA!!!
        
        Tên Lỗi: {name_error}
        
        Tên file: {__name__} | Vị trí dòng thứ: {line_number}
        """
        print(content)
        Action.sendMessage("6312817428801561", content)
        return ["Có vẻ có sự cố bên Bot. Mong bạn báo đến cho Admin"]
