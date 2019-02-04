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

    def __str__(self):
        return self.name


# Here we define more specific Item classes. Since there are quite a few its more elegant than to have a ton of special
# fields on the core Item class.
class Armor(Item):
    ac = models.IntegerField("Armor Class", null=False, default=13)
    stealth_disadvantage = models.BooleanField("Stealth Disadvanatage?", null=False, default=False)
    strength_requirement = models.IntegerField("Strength Requirement", null=True)


# Auxiliary models, needed for e.g. OneToMany relations
class BonusModifier(models.Model):
    belongs_to = models.ForeignKey("Item", null=False, on_delete=models.CASCADE, related_name="bonus_mod")
    modifier = models.IntegerField("Modifier", null=False, default=0)
    applied_to = models.CharField("Applied to", null=False, default="ac", max_length=100)


class AbilityModifier(models.Model):
    belongs_to = models.ForeignKey("Item", null=False, on_delete=models.CASCADE, related_name="ability_mod")
    modifier = models.IntegerField("Modifier", null=False, default=0)
    ability = models.CharField("Ability", null=False, default="Strength", max_length=100)


class SkillModifier(models.Model):
    belongs_to = models.ForeignKey("Item", null=False, on_delete=models.CASCADE, related_name="skill_mod")
    # modifier is a char, because there are some strange things like double prof and stuff. Subject to rework
    modifier = models.CharField("Modifier", null=False, default="+0", max_length=100)
    skill = models.CharField("Skill", null=False, default="Initiative", max_length=100)
