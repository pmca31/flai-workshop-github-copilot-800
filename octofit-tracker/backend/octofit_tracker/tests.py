from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import date
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    """Test cases for User model"""

    def setUp(self):
        self.user = User.objects.create(
            name='Test Hero',
            email='test.hero@test.com',
            team='Test Team'
        )

    def test_user_creation(self):
        """Test that a user can be created"""
        self.assertEqual(self.user.name, 'Test Hero')
        self.assertEqual(self.user.email, 'test.hero@test.com')
        self.assertEqual(self.user.team, 'Test Team')

    def test_user_str(self):
        """Test the string representation of a user"""
        self.assertEqual(str(self.user), 'Test Hero')


class TeamModelTest(TestCase):
    """Test cases for Team model"""

    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='A test team for heroes'
        )

    def test_team_creation(self):
        """Test that a team can be created"""
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.description, 'A test team for heroes')

    def test_team_str(self):
        """Test the string representation of a team"""
        self.assertEqual(str(self.team), 'Test Team')


class ActivityModelTest(TestCase):
    """Test cases for Activity model"""

    def setUp(self):
        self.activity = Activity.objects.create(
            user_email='test.hero@test.com',
            activity_type='running',
            duration=30,
            calories_burned=200,
            date=date.today(),
            notes='Test run'
        )

    def test_activity_creation(self):
        """Test that an activity can be created"""
        self.assertEqual(self.activity.user_email, 'test.hero@test.com')
        self.assertEqual(self.activity.activity_type, 'running')
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories_burned, 200)


class LeaderboardModelTest(TestCase):
    """Test cases for Leaderboard model"""

    def setUp(self):
        self.entry = Leaderboard.objects.create(
            user_email='test.hero@test.com',
            user_name='Test Hero',
            team='Test Team',
            total_points=500,
            rank=1
        )

    def test_leaderboard_creation(self):
        """Test that a leaderboard entry can be created"""
        self.assertEqual(self.entry.user_name, 'Test Hero')
        self.assertEqual(self.entry.total_points, 500)
        self.assertEqual(self.entry.rank, 1)


class WorkoutModelTest(TestCase):
    """Test cases for Workout model"""

    def setUp(self):
        self.workout = Workout.objects.create(
            title='Test Workout',
            description='A test workout routine',
            difficulty_level='Intermediate',
            duration=45,
            category='Cardio',
            recommended_for='All levels'
        )

    def test_workout_creation(self):
        """Test that a workout can be created"""
        self.assertEqual(self.workout.title, 'Test Workout')
        self.assertEqual(self.workout.difficulty_level, 'Intermediate')
        self.assertEqual(self.workout.duration, 45)


class UserAPITest(APITestCase):
    """Test cases for User API endpoints"""

    def setUp(self):
        self.user = User.objects.create(
            name='API Test Hero',
            email='api.test@test.com',
            team='API Test Team'
        )

    def test_get_users_list(self):
        """Test retrieving list of users"""
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        """Test creating a new user via API"""
        url = reverse('user-list')
        data = {
            'name': 'New Hero',
            'email': 'new.hero@test.com',
            'team': 'New Team'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TeamAPITest(APITestCase):
    """Test cases for Team API endpoints"""

    def setUp(self):
        self.team = Team.objects.create(
            name='API Test Team',
            description='Team for API testing'
        )

    def test_get_teams_list(self):
        """Test retrieving list of teams"""
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ActivityAPITest(APITestCase):
    """Test cases for Activity API endpoints"""

    def setUp(self):
        self.activity = Activity.objects.create(
            user_email='api.test@test.com',
            activity_type='cycling',
            duration=60,
            calories_burned=400,
            date=date.today()
        )

    def test_get_activities_list(self):
        """Test retrieving list of activities"""
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LeaderboardAPITest(APITestCase):
    """Test cases for Leaderboard API endpoints"""

    def setUp(self):
        self.entry = Leaderboard.objects.create(
            user_email='api.test@test.com',
            user_name='API Test Hero',
            team='API Test Team',
            total_points=750,
            rank=1
        )

    def test_get_leaderboard_list(self):
        """Test retrieving leaderboard"""
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    """Test cases for Workout API endpoints"""

    def setUp(self):
        self.workout = Workout.objects.create(
            title='API Test Workout',
            description='Workout for API testing',
            difficulty_level='Beginner',
            duration=30,
            category='Strength'
        )

    def test_get_workouts_list(self):
        """Test retrieving list of workouts"""
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class APIRootTest(APITestCase):
    """Test cases for API root endpoint"""

    def test_api_root(self):
        """Test that API root returns all endpoints"""
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
