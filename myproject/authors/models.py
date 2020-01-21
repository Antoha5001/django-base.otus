from django.db import models

class Author(models.Model):



    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Author'

# в БД записывается первое значение, второе отображается
    LEVELS = (
        ('J', 'Junior'),
        ('M', 'Middle'),
        ('S', 'Senior'),
    )

    first_name = models.fields.CharField(max_length=50)
    last_name = models.fields.CharField(max_length=50)
    level = models.fields.CharField(max_length=1, choices=LEVELS, default=LEVELS[0][0])
    email = models.fields.EmailField(null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Create your models here.
