from django.urls import path
from workout_plans.views import UserRegisterView, UserLoginView,ExerciseListView
from . import views  


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('exercises/', ExerciseListView.as_view(), name='exercise_list'),
    path('create/', views.create_workout_plan, name='create_workout_plan'),
    path('customize/<int:workout_plan_id>/', views.customize_workout, name='customize_workout'),
]

