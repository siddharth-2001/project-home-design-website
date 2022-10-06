from django.db import models
from imagesapp.models import Image

# Create your models here.

DESIGN_CHOICES = (
   ( 'home',  'home'),
   ('office', 'office')
)

class ConceptCategory(models.Model):
    name = models.CharField(max_length = 256, blank = False)
    info = models.TextField(blank=True, default='Some info here.')

    def __str__(self):
        return self.name

class Concept(models.Model):
    name          = models.CharField(max_length=256, blank = False)
    concept_cover_image   = models.ImageField(upload_to = 'images/', blank = False)
    concept_type  = models.ForeignKey(ConceptCategory, on_delete = models.CASCADE)
    concept_image = models.ManyToManyField(Image)

    def __str__(self):
        return self.name

class Design(models.Model):
    design_type  = models.CharField(max_length=256, blank=False, choices=DESIGN_CHOICES)
    name         = models.CharField(max_length=256, blank=False)
    cover_image  = models.ImageField(upload_to = 'images/', blank = False)
    design_image = models.ManyToManyField(Image)
    
    def __str__(self):
        return self.name