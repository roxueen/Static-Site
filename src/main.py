from textnode import *

def main():
    text = "This is some anchor text"
    text_type = "link"
    url = "https://www.boot.dev"
    new = TextNode(text, text_type, url)
    print(new)
    
if __name__ == "__main__":
    main()