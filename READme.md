##task_list.html is like a homepage with a redirect link of the add_task on it to allow user add and view task. , inside task_list.html line 18 is a loop example in django templating. {% for task in tasks %} in Django's templating language is a loop, much like a for loop in Python. It iterates over each task in the tasks queryset that was passed from the view to the template.

##The add_task.html template in your project serves as the form page where users can input details for a new task to add to the to-do list.

##Purpose of add_task.html
The purpose of add_task.html is to provide a user interface for submitting a new task. When users navigate to the "Add Task" link in task_list.html, they’re directed to add_task.html where they can fill in the task details.

# step 1:

Create the To-Do Model

# step 2:

Create Views and Templates

# Forms:

Create a forms.py in the todo app for handling form submissions:

# Step 7:

Create Templates, Create a folder named templates inside the todo app folder. Inside templates, create a todo folder for your HTML files.

# Step 8: Set Up URLs

In urls.py of the todo app, create URL patterns:

# step 9: In the urls.py of the project, include the todo app URLs:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('todo.urls')),
]


# the differences between Django’s template-based loop and a standard Python for loop

In Django:

The for loop in task_list.html is not a standalone Python loop but part of the template language, which is used to dynamically render HTML by looping through data passed from the view.
tasks isn’t globally defined. Instead, each time task_list is requested, tasks is redefined and retrieved from the database, allowing the HTML to display current task data.
In standalone Python, like your code example for calculating averages:

You define a list (user_scores = [85, 92, ...]), calculate total and average values, and then print them directly.
This process is entirely within one script, with all data and operations contained in the same place.
4. How Django’s template loop and the Python loop differ
Your standalone Python example calculates a total and average score using a for loop that iterates through a list (user_scores). This for loop:

Directly accesses user_scores, which was explicitly defined.
Uses Python’s built-in print() function to display output.
In Django’s case:

The for loop is within a template file (task_list.html) and iterates over tasks, which the view has dynamically retrieved from the database.
The for loop generates HTML rather than direct output, making a dynamic web page.
Summary of What’s Different
Location of Logic: In Django, logic is split between views (where data is fetched) and templates (where data is displayed).
Data Source: Django’s data (like tasks) is usually stored in a database and retrieved as needed, while standalone Python scripts typically use directly defined data.
Output Type: Django’s for loop renders HTML instead of displaying text output via print().
Why the Difference Exists
Django separates data handling (views) from presentation (templates) to support cleaner, reusable, and maintainable code for web applications. This is different from self-contained Python scripts, which are generally simpler and don’t need to support dynamic web pages.


