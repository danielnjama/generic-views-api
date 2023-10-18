from django.db import models

# Create your models here.
studentgender = (
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
)
class students(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(choices=studentgender,max_length=10)
    marks = models.IntegerField()
    Dateofbirth = models.DateField()

    def __str__(self):
        return self.name