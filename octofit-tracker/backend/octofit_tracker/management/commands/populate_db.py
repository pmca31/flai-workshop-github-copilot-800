from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date, timedelta
from pymongo import MongoClient


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create unique index on email field using pymongo
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.users.create_index('email', unique=True)
        self.stdout.write(self.style.SUCCESS('Created unique index on email field'))

        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Mightiest Heroes of Earth defending justice and peace'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Legendary heroes of the DC Universe fighting for truth and justice'
        )
        self.stdout.write(self.style.SUCCESS(f'Created teams: {team_marvel.name}, {team_dc.name}'))

        # Create Users - Marvel Heroes
        self.stdout.write('Creating Marvel heroes...')
        marvel_users = [
            User.objects.create(name='Tony Stark', email='iron.man@marvel.com', team='Team Marvel'),
            User.objects.create(name='Steve Rogers', email='captain.america@marvel.com', team='Team Marvel'),
            User.objects.create(name='Thor Odinson', email='thor@marvel.com', team='Team Marvel'),
            User.objects.create(name='Natasha Romanoff', email='black.widow@marvel.com', team='Team Marvel'),
            User.objects.create(name='Bruce Banner', email='hulk@marvel.com', team='Team Marvel'),
        ]

        # Create Users - DC Heroes
        self.stdout.write('Creating DC heroes...')
        dc_users = [
            User.objects.create(name='Clark Kent', email='superman@dc.com', team='Team DC'),
            User.objects.create(name='Bruce Wayne', email='batman@dc.com', team='Team DC'),
            User.objects.create(name='Diana Prince', email='wonder.woman@dc.com', team='Team DC'),
            User.objects.create(name='Barry Allen', email='flash@dc.com', team='Team DC'),
            User.objects.create(name='Arthur Curry', email='aquaman@dc.com', team='Team DC'),
        ]

        all_users = marvel_users + dc_users
        self.stdout.write(self.style.SUCCESS(f'Created {len(all_users)} users'))

        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = ['running', 'swimming', 'cycling', 'weightlifting', 'yoga', 'martial arts']
        activities_created = 0

        for user in all_users:
            for i in range(5):  # 5 activities per user
                activity_type = activity_types[i % len(activity_types)]
                Activity.objects.create(
                    user_email=user.email,
                    activity_type=activity_type,
                    duration=30 + (i * 10),
                    calories_burned=200 + (i * 50),
                    date=date.today() - timedelta(days=i),
                    notes=f'{user.name} completed {activity_type} training session'
                )
                activities_created += 1

        self.stdout.write(self.style.SUCCESS(f'Created {activities_created} activities'))

        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard...')
        leaderboard_data = [
            {'user': marvel_users[0], 'points': 950},  # Tony Stark
            {'user': dc_users[0], 'points': 920},      # Clark Kent
            {'user': marvel_users[2], 'points': 890},  # Thor
            {'user': dc_users[2], 'points': 870},      # Diana Prince
            {'user': marvel_users[1], 'points': 850},  # Steve Rogers
            {'user': dc_users[1], 'points': 830},      # Bruce Wayne
            {'user': dc_users[3], 'points': 810},      # Barry Allen
            {'user': marvel_users[3], 'points': 790},  # Natasha Romanoff
            {'user': dc_users[4], 'points': 770},      # Arthur Curry
            {'user': marvel_users[4], 'points': 750},  # Bruce Banner
        ]

        for rank, data in enumerate(leaderboard_data, start=1):
            Leaderboard.objects.create(
                user_email=data['user'].email,
                user_name=data['user'].name,
                team=data['user'].team,
                total_points=data['points'],
                rank=rank
            )

        self.stdout.write(self.style.SUCCESS(f'Created {len(leaderboard_data)} leaderboard entries'))

        # Create Workouts
        self.stdout.write('Creating workouts...')
        workouts = [
            {
                'title': 'Super Soldier Strength Training',
                'description': 'Build superhuman strength with this intense workout routine',
                'difficulty_level': 'Advanced',
                'duration': 60,
                'category': 'Strength',
                'recommended_for': 'Heroes seeking peak physical condition'
            },
            {
                'title': 'Speed Force Cardio',
                'description': 'High-intensity cardio to improve speed and endurance',
                'difficulty_level': 'Intermediate',
                'duration': 45,
                'category': 'Cardio',
                'recommended_for': 'Athletes looking to increase speed'
            },
            {
                'title': 'Amazonian Warrior Training',
                'description': 'Combat-focused workout combining strength and agility',
                'difficulty_level': 'Advanced',
                'duration': 75,
                'category': 'Martial Arts',
                'recommended_for': 'Warriors and fighters'
            },
            {
                'title': 'Arc Reactor Core',
                'description': 'Core strengthening exercises for stability and power',
                'difficulty_level': 'Beginner',
                'duration': 30,
                'category': 'Core',
                'recommended_for': 'All fitness levels'
            },
            {
                'title': 'Asgardian Endurance Circuit',
                'description': 'Build god-like endurance with this circuit training',
                'difficulty_level': 'Advanced',
                'duration': 90,
                'category': 'Circuit Training',
                'recommended_for': 'Advanced athletes'
            },
            {
                'title': 'Atlantean Swimming Techniques',
                'description': 'Master the water with these swimming drills',
                'difficulty_level': 'Intermediate',
                'duration': 45,
                'category': 'Swimming',
                'recommended_for': 'Swimmers and aquatic enthusiasts'
            },
            {
                'title': 'Bat-Agility Training',
                'description': 'Improve flexibility and agility with stealth movements',
                'difficulty_level': 'Intermediate',
                'duration': 40,
                'category': 'Agility',
                'recommended_for': 'Those seeking improved flexibility'
            },
            {
                'title': 'Kryptonian Power Lifting',
                'description': 'Maximum strength training for lifting heavy weights',
                'difficulty_level': 'Advanced',
                'duration': 60,
                'category': 'Powerlifting',
                'recommended_for': 'Advanced strength trainers'
            },
        ]

        for workout_data in workouts:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts)} workouts'))

        # Summary
        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))
        self.stdout.write(self.style.SUCCESS(f'Teams: {Team.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Users: {User.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Activities: {Activity.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Leaderboard entries: {Leaderboard.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Workouts: {Workout.objects.count()}'))
        self.stdout.write(self.style.SUCCESS('='*50))
