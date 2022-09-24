from PIL import ImageGrab, Image
import pyperclip


class Snipper:
    def __init__(self) -> None:
        pass

    def snip(self) -> Image:
        pyperclip.waitForNewPaste()
        img = ImageGrab.grabclipboard()
        if isinstance(img, Image.Image):
            print(img.size)
            print(img.mode)
            return img

        else:
            raise Exception
