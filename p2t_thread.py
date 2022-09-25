from threading import Thread
from threading import Event
import pyperclip
from p2t import P2T


event = Event()


class P2TThread:
    def __init__(self, p2t: P2T) -> None:
        self.__is_alive = True
        self.__is_pause = True
        self.__p2t = p2t
        self.thread = Thread(target=self.__run)
        self.thread.start()

    def exec(self) -> None:
        print("start exec")
        self.__is_pause = False

    def pause(self) -> None:
        print("start pause")
        self.__is_pause = True

    def exit(self) -> None:
        print("start exit")
        self.__is_pause = True
        self.__is_alive = False
        self.thread.join()

    def __run(self) -> None:
        while self.__is_alive:
            event.wait(0.5)
            event.clear()

            if self.__is_pause:
                continue

            text = self.__p2t.run()
            if text is'':
                continue

            pyperclip.copy(text)

        print("end p2t thread running")
