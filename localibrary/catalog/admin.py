from django.contrib import admin
from .models import Author, Genre, Book, BookInstance,Reviews



#admin.site.register(Author)

#admin.site.register(Book)

admin.site.register(Reviews)

class BookInstanceInLine(admin.TabularInline):
    model=BookInstance
class BookAdmin(admin.ModelAdmin):
    list_display=("title","author")
    inlines=[BookInstanceInLine]
admin.site.register(Book,BookAdmin)
class BookInLine(admin.TabularInline):
    model=Book
class AuthorAdmin(admin.ModelAdmin):
    list_display=("last_name","first_name","data_of_birth","date_of_death")
    fields=["last_name","first_name",("data_of_birth","date_of_death")]
    inlines=[BookInLine]
admin.site.register(Author,AuthorAdmin)
#admin.site.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display=("book","imprint","status","due_back","id")
    fieldsets=(
        (None,{
            'fields':('book','imprint','id')
        }),
        ('Availablity',{
            'fields':('status','due_back')
        }),
    )
admin.site.register(BookInstance,BookInstanceAdmin)
admin.site.register(Genre)

# Register your models here.
