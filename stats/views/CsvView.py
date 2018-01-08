from django.shortcuts import render, redirect

def upload(request):
    if request.method == 'POST':
        csv_file = request.FILES["csv_file"]
        
        
        return redirect('/stats/upload')
    else:
        return redirect('/stats/upload')
