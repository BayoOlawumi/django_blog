from django.db import models

# Create your models here

class Project(models.Model):
    title = models.CharField(max_length=100, blank=False)
    about = models.TextField(max_length = 1000, blank = True)
    link = models.URLField()
    date_released = models.DateField(null= True,blank = True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    """def show_desc(self):
        return self.about[:50]
    """

class Developer(models.Model):
    SPECIALITY = (
        ('Full-Stack', 'FullStack'),
        ('Back-End', 'Backend'),
        ('Front-End', 'Frontend'),
        ('UI/UX', 'UI/UX')
    )
    projects = models.ManyToManyField(Project)
    surname = models.CharField(max_length=50)
    othernames = models.CharField(max_length=50)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='developers')
    role = models.CharField(max_length=50, choices = SPECIALITY)

    def __str__(self):
        return self.surname + " " + self.othernames

