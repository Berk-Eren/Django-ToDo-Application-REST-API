from celery import shared_task


@shared_task
def add(request, x, y):
    print("Task was called")
    with open(r"C:\MyWorks\web\todoList\celery.txt", "w") as f:
        f.write("Hello")
