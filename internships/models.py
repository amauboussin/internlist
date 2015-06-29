from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Job(models.Model):
    display_name = models.CharField(max_length=140)
    company = models.ForeignKey(Company)
    apply_url = models.CharField(max_length=500)

