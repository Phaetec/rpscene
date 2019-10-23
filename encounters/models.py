from django.db import models

from user_manager.models import User


class Encounter(models.Model):
    """
    Models a typical (currently combat) encounter. Currently only works with D&D 5e NPCs.
    """
    name = models.CharField(max_length=100, null=False, default="")
    loot = models.TextField(null=True, max_length=10000)
    description = models.TextField(null=True, max_length=10000)
    # Enemies are modelled through "EncounterNPC" model


class EncounterNPC(models.Model):
    npc = models.ForeignKey("DnD5eNPC", null=False, on_delete=models.CASCADE, related_name="encounters")
    encounter = models.ForeignKey("Encounter", null=False, on_delete=models.CASCADE, related_name="npcs")


# ############# NPCs
class NPC(models.Model):
    """
    Models generic NPCs that are versatile. If you need special fields for a certain Tabletop-RPG System,
    create a subclass.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100, null=False, default="")
    description = models.TextField(max_length=20000, blank=True, default='')
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class DnD5eNPC(NPC):
    """
    Models the special stats that are present in Dungeons & Dragons 5th Edition NPCs.
    """
    creature_type = models.CharField(default='', blank=True, max_length=100)
    alignment = models.CharField(default='', blank=True, max_length=100)
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)

    armor_class = models.IntegerField(null=False, default=10)
    armor_type = models.CharField(blank=True, default='', max_length=100)
    hit_points = models.CharField(null=False, max_length=100, default="1d10")
    speed = models.CharField(null=False, max_length=100, default="30 ft.")

    passive_perception = models.IntegerField(null=True, blank=True)
    saving_throw_strength_bonus = models.IntegerField(null=True, blank=True)
    saving_throw_dexterity_bonus = models.IntegerField(null=True, blank=True)
    saving_throw_constitution_bonus = models.IntegerField(null=True, blank=True)
    saving_throw_intelligence_bonus = models.IntegerField(null=True, blank=True)
    saving_throw_wisdom_bonus = models.IntegerField(null=True, blank=True)
    saving_throw_charisma_bonus = models.IntegerField(null=True, blank=True)
    initiative_bonus = models.IntegerField(null=True, blank=True)

    acrobatics_bonus = models.IntegerField(null=True, blank=True)
    animal_handling_bonus = models.IntegerField(null=True, blank=True)
    arcana_bonus = models.IntegerField(null=True, blank=True)
    athletics_bonus = models.IntegerField(null=True, blank=True)
    deception_bonus = models.IntegerField(null=True, blank=True)
    history_bonus = models.IntegerField(null=True, blank=True)
    insight_bonus = models.IntegerField(null=True, blank=True)
    intimidation_bonus = models.IntegerField(null=True, blank=True)
    investigation_bonus = models.IntegerField(null=True, blank=True)
    medicine_bonus = models.IntegerField(null=True, blank=True)
    nature_bonus = models.IntegerField(null=True, blank=True)
    perception_bonus = models.IntegerField(null=True, blank=True)
    performance_bonus = models.IntegerField(null=True, blank=True)
    persuasion_bonus = models.IntegerField(null=True, blank=True)
    religion_bonus = models.IntegerField(null=True, blank=True)
    sleight_of_hand_bonus = models.IntegerField(null=True, blank=True)
    stealth_bonus = models.IntegerField(null=True, blank=True)
    survival_bonus = models.IntegerField(null=True, blank=True)

    damage_immunities = models.CharField(blank=True, default='', max_length=500)
    condition_immunities = models.CharField(blank=True, default='', max_length=500)
    damage_vulnerabilities = models.CharField(blank=True, default='', max_length=500)
    damage_resistances = models.CharField(blank=True, default='', max_length=500)

    senses = models.CharField(blank=True, default='', max_length=500)
    languages = models.CharField(blank=True, default='', max_length=500)
    challenge_rating = models.FloatField(null=False, default="1")


class DnD5eAbility(models.Model):
    name = models.CharField(blank=True, default="Ability", max_length=100)
    description = models.TextField(null=True, max_length=10000)


class DnD5eAction(DnD5eAbility):
    npc = models.ForeignKey(DnD5eNPC, null=False, on_delete=models.CASCADE, related_name="actions")


class DnD5eSpecialAbility(DnD5eAbility):
    npc = models.ForeignKey(DnD5eNPC, null=False, on_delete=models.CASCADE, related_name="special_abilities")


class DnD5eLegendaryAction(DnD5eAbility):
    npc = models.ForeignKey(DnD5eNPC, null=False, on_delete=models.CASCADE, related_name="legendary_actions")


class DnD5eLairAction(DnD5eAbility):
    npc = models.ForeignKey(DnD5eNPC, null=False, on_delete=models.CASCADE, related_name="lair_actions")
