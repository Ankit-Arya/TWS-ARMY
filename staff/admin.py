from django.contrib import admin
from .models import Candidate, Course, CourseVersion, Leg, Subject, CandidateMarks, CompletionStatus

# Registering Candidate model
@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'army_no', 'rank', 'unit')
    search_fields = ('name', 'army_no', 'rank', 'unit')
    list_filter = ('rank', 'unit')

# Registering Course model
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ver_no', 'creation_date', 'complition_status', 'date_from', 'date_to')
    search_fields = ('name',)
    list_filter = ('complition_status', 'date_from', 'date_to')

# Registering CourseVersion model
@admin.register(CourseVersion)
class CourseVersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'version')
    search_fields = ('version',)

# Registering Leg model
@admin.register(Leg)
class LegAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course')
    search_fields = ('name',)
    list_filter = ('course',)

# Registering Subject model
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'leg', 'total_marks')
    search_fields = ('name',)
    list_filter = ('leg',)

# Registering CandidateMarks model
@admin.register(CandidateMarks)
class CandidateMarksAdmin(admin.ModelAdmin):
    list_display = ('id', 'candidate', 'course', 'leg', 'subject', 'marks_obtained')
    search_fields = ('candidate__name', 'course__name', 'leg__name', 'subject__name')
    list_filter = ('course', 'leg', 'subject')

# Registering CompletionStatus model
@admin.register(CompletionStatus)
class CompletionStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_description')
    search_fields = ('status_description',)
