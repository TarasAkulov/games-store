from django.db import models

class Game(models.Model):
	title = models.CharField(max_length=100, unique=True, null=False)
	genre = models.ForeignKey('Genre', on_delete=models.CASCADE, null=False)
	description = models.TextField(null=True, blank=True)
	release_date = models.DateField(null=True, blank=True)
	developer = models.ForeignKey('Developer', on_delete=models.CASCADE, null=False)
	image = models.ImageField(upload_to='games/images/', null=False, blank=False)
	video = models.FileField(upload_to='games/videos/', null=True, blank=True)
	story = models.TextField(null=True, blank=True)
	min_requirements = models.ForeignKey('SystemRequirement', on_delete=models.CASCADE, null=True, blank=True)
	optimal_requirements = models.ForeignKey('SystemRequirement', on_delete=models.CASCADE, null=True, blank=True)

	class Meta:
		verbose_name = 'Гра'
		verbose_name_plural = 'Ігри'

	def __str__(self):
		return self.title

class Genre(models.Model):
	name = models.CharField(max_length=50, unique=True, null=False)

	class Meta:
		verbose_name = 'Жанр'
		verbose_name_plural = 'Жанри'
	
	def __str__(self):
		return self.name

class Developer(models.Model):
	name = models.CharField(max_length=100, unique=True, null=False)
	website = models.CharField(null=True, blank=True)

	class Meta:
		verbose_name = 'Розробник'
		verbose_name_plural = 'Розробники'
	
	def __str__(self):
		return self.name

class SystemRequirement(models.Model):
	os = models.CharField(max_length=50, null=False)
	ram = models.CharField(max_length=20, null=False)
	storage = models.CharField(max_length=20, null=False)
	processor = models.CharField(max_length=100, null=False)
	video_card = models.CharField(max_length=100, null=False)

	class Meta:
		verbose_name = 'Системна вимога'
		verbose_name_plural = 'Системні вимоги'
	
	def __str__(self):
		return f"{self.os}, {self.ram}, {self.storage}, {self.processor}, {self.video_card}"