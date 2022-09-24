from threading import Thread
from threading import Event
import pyperclip
from p2t import P2T


event = Event()


class P2TThread:
    def __init__(self, p2t: P2T) -> None:
        self.__is_pause = True
        self.__is_alive = True
        self.__p2t = p2t
        self.thread = Thread(target=self.__run)
        self.thread.start()

    def start(self) -> None:
        print("thread start")
        event.set()
        self.__is_pause = False

    def pause(self) -> None:
        print("thread pause")
        self.__is_pause = True
        # need set because __run wait blocking not work
        event.set()
        self.__clear_clipboard()

    def exit(self) -> None:
        print("thread exit")
        self.__is_alive = False
        self.pause()
        self.thread.join()

    def __run(self) -> None:
        while self.__is_alive:
            # stay here until start called
            event.wait()
            event.clear()

            # start called, repeat capturing until stop called
            while True:
                if self.__is_pause is True:
                    break

                # stay here until clipboard copy occured
                pyperclip.waitForNewPaste()
                text = self.__p2t.run()
                pyperclip.copy(text)

        print("end p2t thread running")

    def __clear_clipboard(self) -> None:
        pyperclip.copy("")
