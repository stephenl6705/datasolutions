from reports.models import Topic
from django.shortcuts import render, redirect

def home_page(request):
    if request.method == 'POST':
        topic_title = request.POST['topic']
        found = False
        for topic in Topic.objects.all():
            if topic.title == topic_title:
                topic.selected = True
                topic.save()
                found = True
        if found == True:
            for topic in Topic.objects.all():
                if topic.title != topic_title:
                    topic.selected = False
                    topic.save()
        return redirect('/')

    topic_title = ''
    topic_text = ''
    for topic in Topic.objects.all():
        if topic.selected:
            topic_title = topic.title
            topic_text = topic.text
            break

    return render(request, 'home.html', {
        'topic_summary': topic_title,
        'topic_text': topic_text,
    })