from django.db import models
import uuid

class UserProfile(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to = 'profile')

    def __str__(self) -> str:
        return self.name
    
class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name='story')
    file = models.ImageField(upload_to='story')