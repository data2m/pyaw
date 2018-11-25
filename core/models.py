from django.db import models

class Asset(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    identifier = models.CharField(max_length=30, unique=True)
    TYPE_CHOICES = (
    ("machine", "Machine"),
    ("project", "Project"),
    ("other", "Other"),
    )
    asset_type =  models.CharField(max_length=30, choices=TYPE_CHOICES, default="other")

    def __str__(self):
        return self.identifier

class AssetLink(models.Model):
    asset_parent = models.ForeignKey(Asset, related_name='asset_parent', on_delete=models.CASCADE)
    asset_child = models.ForeignKey(Asset, related_name='asset_child', on_delete=models.CASCADE)
    link_type = models.CharField(max_length=50, blank=True, null=True)

class Machine(Asset):
    name = models.CharField(max_length=50)

class Project(Asset):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.identifier, self.name)

class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    identifier = models.CharField(max_length=30, unique=True)

class ProductLink(models.Model):
    product_parent = models.ForeignKey(Product, related_name='product_parent', on_delete=models.CASCADE)
    product_child = models.ForeignKey(Product, related_name='product_child', on_delete=models.CASCADE)
    link_type = models.CharField(max_length=50, blank=True, null=True)

class ProductAssetLink(models.Model):
    product_parent = models.ForeignKey(Product, related_name='product_asset_parent', on_delete=models.CASCADE)
    asset_child = models.ForeignKey(Asset, related_name='product_asset_child', on_delete=models.CASCADE)
    link_type = models.CharField(max_length=50, blank=True, null=True)