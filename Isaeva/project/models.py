from django.db import models

# Create your models here.
class Project (models.Model):
    title = models.CharField(max_length=100)  # первое поле типа чар-символ с ограничением в 100символов
    description = models.TextField()    # поле с описанием без ограничением
    technology = models.CharField(max_length=50)  # поле с использоваными технологиями с 50символами
    image = models.FileField(upload_to='img/')  # картинка