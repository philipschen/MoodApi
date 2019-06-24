from django.contrib import admin
from .models import Moodposts
# Register your models here.
class MoodPostAdmin(admin.ModelAdmin):
    list_display = ('owner', 'mood')

admin.site.register(Moodposts, MoodPostAdmin)