from snipper import Snipper
from translator import Translator


class P2T:
    def __init__(self, snipper: Snipper, translator: Translator) -> None:
        self.__snipper = snipper
        self.__translator = translator

    def run(self) -> str:
        try:
            img = self.__snipper.snip()
        except:
            return ""

        text = self.__translator.translate(img)
        print("--- capture ---")
        print(text)
        return text
