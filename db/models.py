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
	min_requirements = models.ForeignKey('SystemRequirement', on_delete=models.CASCADE, related_name='min_req', null=True, blank=True)
	optimal_requirements = models.ForeignKey('SystemRequirement', on_delete=models.CASCADE, related_name='optimal_req', null=True, blank=True)

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
	website = models.CharField(max_length=255, null=True, blank=True)

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

class Seller(models.Model):
	name = models.CharField(max_length=100, unique=True, null=False)
	website = models.CharField(max_length=255, null=True, blank=True)

	class Meta:
		verbose_name = 'Продавець'
		verbose_name_plural = 'Продавці'
	
	def __str__(self):
		return self.name
	
class SellItem(models.Model):
	seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=False)
	game = models.ForeignKey(Game, on_delete=models.CASCADE, null=False)
	price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
	website = models.CharField(max_length=255, null=True, blank=True)

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товари'

	def __str__(self):
		return f"{self.game.title} - {self.seller.name} - {self.price} грн"
	
class User(models.Model):
	username = models.CharField(max_length=50, unique=True, null=False)
	email = models.EmailField(unique=True, null=False)
	password = models.CharField(max_length=128, null=False)
	image = models.ImageField(upload_to='users/images/', null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Користувач'
		verbose_name_plural = 'Користувачі'
	
	def __str__(self):
		return self.username

class Review(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE, null=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
	rating = models.PositiveIntegerField(null=False)
	comment = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Відгук'
		verbose_name_plural = 'Відгуки'
	
	def __str__(self):
		return f"{self.user.username} - {self.game.title} - {self.rating}"

class UserStory(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE, null=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Сюжет'
		verbose_name_plural = 'Сюжети'
	
	def __str__(self):
		return f"Story for {self.game.title}"