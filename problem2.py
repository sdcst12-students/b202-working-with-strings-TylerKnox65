"""
##### Problem 2
Retrieve the contents of the sd.deltasd.bc.ca webpage.
Remove all of the HTML and display just the real contents of the page.
"""
import requests
x = requests.get("https://sd.deltasd.bc.ca")
#print(x.text)
html = x.text
#print(html)

html = html.split("\n")
#print(type(html))
print(len(html))
for i in html:
    #print(i)
    if "<body" in i:
        #print(i)
        #print(html.index(i))
        bodyIndex = html.index(i)
    elif "</body>" in i:
        #print(html.index(i))
        #print(i)
        bodyIndex2 = html.index(i)
num = 0
for i in html:
    if html.index(i) < (bodyIndex-num) or html.index(i) > (bodyIndex2 - num):
        html.pop(html.index(i))
        num += 1
print(len(html))
for i in html:
    if "<p" in i or "</p" in i or "<br" in i:
        if "=" not in i or "-" not in i or "'" not in i or "\t" not in i:
            #print(i)
            pass
        else:
            html.pop(html.index(i)) 
    else:    
        html.pop(html.index(i))
#print(html)
html = "".join(html)
html = str(html)

for i in list(html):
    while html.find("<") >= 0:
        begin = html.find("<")
        end = html.find(">")
        html = html[0:begin] + html[end+1:len(html)]
    while html.find("(") >= 0:
        begin = html.find("(")
        end = html.find(")")
        html = html[0:begin] + html[end+1:len(html)]
    while html.find("{") >= 0:
        begin = html.find("{")
        end = html.find("}")
        html = html[0:begin] + html[end+1:len(html)]
print
html = [x for x in html]
html = list(html)
print(len(html))
for i in html:
    if i == "":
        html.pop(html.index(i))
html = "".join(html)
print(html)
n = 0
'''
for i in html:
    #print()
    if i == " ":
        html.pop(html.index(i))
    if i == "." or i == ";" or i == "!":
        html.insert(html.index(i), "\n")
    n+=1
html = " ".join(html)
print(html)
'''
    
    

