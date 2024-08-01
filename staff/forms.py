from django import forms
from .models import Candidate, Course, Leg, Subject, CandidateMarks

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'army_no', 'rank', 'unit']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'ver_no', 'creation_date', 'complition_status', 'date_from', 'date_to']

class LegForm(forms.ModelForm):
    class Meta:
        model = Leg
        fields = ['name', 'course']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'leg', 'total_marks']

class CandidateMarksForm(forms.ModelForm):
    class Meta:
        model = CandidateMarks
        fields = ['candidate', 'course', 'leg', 'subject', 'marks_obtained']
