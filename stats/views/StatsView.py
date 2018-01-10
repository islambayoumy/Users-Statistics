from django.shortcuts import render, redirect
from stats import CsvController


def upload(request):
    if request.method == 'POST':
        csv_file = request.FILES["csv_file"]
        weekNumFrom = request.POST.get('weekNumFrom', '')
        weekNumTo = request.POST.get('weekNumTo', '')
        yearNum = request.POST.get('yearNum', '')
        
        exc = CsvController.CsvController(csv_file, weekNumFrom, weekNumTo, yearNum)
        exc.excuteCsv()
        
        return render(request, 'stats/data.html')
    else:
        return redirect('/stats/upload')
