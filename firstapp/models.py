from django.db import models

# Create your models here.
# tao 2 class || tao 2 table trong SQl
class Category(models.Model):
    name  = models.CharField(max_length = 150,unique = True)

    def __str__(self):
        return self.name

class Website(models.Model):
    category = models.ForeignKey(Category,on_delete = models.PROTECT)
    name = models.URLField(unique = True)
    url = models.URLField(unique = True)
    
    def __str__(self):
        return self.name