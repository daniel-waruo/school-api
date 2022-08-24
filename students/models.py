from django.db import models


class Student(models.Model):
    """ Model for storing details belonging to a particular student
        Attributes:
            first_name (str): First name of the student.
            last_name (str): Last name of the student`.
            profile_photo (:obj): The image of the student.
            id_number (str): The student's national ID
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_photo = models.ImageField(upload_to='student_profile_photos')
    id_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Activity(models.Model):
    """ Model for storing the activities a particular students undertakes
        Attributes:
            name (str): Name of the activity
            description (str): Description of the activity
            students (:obj): Students who are partaking in that activity
    """
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)

    students = models.ManyToManyField(Student, related_name='activities')

    def __str__(self):
        return f"{self.name} "
