from django import template

from encounters.models import DnD5eNPC

register = template.Library()


@register.filter
def with_sign(value: int) -> str:
    sign = "+" if value >= 0 else ""
    return "{0}{1}".format(sign, value)


@register.filter
def modifier(score: int) -> str:
    modifier_value = -5 + score // 2  # Add one for every two steps above zero
    return with_sign(modifier_value)


@register.filter
def with_modifier(value: str) -> str:
    score = int(value)
    return "{0} ({1})".format(score, modifier(score))


@register.simple_tag
def saving_throws(npc: DnD5eNPC) -> str:
    throws = {'Str': npc.saving_throw_strength_bonus,
              'Dex': npc.saving_throw_dexterity_bonus,
              'Con': npc.saving_throw_constitution_bonus,
              'Int': npc.saving_throw_intelligence_bonus,
              'Wis': npc.saving_throw_wisdom_bonus,
              'Cha': npc.saving_throw_charisma_bonus}
    available_throws = [name + " " + with_sign(value) for name, value in throws.items() if value is not None]
    return ", ".join(available_throws)
