abc = (
    ("1",1),
    ("2",2),
    ("3",3),
    ("4",4)
)

from xml.etree import ElementTree as xml
root = xml.Element("Numbers")
number = xml.Element("number")
root.append(number)


for a,b in abc:
    # for a,b in i:
    num = xml.SubElement(number,a)
    num.set("tc","10")
    num.text = str(b)
tree = xml.tostring(root, 'utf-8')
print (tree)
