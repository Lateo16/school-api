from django.db import models


class Guardian(models.Model):
    name = models.CharField(max_length=60, null=False)
    telephone = models.CharField(max_length=10)
    location = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length=40, null=False)
    courseCode = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=40, null=False)
    # head = models.ForeignKey(
    #     to=Lecturer,
    #     on_delete=models.CASCADE
    # )
    totalStudents = models.IntegerField()
    totalLecturers = models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    firstName = models.CharField(max_length=25, null=False)
    lastName = models.CharField(max_length=25, null=False)
    yearOfBirth = models.DateField()
    currentLevel = models.IntegerField()
    department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE
    )
    guardian = models.ForeignKey(
        to=Guardian,
        on_delete=models.CASCADE,
        related_name="students"
    )
    coursesRegistered = models.ManyToManyField(
        to=Courses
    )

    def __str__(self):
        return self.firstName


class Lecturer(models.Model):
    name = models.CharField(max_length=40, null=False)
    department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        to=Courses,
        on_delete=models.CASCADE
    )

