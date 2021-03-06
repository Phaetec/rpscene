import re
from defusedxml.ElementTree import parse
from django.core.exceptions import ObjectDoesNotExist

from items.errors import ItemAlreadyExists
from items.models import Armor, BonusModifier, Money
from .errors import XMLModifierCategoryNotRecognized


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
        return "Light Armor"
    elif typename == "MA":
        return "Medium Armor"
    elif typename == "HA":
        return "Heavy Armor"
    elif typename == "S":
        return "Shield"
    else:
        raise TypeError("Item Type not recognized")


def parse_modifiers(modifiers, item):
    """Parse modifiers and create corresponding objects."""
    for mod in modifiers:
        category = mod.attrib['category']
        text = mod.text
        if category == "bonus":
            applied_to, modifier = re.split("\+", text)
            mod = BonusModifier(belongs_to=item,
                                modifier=int(modifier.strip()),
                                applied_to=applied_to.strip())
            mod.save()
        elif category == "skills":
            # TODO
            pass
        elif category == "ability score":
            # TODO
            pass
        else:
            raise XMLModifierCategoryNotRecognized("Modifier not recognized")


def is_magic(item):
    magic_attr = item.find("magic")
    if not magic_attr:
        return False
    if magic_attr.text != "1":
        return False
    return True


def parse_strength_requirement(item):
    strength_var = item.find("strength")
    if strength_var.text is None:
        return 0
    try:
        requirement = int(strength_var.text)
        return requirement
    except (TypeError, ValueError):
        return 0


def parse_details(detail):
    if detail is None:
        return False, False, "COMMON"
    detailstring = detail.text
    attunement = False
    cursed = False
    if "(requires attunement)" in detailstring:
        attunement = True
    if "cursed" in detailstring:
        cursed = True
    if "artifact" in detailstring:
        return attunement, cursed, "ARTIFACT"
    if "legendary" in detailstring:
        return attunement, cursed, "LEGENDARY"
    # Never put the rare case before very rare. Same with uncommon and common
    if "very rare" in detailstring:
        return attunement, cursed, "VERY_RARE"
    if "rare" in detailstring:
        return attunement, cursed, "RARE"
    if "uncommon" in detailstring:
        return attunement, cursed, "UNCOMMON"
    if "common" in detailstring:
        return attunement, cursed, "COMMON"

    return attunement, cursed, "NO_INFO"


def parse_text(texts):
    description = ""
    for text in texts:
        if text.text is None:
            description += "\n"
        else:
            description += text.text + "\n"
    return description


def create_armor(item):
    # TODO Forgot to take modifier into account
    name = item.find("name").text
    type_str = convert_type(item.find("type").text)
    magic = is_magic(item)
    attunement, cursed, rarity = parse_details(item.find("detail"))
    weight = float(item.find("weight").text)
    ac = int(item.find("ac").text)
    description = parse_text(item.findall("text"))
    stealth_disadvantage = True if item.find("stealth").text == "1" else False
    strength_requirement = parse_strength_requirement(item)

    try:
        Armor.objects.get(name=name)
        # Object already exists, raise an Error
        raise ItemAlreadyExists("An Item with this name already exists.")
    except ObjectDoesNotExist:
        new_armor = Armor(name=name, type=type_str, magic=magic, requires_attunement=attunement, cursed=cursed,
                          rarity=rarity, description=description, weight=weight, ac=ac,
                          stealth_disadvantage=stealth_disadvantage, strength_requirement=strength_requirement)
        new_armor.save()
        parse_modifiers(item.findall("modifier"), new_armor)


def create_money(item):
    name = item.find("name").text
    description = parse_text(item.findall("text"))
    weight = float(item.find("weight").text)
    if Money.objects.filter(name=name).exists():
        raise ItemAlreadyExists("An Item with this name already exists.")
    new_money = Money(name=name, description=description, weight=weight, type="Money", rarity="COMMON")
    new_money.save()


def parse_and_store_item(item):
    item_type = item.find("type").text
    # Armor Types: LA, MA, HA (Light, Medium, Heavy Armor), S for Shield
    if item_type in ["LA", "MA", "HA", "S"]:
        create_armor(item)
    elif item_type == "$":
        create_money(item)


def parse_entities(file_path="CorePlusUAWithModern.xml"):
    tree = parse(file_path)
    root = tree.getroot()
    for child in root.findall('item'):
        try:
            parse_and_store_item(child)
        except ItemAlreadyExists:
            pass

        # for attrs in child:
        #    if attrs.tag not in ['weight', 'type', 'text', 'name', 'magic', 'detail', 'roll', 'range', 'dmg1',
        #                         'dmgType', 'property', 'dmg2', 'modifier', 'value', 'stealth', 'strength', 'ac']:
        #        print(attrs.tag)
        #        print(attrs.attrib)
        #       print('---')
