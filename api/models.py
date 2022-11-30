from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Customer(User):
    # username = models.CharField(max_length=155)
    image = models.ImageField(upload_to='users/image')
    # email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def image_url(self):
        if self.image:
            return "%s%s" % (settings.HOST, self.image.url)

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
        verbose_name = 'movie category'
        verbose_name_plural = 'movie categories'


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
    dislikes = models.IntegerField(default=0)
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
        ('480', "Mobile HD(480)"),
        ('720', 'HD(720)'),
        ('1080', 'Full HD(1080)')
    ]

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    video = models.FileField(verbose_name='Movie video', upload_to='files/')
    video_format = models.CharField(verbose_name='Movie format', max_length=25, choices=CHOICE_FORMAT)
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
        verbose_name = 'movie file'
        verbose_name_plural = 'movie files'


class Review(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=155)
    review = models.TextField()
    reviewed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-reviewed_at']
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
