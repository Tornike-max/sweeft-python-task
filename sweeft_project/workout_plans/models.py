from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField(default="No instructions available")  
    target_muscles = models.CharField(max_length=100, default="Not specified")  

    def __str__(self):
        return self.name
        
class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=50, default='')  
    goals = models.CharField(max_length=100, default='')  
    duration = models.IntegerField(default=0)  
    exercises = models.ManyToManyField(Exercise, through='WorkoutPlanExercise')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_default_values()

    def _set_default_values(self):
        self.frequency = self.frequency or ''
        self.goals = self.goals or ''
        self.duration = self.duration or 0

class WorkoutPlanExercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)
    duration = models.IntegerField(default=0) 
    distance = models.FloatField(default=0)

class WorkoutProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField()
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.FloatField()

