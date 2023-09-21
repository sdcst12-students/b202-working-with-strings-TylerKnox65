text = "<p class='done'>this is some text and there is a <a a;lskdjf;alksdj f;askdjf>Hyperlink</a></p>"

while text.find("<") >= 0:
    begin = text.find("<")
    end = text.find(">")
    print(begin,end)

    text = text[0:begin] + text[end+1:len(text)]
    print(text)