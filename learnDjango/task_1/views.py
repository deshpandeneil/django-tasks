from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    numList = [i for i in range(1, 21)]
    params = {'numbers': numList}
    return render(request, 'task_1/index.html', params)


def result(request):
    start = request.POST.get('start')
    end = request.POST.get('end')
    if (start > end):
        return render(request, 'task_1/error.html')
    numList = []
    for i in range(int(start), int(end) + 1):
        numList.append(i)
    params = {'result': numList}
    return render(request, 'task_1/result.html', params)
