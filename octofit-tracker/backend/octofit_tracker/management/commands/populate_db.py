from django.core.management.base import BaseCommand
from octofit_tracker.utils import get_mongo_db

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        db = get_mongo_db()

        # Populate users collection
        users = db.users
        users.insert_many([
            {"email": "user1@example.com", "name": "User One", "age": 20},
            {"email": "user2@example.com", "name": "User Two", "age": 22},
        ])

        # Populate teams collection
        teams = db.teams
        teams.insert_one({"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]})

        # Populate activities collection
        activities = db.activity
        activities.insert_many([
            {"user": "user1@example.com", "type": "Running", "duration": 30, "date": "2025-05-15"},
            {"user": "user2@example.com", "type": "Cycling", "duration": 45, "date": "2025-05-15"},
        ])

        # Populate leaderboard collection
        leaderboard = db.leaderboard
        leaderboard.insert_one({"team": "Team Alpha", "points": 100})

        # Populate workouts collection
        workouts = db.workouts
        workouts.insert_many([
            {"name": "Push-ups", "description": "Do 20 push-ups"},
            {"name": "Sit-ups", "description": "Do 30 sit-ups"},
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
