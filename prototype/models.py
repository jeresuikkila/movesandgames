from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    video_link = models.URLField()
    rules = models.TextField()
    player_count = models.CharField(max_length=200)

# - description
# - video
# - photos
# - rules
# - player count
# - 