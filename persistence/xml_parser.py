from defusedxml.ElementTree import parse


def parse_entities(file_path):
    tree = parse("CorePlusUAWithModern.xml")
    root = tree.getroot()
    for child in root:
        if child.tag == "item":
            print(child.find('name').text)
            print(child.attrib)
            print('---')


parse_entities(True)
