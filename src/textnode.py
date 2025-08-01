from enum import Enum

class TextType(Enum):
    PLAIN = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        # dacă text_type e deja Enum, îl păstrăm
        # dacă e string (ex. "bold"), îl convertim la Enum
        self.text_type = text_type if isinstance(text_type, TextType) else TextType(text_type)
        self.text = text
        self.url = url if self.text_type in [TextType.LINK, TextType.IMAGE] else None

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text!r}, {self.text_type.value!r}, {self.url!r})"
    