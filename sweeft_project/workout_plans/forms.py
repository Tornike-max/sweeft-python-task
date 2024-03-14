from django import forms
from .models import WorkoutPlan, Exercise,WorkoutPlanExercise



class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ['frequency', 'goals', 'duration', 'exercises']

class ExerciseSelectionForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlanExercise 
        fields = ['exercise', 'repetitions', 'sets', 'duration', 'distance']