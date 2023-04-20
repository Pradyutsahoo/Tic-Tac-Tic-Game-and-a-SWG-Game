from cgitb import text


with open('file.txt', 'r')as f:
    text= f.read()
    
text = text.replace('mad' , '###')

with open('file.txt', 'r')as f:
    text= f.read()
