import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")

app = Celery("todo", broker="redis://127.0.0.1:6379/")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
