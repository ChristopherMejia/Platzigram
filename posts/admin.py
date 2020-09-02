from django.contrib import admin


#models

from posts.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Post add Admin  """

    list_display = (
      'user',
      'title',
      'photo',
      'created',  
    )
    list_display_links = ('user',)
    list_filter = (
        'created',
        'user',
    )

    #Modified Posts

    fieldsets = (
        ('Profile', {
            "fields": ('user','profile',),
        }),
        (None, {
            "fields": ('title','photo',),
        }),
        ('Date', {
            "fields":('created',),
        }),
    )
    

    readonly_fields = ('created', 'modified')

