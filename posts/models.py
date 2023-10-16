from django.db import models

# Create your models here.
class recipes(models.Model):
    recipe_name = models.CharField(verbose_name= 'Recipe name', max_length=120, blank=False, null=False)
    preparation = models.TextField(verbose_name= 'Preparations',blank=True, null=False)
    recipe_img = models.ImageField(verbose_name='recipe Image', upload_to='recipes', blank=True, null=True)
    tags = models.CharField(verbose_name='Food Tags', max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe_name
    
    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'