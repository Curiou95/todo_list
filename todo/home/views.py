from django.shortcuts import render
from .models import To_do

# Create your views here.

def home_page(request):
    if request.method == 'POST':
        new_task = request.POST['newtask']
        add_task = To_do(task = new_task)
        add_task.save()
    
        # print(task)
        # print(request.POST)
    all_todo = To_do.objects.all()
    context = {
            "all_todo": all_todo,
    }
    return render(request, 'index.html', context)