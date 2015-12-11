from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html', {
        'topic_summary': request.POST.get('topic', ''),
    })