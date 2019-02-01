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


def parse_entities(file_path):
    tree = parse("CorePlusUAWithModern.xml")
    root = tree.getroot()
    for child in root.findall('item'):
        for attrs in child:
            if attrs.tag not in ['weight', 'type', 'text', 'name', 'magic', 'detail', 'roll', 'range', 'dmg1',
                                 'dmgType', 'property', 'dmg2', 'modifier', 'value', 'stealth', 'strength', 'ac']:
                print(attrs.tag)
                print(attrs.attrib)
                print('---')


parse_entities(True)
