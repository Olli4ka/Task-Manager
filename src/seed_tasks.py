import os
import django
import random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from app_taskmanager.models import Task


def run():
    TASKS_DATA = [
        (
            "Buy groceries",
            "Purchase milk, eggs, bread, fruits, and vegetables from the supermarket."
        ),
        (
            "Finish Django project",
            "Complete models, forms, views, and templates for the task manager application."
        ),
        (
            "Read Python documentation",
            "Study Django forms and validation in the official Python and Django documentation."
        ),
        (
            "Workout session",
            "Go to the gym for a one-hour strength and cardio training session."
        ),
        (
            "Clean the apartment",
            "Vacuum the floors, wash dishes, and organize the workspace."
        ),
        (
            "Prepare presentation",
            "Create slides for the upcoming team meeting about the new project."
        ),
        (
            "Call parents",
            "Have an evening video call with parents and discuss weekend plans."
        ),
        (
            "Update GitHub repository",
            "Push latest commits, update README, and organize project structure."
        ),
        (
            "Study SQL joins",
            "Practice INNER JOIN, LEFT JOIN, and aggregation queries using PostgreSQL."
        ),
        (
            "Write blog post",
            "Draft an article about learning Django and building first web applications."
        ),
    ]

    for title, description in TASKS_DATA:
        Task.objects.create(
            title=title,
            description=description,
            is_completed=random.choice([True, False])
        )

    print("✅ Seeding completed!")


if __name__ == "__main__":
    run()
