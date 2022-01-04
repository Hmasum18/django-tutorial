from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse


class NewTaskForm(forms.Form):
    newTask = forms.CharField(label="new task")

# Create your views here.
# a empty list of task

# session_task_list = []

def index(req):
    # session_task_list is the list vairable name for the task
    # check if there is already a session_task_list is this session
    if "session_task_list" not in req.session: # if user enter in a new session
        req.session["session_task_list"] = []

    return render(req, 'tasks/index.html', {
        # 'task_list': session_task_list,
        # task_list is the session_task_list for index.html file
        'task_list': req.session["session_task_list"],
    })


def add_task(req):
    if req.method == "POST": # if user submit a new task from the form using POST request
        tempForm = NewTaskForm(req.POST)
        if tempForm.is_valid():
            tempTask = tempForm.cleaned_data["newTask"]  #  get data from  'newTask'  CharField of  NewTaskForm ( here tempForm )
            req.session["session_task_list"] += [tempTask]  # add new task as list in session task list
            # go to index page to show the list of task
            # give the name of the url and then reverse function will reverse engineer and find the url
            return HttpResponseRedirect(reverse("tasks:index"))  # after adding a new task go to index.html page
        else:  # if user didn't submit any new task by the form
            # go to add_task page again to input a task by the html form
            return render(req, "tasks/add_task.html", {
                "task_form": tempForm,
            })

    return render(req, 'tasks/add_task.html',
                  {
                      "task_form": NewTaskForm(),
                  })
