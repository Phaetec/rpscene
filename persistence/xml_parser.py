from defusedxml.ElementTree import parse


# NOTES:
# detail tag: Beinhaltet rarity als auch informationen wie cursed oder "requires attunement"
# roll: kann mehrmals auftauchen. Beschreibt entweder DMG oder andere Effekte. Kann variablen wie SPELL enthalten.
# - Muss noch ins Modell eingearbeitet werden
# range: Reichweite, wenn vorhanden (Waffen, spells?)
# dmg1: Damage, wenn die Waffe einen Angriffswert hat
# dmg2: Zum Beispiel Zweihanddmg bei Versatile Waffen. Noch keinen anderen Nutzen gesehen
# dmgType: Damagetyp, leider nur als Abkürzung, brauchtmehr Research was gemeint ist
# property: Sowas wie 2H, Automatic? - pistolen evtl., light, versatile, etc. Meist als 1 oder 2 Buchstaben Abkürzungen
# modifier: Die ganzen +X waffen haben zB einen. Normalerweise mehrere so wie zum Beispiel auf damage und attack roll
# - Beinhaltet ein Attribute "Category" mit werten "Bonus", "Skills" oder "Ability Score"
# value: Wert des Gegenstandes in Gold
# stealth: Wenn 1, dann hat man disadvantage für stealth mit der Ausrüstung
# strength: Benötigt mindestens den Inhalt des Tags als Stärke um Getragen zu werden
# ac: Die AC, die die Ausrüstung einem gibt
def convert_type(typename):
    if typename == "LA":
        return "LIGHT_ARMOR"
    elif typename == "MA":
        return "MEDIUM_ARMOR"
    elif typename == "HA":
        return "HEAVY_ARMOR"
    elif typename == "S":
        return "Shield"
    else:
        raise TypeError("Item Type not recognized")


def is_magic(item):
    magic_attr = item.find("magic")
    if not magic_attr:
        return False
    if magic_attr.text != "1":
        return False
    return True


def parse_strength_requirement(item):
    strength_var = item.find("strength")
    if not strength_var:
        return 0
    try:
        requirement = int(strength_var.text)
        return requirement
    except TypeError:
        return 0


def create_armor(item):
    name = item.find("name").text
    type = convert_type(item.find("type").text)
    magic = is_magic(item)
    # TODO parse detail attribute
    weight = float(item.find("weight").text)
    ac = int(item.find("ac").text)
    # TODO parse text
    stealth_disadvantage = True if item.find("stealth").text == "1" else False
    strength_requirement = parse_strength_requirement(item)
    print(name, type, magic, weight, ac, stealth_disadvantage, strength_requirement)


def parse_and_store_item(item):
    type = item.find("type").text
    # Armor Types: LA, MA, HA (Light, Medium, Heavy Armor), S for Shield
    if type in ["LA", "MA", "HA", "S"]:
        create_armor(item)


def parse_entities(file_path):
    tree = parse("CorePlusUAWithModern.xml")
    root = tree.getroot()
    for child in root.findall('item'):
        parse_and_store_item(child)

        if child.findall('ac'):
            print("Type: " + str(child.findall('type')[0].text))
            print("-----")
        # for attrs in child:
        #    if attrs.tag not in ['weight', 'type', 'text', 'name', 'magic', 'detail', 'roll', 'range', 'dmg1',
        #                         'dmgType', 'property', 'dmg2', 'modifier', 'value', 'stealth', 'strength', 'ac']:
        #        print(attrs.tag)
        #        print(attrs.attrib)
        #       print('---')



parse_entities(True)
