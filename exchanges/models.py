from django.db import models
from django.contrib.auth.models import User
from skills.models import Skill


class ExchangeRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    sender_skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='offered')
    receiver_skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='requested')

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username} ({self.status})"


class Review(models.Model):
    exchange = models.OneToOneField(ExchangeRequest, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.reviewer.username} for Exchange #{self.exchange.id}"