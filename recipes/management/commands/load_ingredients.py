import json

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('ingredients.json', ) as f:
            for ingredient in json.load(f):
                title = ingredient['title']
                dimension = ingredient['dimension']

                Ingredient.objects.create(title=title, dimension=dimension)
