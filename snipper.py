from PIL import ImageGrab, Image


class Snipper:
    def __init__(self) -> None:
        pass

    def snip(self) -> Image:
        img = ImageGrab.grabclipboard()
        if isinstance(img, Image.Image):
            return img

        raise Exception
