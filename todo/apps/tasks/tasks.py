from celery import shared_task
from todo.celery import app

@app.task(bind=True)
def add(request, x, y):
    print("Task was called")
    with open(r"C:\MyWorks\web\todoList\celery.txt", "w") as f:
        f.write("Hello")
