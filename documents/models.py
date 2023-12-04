# models.py

from django.db import models
from accounts.models import User
from django.conf import settings

class Dossier(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Document(models.Model):
    nom = models.CharField(max_length=255)
    fichier = models.FileField(upload_to='documents/')
    categorie = models.CharField(max_length=50)
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE, related_name='documents', null=True, blank=True, default=None)
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents',null=True, blank=True)

    def __str__(self):
        return self.nom

    def get_image_url(self):
        if self.fichier and hasattr(self.fichier, 'url'):
            return self.fichier.url
        return None
 #ghodwa beech naaml commentaire w naaml partie security
     
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80, blank=True)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.document}'