from django.contrib import admin
from frontapp.models import Mood
from frontapp.models import Tracking

class MoodAdmin(admin.ModelAdmin):
    pass
admin.site.register(Mood, MoodAdmin)

class TrackingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tracking, TrackingAdmin)
