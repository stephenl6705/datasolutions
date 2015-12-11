from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html', {
        'report_summary': request.POST.get('report', ''),
    })