from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model
from todo.models import Task
import random
from django.utils import timezone

User = get_user_model()

class Command(BaseCommand):
    help = "Inserting dummy data"
    
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()


    def handle(self, *args, **options):
        user = User.objects.create(email=self.fake.email(),password="Test@123456") # type: ignore
        
        
        for _ in range(5):
            Task.objects.create(
                user = user,
                title = self.fake.paragraph(nb_sentences=1),
                complete = random.choice([True,False]),
                created_date = timezone.now()
            )