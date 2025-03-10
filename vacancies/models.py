from django.db import models
from pytils.translit import slugify

class Category(models.Model):
	name = models.CharField("Название категории", max_length=255)
	slug = models.SlugField(unique=True, editable=False, blank=True)

	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории" 

	def __str__(self):
		return self.name
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)
	

class Vacancy(models.Model):
	title = models.CharField("Заголовок", max_length=255)
	description = models.TextField("Описание")
	company = models.CharField("Название компании", max_length=80)
	location = models.CharField("Местоположение", max_length=255)
	data_posted = models.DateField("Дата публикации", auto_now_add=True)



	def __str__(self):
		return self.title
# Create your models here.

