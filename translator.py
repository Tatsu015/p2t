from PIL import Image
import pyocr

class Translator:
    def __init__(self) -> None:
        tools = pyocr.get_available_tools()
        tool = tools[0]
        self.tool = tool

    def translate(self, image:Image, lang:str = 'jpn', layout:int = 3)->str:
        builder = pyocr.builders.TextBuilder(tesseract_layout=layout)
        plane_jpn = self.tool.image_to_string(image,lang=lang,builder=builder)
        jpn = plane_jpn.strip()
        return jpn
