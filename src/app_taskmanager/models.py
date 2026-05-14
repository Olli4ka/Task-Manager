from django.db import models

class Task(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Task name"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Task description"
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name="Completed?"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creation date"
    )

    def __str__(self):
        return self.title
