from django.db import models

class Prof(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'prof'


class Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    grade = models.IntegerField(blank=True, null=True)
    prof_id = models.ForeignKey(Prof, models.DO_NOTHING, blank=True, null=True)
    unit_list = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'subject'


class Unit(models.Model):
    id = models.IntegerField(primary_key=True)
    apply_period = models.DateTimeField(blank=True, null=True)
    limit_num = models.IntegerField(blank=True, null=True)
    audit_type = models.TextField()
    subject = models.ForeignKey(Subject, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'unit'


