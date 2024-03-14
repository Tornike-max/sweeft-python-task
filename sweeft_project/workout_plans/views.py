from django.contrib.auth import authenticate  

from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer, UserLoginSerializer, ExerciseSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 


from django.shortcuts import render, redirect
from .models import WorkoutPlan, Exercise, WorkoutPlanExercise
from .forms import WorkoutPlanForm
from django.urls import reverse_lazy


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)  
            if user:
                tokens = generate_tokens(user)
                return Response(tokens)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return redirect(reverse_lazy('create_workout_plan'))

def generate_tokens(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }

@api_view(['GET'])
def exercise_list(request):
    exercises = Exercise.objects.all()
    serializer = ExerciseSerializer(exercises, many=True)
    content = JSONRenderer().render(serializer.data)
    return Response(content, content_type='application/json', status=200)

class ExerciseListView(APIView):
    def get(self, request, format=None):
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

def create_workout_plan(request):
    if request.method == 'POST':
        form = WorkoutPlanForm(request.POST)
        if form.is_valid():
            try:
                workout_plan = form.save(commit=False)
                user = User.objects.get(username=request.user.username)  
                workout_plan.user = user 
                workout_plan.save()
                return JsonResponse({'success': 'Workout plan created successfully'})
            except Exception as e:
                print(f"Error creating workout plan: {e}")
                return JsonResponse({'error': 'An error occurred while creating the workout plan'}, status=500)
        else:
            errors = dict(form.errors.items())
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = WorkoutPlanForm()
    return render(request, 'create_workout_plan.html', {'form': form})


def customize_workout(request, workout_plan_id):
    workout_plan = WorkoutPlan.objects.get(pk=workout_plan_id)
    if request.method == 'POST':
        form = ExerciseSelectionForm(request.POST)
        if form.is_valid():
            exercise_selection = form.save(commit=False)
            exercise_selection.workout_plan = workout_plan
            exercise_selection.save()
            return redirect('customize_workout_success')  
    else:
        form = ExerciseSelectionForm()
    return render(request, 'customize_workout.html', {'form': form, 'workout_plan': workout_plan})
