from enum import Enum


class Bender(Enum):
    AIR_BENDER = "air"
    WATER_BENDER = "water"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"

class TextNode:

    def __init__(self, text: str, text_type, url: str):        
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: "TextNode"):
        if self.text != value.text:
            return False
        if self.text_type != value.text_type:
            return False
        if self.url != value.url:
            return False
        
        return True
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
