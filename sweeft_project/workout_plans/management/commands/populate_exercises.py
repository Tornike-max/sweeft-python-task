from django.core.management.base import BaseCommand
from workout_plans.models import Exercise

class Command(BaseCommand):
    help = 'Populate predefined exercises'

    def handle(self, *args, **kwargs):
        exercises_data = [
            {"name": "Push-up", "description": "A classic bodyweight exercise.", "instructions": "Lie prone on the ground with hands placed as wide or slightly wider than shoulder width. Keeping the body straight, lower the body to the ground by bending the arms.", "target_muscles": "Chest, Shoulders, Triceps"},
            {"name": "Squats", "description": "A fundamental lower-body exercise.", "instructions": "Stand with your feet shoulder-width apart. Lower your body as far as you can by pushing your hips back and bending your knees.", "target_muscles": "Quadriceps, Hamstrings, Glutes"},
            {"name": "Pull-up", "description": "An upper-body strength exercise.", "instructions": "Grab the pull-up bar with your palms facing away from you and hands shoulder-width apart. Hang with your arms fully extended.", "target_muscles": "Back, Biceps, Forearms"},
            {"name": "Lunges", "description": "A unilateral lower-body exercise.", "instructions": "Stand tall with feet hip-width apart. Step forward with one leg and lower your hips until both knees are bent at about a 90-degree angle.", "target_muscles": "Quadriceps, Hamstrings, Glutes"},
            {"name": "Plank", "description": "A core-strengthening exercise.", "instructions": "Start in a push-up position with your elbows bent and resting on your forearms. Keep your body in a straight line from head to heels.", "target_muscles": "Core, Shoulders, Back"},
            {"name": "Deadlift", "description": "A compound weightlifting exercise.", "instructions": "Stand with your feet hip-width apart, then bend at your hips and knees to lower your body until you can grasp the bar with an overhand grip.", "target_muscles": "Lower Back, Glutes, Hamstrings"},
            {"name": "Bench Press", "description": "A popular upper-body strength exercise.", "instructions": "Lie on a flat bench with your feet on the ground. Grip the barbell with your hands slightly wider than shoulder-width apart. Lower the bar to your chest, then press it back up.", "target_muscles": "Chest, Shoulders, Triceps"},
            {"name": "Dumbbell Shoulder Press", "description": "An effective shoulder-strengthening exercise.", "instructions": "Sit on a bench with back support. Hold a dumbbell in each hand at shoulder level, then press the weights directly above your head.", "target_muscles": "Shoulders, Triceps"},
            {"name": "Russian Twist", "description": "A core exercise that targets the obliques.", "instructions": "Sit on the floor with your knees bent and feet lifted. Hold a weight or medicine ball in front of your chest, then twist your torso from side to side.", "target_muscles": "Obliques, Core"},
            {"name": "Burpees", "description": "A full-body exercise that combines squats, push-ups, and jumps.", "instructions": "Start in a standing position, then squat down and place your hands on the floor. Kick your feet back into a push-up position, then quickly return to the squat position and jump up as high as possible.", "target_muscles": "Legs, Core, Chest, Shoulders"},
            {"name": "Bicycle Crunches", "description": "A variation of crunches that engages the obliques.", "instructions": "Lie on your back with your knees bent and hands behind your head. Lift your shoulders off the floor and bring your right elbow toward your left knee while straightening your right leg. Alternate sides in a pedaling motion.", "target_muscles": "Obliques, Core"},
            {"name": "Barbell Curl", "description": "An isolation exercise for the biceps.", "instructions": "Stand with feet shoulder-width apart and hold a barbell with an underhand grip. Curl the barbell toward your shoulders while keeping your upper arms stationary.", "target_muscles": "Biceps"},
            {"name": "Tricep Dips", "description": "An effective exercise for the triceps.", "instructions": "Sit on a bench and grip the edge with your hands shoulder-width apart. Slide your butt off the bench and lower your body until your elbows are bent at a 90-degree angle, then press back up.", "target_muscles": "Triceps"},
            {"name": "Leg Press", "description": "A lower-body exercise performed on a leg press machine.", "instructions": "Sit on the leg press machine with your feet shoulder-width apart. Push the platform away until your legs are fully extended, then lower the platform back down.", "target_muscles": "Quadriceps, Hamstrings, Glutes"},
            {"name": "Lat Pulldown", "description": "An exercise that targets the latissimus dorsi muscles.", "instructions": "Sit at a lat pulldown machine with your knees secure under the pads. Grip the bar with hands wider than shoulder-width apart, then pull the bar down to your chest.", "target_muscles": "Latissimus Dorsi, Biceps"},
            {"name": "Plank Leg Lifts", "description": "A variation of the plank exercise that adds leg lifts.", "instructions": "Start in a plank position, then lift one leg off the ground while maintaining a straight body. Hold for a few seconds, then lower the leg and repeat with the other leg.", "target_muscles": "Core, Glutes"},
        ]
        for data in exercises_data:
            Exercise.objects.get_or_create(**data)
        self.stdout.write(self.style.SUCCESS('Successfully populated exercises'))
