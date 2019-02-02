from django.db import models


# Create your models here.
class Item(models.Model):
    RARITIES = [
        ("NO_INFO", "No Information"),
        ("COMMON", "Common"),
        ("UNCOMMON", "Uncommon"),
        ("RARE", "rare"),
        ("VERY_RARE", "Very Rare"),
        ("LEGENDARY", "Legendary"),
        ("ARTIFACT", "Artifact")
    ]

    name = models.CharField("Name", max_length=200, null=False, default="")
    weight = models.FloatField("Weight (pounds)", null=False)
    type = models.CharField("Type", max_length=200, null=False, default="Unknown")
    description = models.TextField("Description", max_length=10000, null=False, default="")
    magic = models.BooleanField("Magic?", null=False, default=False)
    rarity = models.CharField("Rarity", max_length=100, null=False, choices=RARITIES, default="NO_INFO")
    cursed = models.BooleanField("Cursed?", null=False, default=False)
    requires_attunement = models.BooleanField("Requires Attunement?", null=False, default=False)


# Here we define more specific Item classes. Since there are quite a few its more elegant than to have a ton of special
# fields on the core Item class.
class Armor(Item):
    ac = models.IntegerField("Armor Class", null=False, default=13)
