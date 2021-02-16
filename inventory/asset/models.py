from django.db import models

class Login(models.Model):
    uname = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)

class Registration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    uname = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)
    cpwd = models.CharField(max_length=200)

class AssetCat(models.Model):
    cat_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cat_name

class Asset(models.Model):
    asset_name = models.CharField(max_length=200)
    asset_number = models.CharField(max_length=30, null=True)
    asset_date = models.DateField()
    asset_category = models.ForeignKey(AssetCat, on_delete=models.CASCADE)
