from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskDetails

# Create your views here.
def home_view(request):
    incomplete_task = TaskDetails.objects.filter(Task_status=False)
    complete_task = TaskDetails.objects.filter(Task_status=True)
    len_incomplete_task = len(incomplete_task)
    len_complete_task = len(complete_task)
    total_no_task = TaskDetails.objects.all().count()

    context = {
        'incomplete_task': incomplete_task,
        'complete_task': complete_task,
        'len_incomplete_task': len_incomplete_task,
        'len_complete_task': len_complete_task,
        'total_no_task': total_no_task,
        'total_no_incompleted_task': len_incomplete_task,
        'total_no_complete_task': len_incomplete_task,
    }
    return render(request, 'Taskapp/home.html', context)


def add_task_view(request):
    if request.method == 'POST':
        task_name = request.POST.get('add_task', '')
        TaskDetails.objects.create(Task_name=task_name, Task_status=False)
        return redirect('home')

def task_done_view(request, id):
    record = get_object_or_404(TaskDetails, id=id)
    record.Task_status = True
    record.save()
    return redirect('home')


def task_undo_view(request, id):
    record = get_object_or_404(TaskDetails, id=id)
    record.Task_status = False
    record.save()
    return redirect('home')

def task_delete_view(request, id):
    record = get_object_or_404(TaskDetails, id=id)
    record.delete()
    return redirect('home')

def delete_all_view(request):
    incomplete_task = TaskDetails.objects.filter(Task_status=False)
    incomplete_task.delete()
    return redirect('home')

def clear_all_view(request):
    complete_task = TaskDetails.objects.filter(Task_status=True)
    complete_task.delete()
    return redirect('home')

def remove_all_view(request):
    all_records = TaskDetails.objects.all()
    all_records.delete()
    return redirect('home')

def update_task_view(request, id):
    record = get_object_or_404(TaskDetails, id=id)
    if request.method == 'POST':
        updated_task = request.POST.get('update_task', '')
        record.Task_name = updated_task  
        record.Task_status = True  
        record.save()
        return redirect('home')
    else:
        context = {
            'Task_name': record.Task_name,
            'id': record.id,
        }
        return render(request, 'Taskapp/update.html', context)
