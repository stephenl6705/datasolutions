from reports.models import Topic
from django.shortcuts import render

def home_page(request):
    topic_title = ''
    topic_text = ''
    if request.method == 'POST':
        topic_title = request.POST['topic']
        for topic in Topic.objects.all():
            if topic.title == topic_title:
                topic_text = topic.text

    return render(request, 'home.html', {
        'topic_summary': topic_title,
        'topic_text': topic_text,
    })