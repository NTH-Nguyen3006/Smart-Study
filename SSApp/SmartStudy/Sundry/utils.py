import sqlite3
from json import load, dump

class Json:
    def __init__(self) -> None:
        pass

    def load(self, fileName: str) -> list | dict | None:
        try:
            with open(fileName, "r", encoding="utf8") as file:
                return load(file)
        except Exception as e:
            print(f'Open Json name is "{fileName}" Error ->', e)
            return 

    def save(self, fileName: str, data) -> None:
        try:
            with open(fileName, "w", encoding="utf8") as save:
                dump(data, save, ensure_ascii=False, indent=4)
        except Exception as e: 
            print(f'Save Json name is "{fileName}" Error ->', e)


def cutContent(text) -> list:
    if len(text) < 2000:
        return [text] 
    elif len(text) < 4000:
        answer: list = text.split() 
        return [
            ' '.join(answer[: len(answer)//2]), 
            ' '.join(answer[(len(answer)//2) :])
            ]
    else:
        answer = text.split()
        return [
            ' '.join(answer[: (len(answer)//3)]), 
            ' '.join(answer[(len(answer)//3) : (2*len(answer))//3]),
            ' '.join(answer[((2*len(answer))//3) :])
        ]