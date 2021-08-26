# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Endstatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EndStatus'


class Machineinfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    machinename = models.CharField(db_column='MachineName', max_length=50)  # Field name made lowercase.
    serialnum = models.CharField(db_column='SerialNum', max_length=50)  # Field name made lowercase.
    swversion = models.CharField(db_column='SWVersion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MachineInfo'


class Machinestatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    machineid = models.ForeignKey(Machineinfo, models.DO_NOTHING, db_column='MachineID')
    status = models.CharField(db_column='Status', max_length=50)
    startid = models.ForeignKey('Startstatus', models.DO_NOTHING, db_column='StartID')
    endid = models.ForeignKey(Endstatus, models.DO_NOTHING, db_column='EndID', blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MachineStatus'


class Startstatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StartStatus'


class Users(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=50)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.
    usergroup = models.CharField(db_column='UserGroup', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
