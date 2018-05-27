from django.db import models

# Create your models here.
class Blog(models.Model):
    titutolo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=500)
    img = models.ImageField(upload_to='img_blog')
    data_blog = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.descricao
