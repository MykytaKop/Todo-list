from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.title


class Task(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self) -> str:
        return f"{self.content} {self.done} {self.created_time}"
