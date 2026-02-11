from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.IntegerField()
    date = models.DateField()
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'activities'
        verbose_name_plural = 'activities'

    def __str__(self):
        return f"{self.user_email} - {self.activity_type}"


class Leaderboard(models.Model):
    user_email = models.EmailField()
    user_name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    total_points = models.IntegerField()
    rank = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank']

    def __str__(self):
        return f"{self.rank}. {self.user_name} - {self.total_points} points"


class Workout(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty_level = models.CharField(max_length=20)
    duration = models.IntegerField()  # in minutes
    category = models.CharField(max_length=50)
    recommended_for = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.title
