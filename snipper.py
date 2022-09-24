from PIL import ImageGrab, Image
import pyperclip


class Snipper:
    def __init__(self) -> None:
        pass

    def wait_for_snip(self) -> Image:
        print("Wait for snipping...")

        pyperclip.waitForNewPaste()
        print("copied!")
        img = ImageGrab.grabclipboard()
        if isinstance(img, Image.Image):
            return img

        raise Exception

    def clear(self) -> None:
        pyperclip.copy("")
