from django.contrib import admin
from .models import Job, Candidate, Application

admin.site.register(Job)
admin.site.register(Candidate)
admin.site.register(Application)