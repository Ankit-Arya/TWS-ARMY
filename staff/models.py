from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=50)
    army_no = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)

    class Meta:
        db_table = 'candidate'

class Course(models.Model):
    name = models.CharField(max_length=100)
    ver_no = models.IntegerField()
    creation_date = models.DateTimeField()
    complition_status = models.IntegerField(default=1)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()

    class Meta:
        db_table = 'courses'

class CourseVersion(models.Model):
    version = models.CharField(max_length=50)

    class Meta:
        db_table = 'course_version'

class Leg(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'leg'

class Subject(models.Model):
    name = models.CharField(max_length=50)
    leg = models.ForeignKey(Leg, on_delete=models.CASCADE)
    total_marks = models.FloatField()

    class Meta:
        db_table = 'subjects'

class CandidateMarks(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    leg = models.ForeignKey(Leg, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.FloatField()

    class Meta:
        db_table = 'candidate_marks'

class CompletionStatus(models.Model):
    status_description = models.CharField(max_length=50)

    class Meta:
        db_table = 'complition_status'
