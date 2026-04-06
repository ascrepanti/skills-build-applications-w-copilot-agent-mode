from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]
        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert users
        users = [
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
            {"name": "Spider-Man", "email": "spiderman@marvel.com", "team": "Marvel"},
            {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
        ]
        db.users.insert_many(users)
        db.users.create_index("email", unique=True)

        # Insert teams
        teams = [
            {"name": "Marvel", "members": [u["email"] for u in users if u["team"] == "Marvel"]},
            {"name": "DC", "members": [u["email"] for u in users if u["team"] == "DC"]},
        ]
        db.teams.insert_many(teams)

        # Insert activities
        activities = [
            {"user": "ironman@marvel.com", "activity": "Running", "duration": 30},
            {"user": "cap@marvel.com", "activity": "Cycling", "duration": 45},
            {"user": "spiderman@marvel.com", "activity": "Swimming", "duration": 25},
            {"user": "superman@dc.com", "activity": "Flying", "duration": 60},
            {"user": "batman@dc.com", "activity": "Martial Arts", "duration": 40},
            {"user": "wonderwoman@dc.com", "activity": "Weightlifting", "duration": 35},
        ]
        db.activities.insert_many(activities)

        # Insert leaderboard
        leaderboard = [
            {"user": "ironman@marvel.com", "points": 100},
            {"user": "cap@marvel.com", "points": 90},
            {"user": "spiderman@marvel.com", "points": 80},
            {"user": "superman@dc.com", "points": 120},
            {"user": "batman@dc.com", "points": 110},
            {"user": "wonderwoman@dc.com", "points": 105},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Insert workouts
        workouts = [
            {"name": "Full Body", "exercises": ["Push-ups", "Squats", "Burpees"]},
            {"name": "Cardio Blast", "exercises": ["Running", "Cycling", "Jump Rope"]},
            {"name": "Strength", "exercises": ["Deadlift", "Bench Press", "Pull-ups"]},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
