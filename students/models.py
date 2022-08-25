from django.db import models


class Activity(models.Model):
    """ Model for storing the activities a particular students undertakes
        Attributes:
            name (str): Name of the activity
            description (str): Description of the activity
    """
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} "


class Student(models.Model):
    """ Model for storing details belonging to a particular student
        Attributes:
            first_name (str): First name of the student.
            last_name (str): Last name of the student`.
            profile_photo (:obj): The image of the student.
            id_number (str): The student's national ID
            activities (:obj): Activities that a student is participating in
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_photo = models.ImageField(upload_to='media/student_profile_photos')
    id_number = models.CharField(max_length=10)

    activities = models.ManyToManyField(Activity, related_name='students', null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
