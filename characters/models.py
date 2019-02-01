from django.db import models


class Race(models.Model):
    # Should be unique for every user. i.e. No two "Human" races
    name = models.CharField("Name", max_length=200, null=False, default="Human")

    def __str__(self):
        return self.name


# Create your models here.
class Character(models.Model):
    ALIGNMENT_CHOICES = [
        ('LAWFUL_GOOD', 'Lawful Good'),
        ('NEUTRAL_GOOD', 'Neutral Good'),
        ('CHAOTIC_GOOD', 'Chaotic Good'),
        ('LAWFUL_NEUTRAL', 'Lawful Neutral'),
        ('TRUE_NEUTRAL', 'True Neutral'),
        ('CHAOTIC_NEUTRAL', 'Chaotic Neutral'),
        ('LAWFUL_EVIL', 'Lawful Evil'),
        ('NEUTRAL_EVIL', 'Neutral Evil'),
        ('CHAOTIC_EVIL', 'Chaotic Evil')
    ]

    name = models.CharField("Name", max_length=200, null=False, default="Mysterious Stranger")
    race = models.ForeignKey("Race", null=False, on_delete=models.CASCADE)
    gender = models.CharField("Gender", null=False, default="Unknown", max_length=200)
    ability_class = models.CharField("Class", null=False, default="Peasant", max_length=200)
    hitpoints = models.IntegerField("Hitpoints", null=False, default=1)
    temporary_hitpoints = models.IntegerField("Temporary Hitpoints", null=False, default=0)
    alignment = models.CharField(
        max_length=100,
        choices=ALIGNMENT_CHOICES,
        default='TRUE_NEUTRAL',
    )

    def __str__(self):
        return self.name