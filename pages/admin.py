from django.contrib import admin
from models import StudentOrganizer

@admin.register(StudentOrganizer)
class StudentOrganizerAdmin(admin.ModelAdmin):
    pass
