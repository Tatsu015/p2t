from select import select
from snipper import Snipper
from translator import Translator
import pyperclip
import threading


class P2T:
    def __init__(self, snipper: Snipper, translator: Translator) -> None:
        self.snipper = snipper
        self.translator = translator

    def __del__(self):
        self.stop()

    def start(self) -> None:
        thread = threading.Thread(target=self.__run)
        thread.start()

    def stop(self) -> None:
        pyperclip.copy("")

    def __run(self) -> None:
        try:
            self.snipper.clear()
            img = self.snipper.wait_for_snip()
        except:
            print("exit waiting")
            return

        text = self.translator.translate(img)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(text)
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
