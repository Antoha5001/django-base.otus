from django.db import models
from django.db.models.signals import post_save


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

    pass_id = models.CharField(max_length=10, unique=True, null=True)
    email = models.EmailField(unique=True)
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='info'
    )

    def __str__(self):
        return f'{self.pass_id}'


def new_student_created(instance, created, **kwargs):
    DOMEN = 'playground.org'
    if not created:
        return
    count = Student.objects.filter(first_name=instance.first_name).count()
    email = f'{instance.first_name}{count}@{DOMEN}'.lower()
    StudentInfo.objects.create(email=email, student=instance)


post_save.connect(new_student_created, Student)


class Publisher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'Publisher: {self.first_name} {self.last_name}'


class Articles(models.Model):
    title = models.CharField(max_length=250)
    # body
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
