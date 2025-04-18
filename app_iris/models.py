from django.db import models

class IrisModel(models.Model):
    id = models.AutoField(primary_key=True)
    sepal_width = models.FloatField()
    sepal_length = models.FloatField()
    petal_width = models.FloatField()
    petal_length = models.FloatField()
    specie = models.CharField(max_length=25)

    class Meta:
        db_table = 'iris'
