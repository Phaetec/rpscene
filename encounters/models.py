from django.db import models


class NPC(models.Model):
    """
    Models generic NPCs that are versatile. If you need special fields for a certain Tabletop-RPG System,
    create a subclass.
    """
    name = models.CharField(max_length=100, null=False, default="")
    description = models.TextField(max_length=20000, null=True)
    picture = models.ImageField(null=True)

    def __str__(self):
        return self.name


class DnD5eNPC(NPC):
    """
    Models the special stats that are present in Dungeons & Dragons 5th Edition NPCs
    """
    strength = models.IntegerField(null=True)
    dexterity = models.IntegerField(null=True)
    constitution = models.IntegerField(null=True)
    intelligence = models.IntegerField(null=True)
    wisdom = models.IntegerField(null=True)
    charisma = models.IntegerField(null=True)

    armor_class = models.IntegerField(null=False, default=10)
    armor_type = models.CharField(null=True, max_length=100)
    hit_points = models.CharField(null=False, max_length=100, default="1d10")
    speed = models.CharField(null=False, max_length=100, default="30 ft.")

    passive_perception = models.IntegerField(null=True)
    saving_throw_strength_bonus = models.IntegerField(null=True)
    saving_throw_dexterity_bonus = models.IntegerField(null=True)
    saving_throw_constitution_bonus = models.IntegerField(null=True)
    saving_throw_intelligence_bonus = models.IntegerField(null=True)
    saving_throw_wisdom_bonus = models.IntegerField(null=True)
    saving_throw_charisma_bonus = models.IntegerField(null=True)
    initiative_bonus = models.IntegerField(null=True)

    acrobatics_bonus = models.IntegerField(null=True)
    animal_handling_bonus = models.IntegerField(null=True)
    arcana_bonus = models.IntegerField(null=True)
    athletics_bonus = models.IntegerField(null=True)
    deception_bonus = models.IntegerField(null=True)
    history_bonus = models.IntegerField(null=True)
    insight_bonus = models.IntegerField(null=True)
    intimidation_bonus = models.IntegerField(null=True)
    investigation_bonus = models.IntegerField(null=True)
    medicine_bonus = models.IntegerField(null=True)
    nature_bonus = models.IntegerField(null=True)
    perception_bonus = models.IntegerField(null=True)
    performance_bonus = models.IntegerField(null=True)
    persuasion_bonus = models.IntegerField(null=True)
    religion_bonus = models.IntegerField(null=True)
    sleight_of_hand_bonus = models.IntegerField(null=True)
    stealth_bonus = models.IntegerField(null=True)
    survival_bonus = models.IntegerField(null=True)

    damage_immunities = models.CharField(null=True, max_length=500)
    condition_immunities = models.CharField(null=True, max_length=500)
    damage_vulnerabilities = models.CharField(null=True, max_length=500)
    damage_resistances = models.CharField(null=True, max_length=500)

    senses = models.CharField(null=True, max_length=500)
    languages = models.CharField(null=True, max_length=500)
    challenge_rating = models.FloatField(null=False, default="1")


class DnD5eAbility(models.Model):
    name = models.CharField(null=False, default="Ability", max_length=100)
    description = models.TextField(null=True, max_length=10000)


class DnD5eAction(DnD5eAbility):
    npc = models.ForeignKey(DnD5eNPC, null=False, on_delete=models.CASCADE, related_name="actions")


class DnD5eSpecialAbility(DnD5eAbility):
    npc = models.ForeignKey(DnD5eNPC, null=False, on_delete=models.CASCADE, related_name="special_abilities")


class DnD5eLegendaryAction(DnD5eAbility):
    npc = models.ForeignKey(DnD5eNPC, null=False, on_delete=models.CASCADE, related_name="legendary_actions")


class DnD5eLairAction(DnD5eAbility):
    npc = models.ForeignKey(DnD5eNPC, null=False, on_delete=models.CASCADE, related_name="lair_actions")
