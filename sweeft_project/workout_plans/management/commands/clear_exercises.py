from django.core.management.base import BaseCommand
from workout_plans.models import Exercise

class Command(BaseCommand):
    help = 'Clear all Exercise objects from the database'

    def handle(self, *args, **kwargs):
        Exercise.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared all Exercise objects'))

