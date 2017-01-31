from django.contrib import admin
from firstapp.models import People,Article,Topics,Tag,invalid_list,Comment,UserProfile,Ticket


# Register your models here.

admin.site.register(People)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Topics)
admin.site.register(Tag)
admin.site.register(invalid_list)
admin.site.register(UserProfile)
admin.site.register(Ticket)