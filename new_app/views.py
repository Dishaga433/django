from django.shortcuts import render

from new_app.form import TodoForm


# Create your views here.
# def text(request):
#     return render(request,"text.html")

def tem(request):
    return render(request,"index.html")

def dashboard(request):
    return render(request,"index_dashboard.html")

def dashboard2(request):
    return render(request,"dashboard2.html")

def text(request):

    data =TodoForm()
    if request.method == "POST":
        todo = TodoForm(request.POST)
        if todo.is_valid():
            todo.save()
    return render(request,"text.html",{"form":data})