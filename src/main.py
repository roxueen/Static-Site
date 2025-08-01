from textnode import TextNode, TextType

def main():
    new = TextNode("This is some anchor text", text_type.LINK, "https://www.boot.dev")
    print(new)
    
if __name__ == "__main__":
    main()