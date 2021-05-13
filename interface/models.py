from djongo import models

class Person(models.Model):
    # _id = models.ObjectIdField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=30)

class Tasks(models.Model):
    Task_name = models.CharField(max_length=30)
    Task_start = models.CharField(max_length=30)
    Task_end = models.CharField(max_length=30)