from django.urls import path
from . import views

urlpatterns = [
    path('', views.staffui, name='staffui'),
    # Candidates
    path('candidates/', views.candidate_list, name='candidate_list'),
    path('candidates/create/', views.candidate_create, name='candidate_create'),
    path('candidates/<int:pk>/', views.candidate_detail, name='candidate_detail'),
    path('candidates/<int:pk>/edit/', views.candidate_update, name='candidate_update'),
    path('candidates/<int:pk>/delete/', views.candidate_delete, name='candidate_delete'),
    # Courses
    path('courses/', views.course_list, name='course_list'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('courses/<int:pk>/edit/', views.course_update, name='course_update'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course_delete'),
    # Legs
    path('legs/', views.leg_list, name='leg_list'),
    path('legs/create/', views.leg_create, name='leg_create'),
    path('legs/<int:pk>/', views.leg_detail, name='leg_detail'),
    path('legs/<int:pk>/edit/', views.leg_update, name='leg_update'),
    path('legs/<int:pk>/delete/', views.leg_delete, name='leg_delete'),
    # Subjects
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/create/', views.subject_create, name='subject_create'),
    path('subjects/<int:pk>/', views.subject_detail, name='subject_detail'),
    path('subjects/<int:pk>/edit/', views.subject_update, name='subject_update'),
    path('subjects/<int:pk>/delete/', views.subject_delete, name='subject_delete'),
    # Candidate Marks
    path('candidate_marks/', views.candidate_marks_list, name='candidate_marks_list'),
    path('candidate_marks/create/', views.candidate_marks_create, name='candidate_marks_create'),
    path('candidate_marks/<int:pk>/', views.candidate_marks_detail, name='candidate_marks_detail'),
    path('candidate_marks/<int:pk>/edit/', views.candidate_marks_update, name='candidate_marks_update'),
    path('candidate_marks/<int:pk>/delete/', views.candidate_marks_delete, name='candidate_marks_delete'),
]
