from django.db import models


class Stud(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    mileage = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'stud'

class Apply(models.Model):
    id = models.IntegerField(primary_key=True)
    unit = models.ForeignKey("ProfApp.Unit", on_delete=models.DO_NOTHING, blank=True, null=True)
    student = models.ForeignKey(Stud, on_delete=models.DO_NOTHING, blank=True, null=True)
    admin_mileage = models.IntegerField()
    apply_time = models.DateTimeField()
    remain_semaster = models.IntegerField(blank=True, null=True)
    result = models.BooleanField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'apply'

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey("ProfApp.Subject", on_delete=models.DO_NOTHING, blank=True, null=True)
    category = models.BooleanField()
    content = models.TextField()
    time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'post'