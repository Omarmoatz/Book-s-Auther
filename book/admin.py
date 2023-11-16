from django.contrib import admin
from .models import Book , Auther, Review


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title','auther']
    list_filter = ['price','publication_date']

admin.site.register(Book,BookAdmin)
admin.site.register(Review)
admin.site.register(Auther)





