import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sweeft_project.sweeft_project.settings")
django.setup()

from workout_plans.models import Exercise

def populate_exercises():
    exercises = [
        {
            'name': 'Push-up',
            'description': 'A classic bodyweight exercise targeting the chest, shoulders, and triceps.',
            'instructions': '1. Start in a plank position with your hands shoulder-width apart. 2. Lower your body until your chest nearly touches the floor. 3. Push back up to the starting position.',
            'target_muscles': 'Chest, Shoulders, Triceps'
        },
        {
            'name': 'Squat',
            'description': 'A compound exercise targeting the quadriceps, hamstrings, glutes, and lower back.',
            'instructions': '1. Stand with feet shoulder-width apart. 2. Lower your body by bending your knees and pushing your hips back. 3. Keep your chest up and back straight. 4. Return to the starting position by driving through your heels.',
            'target_muscles': 'Quadriceps, Hamstrings, Glutes, Lower Back'
        },
        {
            'name': 'Deadlift',
            'description': 'A weightlifting exercise where a loaded barbell is lifted off the ground to the hips, then lowered back to the ground.',
            'instructions': '1. Stand with feet hip-width apart, toes under the barbell. 2. Bend knees, grip the barbell with hands just outside knees. 3. Keep back straight, chest up. 4. Lift the bar by straightening hips and knees. 5. Lower the bar back to the ground by bending hips and knees.',
            'target_muscles': 'Hamstrings, Glutes, Lower Back'
        },
        {
            'name': 'Bench Press',
            'description': 'A weight training exercise that works the pectoralis major, anterior deltoids, and triceps.',
            'instructions': '1. Lie on a flat bench with eyes under the bar. 2. Grip the bar slightly wider than shoulder-width. 3. Lower the bar to the mid-chest. 4. Press the bar back up until arms are straight.',
            'target_muscles': 'Chest, Shoulders, Triceps'
        },
    ]

    for exercise_data in exercises:
        exercise, created = Exercise.objects.get_or_create(name=exercise_data['name'], defaults=exercise_data)
        if created:
            print(f"Exercise '{exercise.name}' created.")
        else:
            print(f"Exercise '{exercise.name}' already exists.")

if __name__ == "__main__":
    populate_exercises()