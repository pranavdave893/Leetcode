from xml.etree import ElementTree as xml
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = xml.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

root = xml.Element("Users")
userelement = xml.Element("user")
root.append(userelement)
uid = xml.SubElement(userelement, "uid")
uid.text = "1"
FirstName = xml.SubElement(userelement, "FirstName")
FirstName.text = "testuser"
LastName = xml.SubElement(userelement, "LastName")
LastName.text = "testuser"
Email = xml.SubElement(userelement, "Email")
Email.text = "testuser@test.com"
state = xml.SubElement(userelement, "state")
state.text = "xyz"
location = xml.SubElement(userelement, "location")
location.text = "abc"

# xml_str = xml.tostring(root).decode()
tree = xml.tostring(root, 'utf-8')
print (tree)
# xml_str = (prettify(root))
# with open("text.xml","w") as fh:
#     fh.write(xml_str)