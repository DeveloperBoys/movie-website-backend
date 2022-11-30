from django.contrib import admin
from .models import (Customer, MovieCategory, Movie, MovieFile, Review)

admin.site.register(Customer)
admin.site.register(MovieCategory)
admin.site.register(Movie)
admin.site.register(MovieFile)
admin.site.register(Review)
