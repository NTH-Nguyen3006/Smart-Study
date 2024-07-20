from ...Sundry import cutContent
from mtranslate import translate
from ....models import Eng_Dictionary

def Mean(word: str):
    try: 
        data = Eng_Dictionary.objects.get(word=word)
        if data:
            return data
        else:
            return
    except Exception as e:
        print(f'file "{__name__}" with error name is -> {e}')


def content(word) -> list:
    result = []
    data = Mean(word=word)
    word = data.word
    mean = f'*{word.capitalize()}*\\n{data.mean}'
    mean:list = cutContent(mean)
    for content in mean:
        result += [content.replace('\\n', '\n')]
    return result
    

def Mean_(word):
    try: 
        DB = DataBase(DataBaseName="DataBase/Words.db")

        if len(word.split()) >= 2:
            firstWord = word.split()[0]
            secondWord = word.split()[1]
            command = f"""
                SELECT * FROM vocabulary 
                WHERE word LIKE '{firstWord}%' AND word LIKE '%{secondWord}%'
            """

        else: 
            command = f"SELECT * FROM vocabulary WHERE word='{word}'"
            
        data = DB.select(command=command)
        if data: # nếu có kết quả
            return {
                "word": data[0],
                "meaning": data[1]
            }
        
        return translate(word, to_language='vi')
    
    except Exception as e:
        print(f'file "{__name__}" with error name is -> {e}')