from django.db import models


class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self. username


class MachineStatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    machineID = models.IntegerField()
    Status = models.CharField(max_length=50)
    StartID = models.IntegerField()
    endID = models.IntegerField()
    description = models.CharField(max_length=100)
    comments = models.CharField(max_length=255)

    class Meta:
        db_table = 'MachineStatus'

    def __str__(self):
        return self.id


class MachineInfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=50)
    serialNum = models.CharField(max_length=50)
    swVersion = models.CharField(max_length=50)

    class Meta:
        db_table = 'MachineInfo'

    def __str__(self):
        return self.name


class StartStatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    userID = models.IntegerField()
    Time = models.DateField()

    class Meta:
        db_table = 'StartStatus'

    def __str__(self):
        return self.id


class EndStatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    userID = models.IntegerField()
    Time = models.DateField()

    class Meta:
        db_table = 'EndStatus'

    def __str__(self):
        return self.id
