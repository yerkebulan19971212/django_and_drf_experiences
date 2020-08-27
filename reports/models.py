from django.db import models


class TestCallResults(models.Model):
    route = models.CharField(max_length=12, null=True, blank=True)
    second_route = models.CharField(max_length=12, default="")
    duration = models.IntegerField(default=0)
    call_date = models.DateTimeField()
    cal_rec = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.route


class TestCallResultFile(models.Model):
    file = models.FileField(upload_to="csv_files")
