from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Customer(User):
    username = models.CharField(max_length=155)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'customer'
        verbose_name = 'customer'
        verbose_name_plural = 'customers'


class MovieCategory(models.Model):
    title = models.CharField(max_length=155, verbose_name='Category name')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'movie_category'
        verbose_name = 'movie_category'
        verbose_name_plural = 'movie_categories'


class Movie(models.Model):
    CHOICE_LANGUAGE = [
        ('UZ', "O'zbek tili"),
        ('RU', "Rus tili"),
        ('EN', "Ingliz tili")
    ]

    title = models.CharField(max_length=155, verbose_name='Movie name')
    description = models.TextField()
    category = models.ForeignKey(MovieCategory, on_delete=models.CASCADE)
    language = models.CharField(max_length=20, choices=CHOICE_LANGUAGE)
    date_of_manufacture = models.DateField(verbose_name='Date of manufacture')
    duration = models.TimeField(verbose_name='Movie duration')
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'movie'
        verbose_name_plural = 'movies'


class MovieFile(models.Model):
    CHOICE_FORMAT = [
        ('480', "Mobile HD"),
        ('720', 'HD'),
        ('1080', 'Full HD')
    ]

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    video = models.FileField(verbose_name='Movie video', choices=CHOICE_FORMAT, upload_to='files/')
    image = models.ImageField(verbose_name='Movie image', upload_to='images/')

    @property
    def image_url(self):
        if self.image:
            return "%s%s" % (settings.HOST, self.image.url)

    @property
    def video_url(self):
        if self.video:
            return "%s%s" % (settings.HOST, self.video.url)

    def __str__(self):
        return self.movie.title

    class Meta:
        db_table = 'movie_file'
        verbose_name = 'movie_file'
        verbose_name_plural = 'movie_files'


class Review(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=155)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
