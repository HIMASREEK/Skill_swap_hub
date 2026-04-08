from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='Unknown')
    teach_or_learn = models.CharField(
        max_length=10,
        choices=[('teach', 'Teach'), ('learn', 'Learn')],
        default='teach'
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.name} ({self.teach_or_learn})"