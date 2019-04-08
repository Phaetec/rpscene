from django.shortcuts import render

# Create your views here.
from items.models import Armor, Money
from persistence import xml_parser


def armory(request):
    xml_parser.parse_entities()
    armory = Armor.objects.all()
    treasury = Money.objects.all()
    return render(request, 'items/armory.html', {"armory": armory,
                                                 "treasury": treasury})
