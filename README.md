# ToDo Application
 
This is a project to create a backend for ToDo application using Django REST Framework.

- Models to be created
    - Task
        - Name
        - Description
        - Comment
        - Reporter (User)
        - Assigned to (User)
        - Sprint (*ForeignKey*)
    - User
    - Sprint
        - Name (*automatic*) - index
        - Epic (*ForeignKey*)
    - Epic
        - Name - index
        - List of tasks
    - Comment
        - commented_by (User)