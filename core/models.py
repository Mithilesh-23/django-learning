from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    branch = models.CharField(max_length = 50)
    email = models.EmailField()


    # this function controls now model objects are display
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    salary = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name  # using this function we show the name of 
                            # teacher in admin board 

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    isbn = models.CharField(max_length=30)
    price = models.IntegerField()
    pages = models.IntegerField()
    published_year = models.DateField()
    available = models.BooleanField(default=True)

    borrower = models.ForeignKey(
        'Borrower',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books"
    )

    def __str__(self):
        return self.title


class Borrower(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    