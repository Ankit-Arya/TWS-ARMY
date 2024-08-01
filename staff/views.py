from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Candidate, Course, Leg, Subject, CandidateMarks
from .forms import CandidateForm, CourseForm, LegForm, SubjectForm, CandidateMarksForm

def staffui(request):
    return render(request, 'staffui.html')

# Candidates Views
def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidate_list.html', {'candidates': candidates})

def candidate_detail(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    return render(request, 'candidate_detail.html', {'candidate': candidate})

def candidate_create(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidate_list')
    else:
        form = CandidateForm()
    return render(request, 'candidate_form.html', {'form': form})

def candidate_update(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    if request.method == 'POST':
        form = CandidateForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('candidate_detail', pk=candidate.pk)
    else:
        form = CandidateForm(instance=candidate)
    return render(request, 'candidate_form.html', {'form': form})

def candidate_delete(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    if request.method == 'POST':
        candidate.delete()
        return redirect('candidate_list')
    return render(request, 'candidate_confirm_delete.html', {'candidate': candidate})

# Courses Views
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course_detail.html', {'course': course})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form})

def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form.html', {'form': form})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'course_confirm_delete.html', {'course': course})

# Legs Views
def leg_list(request):
    legs = Leg.objects.all()
    return render(request, 'leg_list.html', {'legs': legs})

def leg_detail(request, pk):
    leg = get_object_or_404(Leg, pk=pk)
    return render(request, 'leg_detail.html', {'leg': leg})

def leg_create(request):
    if request.method == 'POST':
        form = LegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leg_list')
    else:
        form = LegForm()
    return render(request, 'leg_form.html', {'form': form})

def leg_update(request, pk):
    leg = get_object_or_404(Leg, pk=pk)
    if request.method == 'POST':
        form = LegForm(request.POST, instance=leg)
        if form.is_valid():
            form.save()
            return redirect('leg_detail', pk=leg.pk)
    else:
        form = LegForm(instance=leg)
    return render(request, 'leg_form.html', {'form': form})

def leg_delete(request, pk):
    leg = get_object_or_404(Leg, pk=pk)
    if request.method == 'POST':
        leg.delete()
        return redirect('leg_list')
    return render(request, 'leg_confirm_delete.html', {'leg': leg})

# Subjects Views
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})

def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    return render(request, 'subject_detail.html', {'subject': subject})

def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'subject_form.html', {'form': form})

def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_detail', pk=subject.pk)
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'subject_form.html', {'form': form})

def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return render(request, 'subject_confirm_delete.html', {'subject': subject})

# Candidate Marks Views
def candidate_marks_list(request):
    candidate_marks = CandidateMarks.objects.all()
    return render(request, 'candidate_marks_list.html', {'candidate_marks': candidate_marks})

def candidate_marks_detail(request, pk):
    candidate_marks = get_object_or_404(CandidateMarks, pk=pk)
    return render(request, 'candidate_marks_detail.html', {'candidate_marks': candidate_marks})

def candidate_marks_create(request):
    if request.method == 'POST':
        form = CandidateMarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidate_marks_list')
    else:
        form = CandidateMarksForm()
    return render(request, 'candidate_marks_form.html', {'form': form})

def candidate_marks_update(request, pk):
    candidate_marks = get_object_or_404(CandidateMarks, pk=pk)
    if request.method == 'POST':
        form = CandidateMarksForm(request.POST, instance=candidate_marks)
        if form.is_valid():
            form.save()
            return redirect('candidate_marks_detail', pk=candidate_marks.pk)
    else:
        form = CandidateMarksForm(instance=candidate_marks)
    return render(request, 'candidate_marks_form.html', {'form': form})

def candidate_marks_delete(request, pk):
    candidate_marks = get_object_or_404(CandidateMarks, pk=pk)
    if request.method == 'POST':
        candidate_marks.delete()
        return redirect('candidate_marks_list')
    return render(request, 'candidate_marks_confirm_delete.html', {'candidate_marks': candidate_marks})
