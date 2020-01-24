from django.db import models

class StudentInformation(models.Model):

    firsr_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    card_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.firsr_name} {self.last_name}"

class Student(models.Model):

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class StudentInfo(models.Model):

    pass_id = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='info'
    )
    def __str__(self):
        return f'{self.pass_id}'

class Publisher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'Publisher: {self.first_name} {self.last_name}'

class Articles(models.Model):
    title = models.CharField(max_length=250)
    #body
    date = models.DateField(auto_now=False)
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.title}'

class Category(models.Model):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    label = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.label}'

class Shop(models.Model):

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'

    title = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


# Create your models here.
