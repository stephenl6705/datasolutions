from reports.models import Topic
from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from reports.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        Topic.objects.create(title='CCI Suite', text='CCI Suite Text', selected=True)
        Topic.objects.create(title='CCI Dashboard', text='CCI Dashboard Text', selected=False)

        request = HttpRequest()
        request.method = 'POST'
        request.POST['topic'] = 'CCI Dashboard'

        response = home_page(request)

        topic = Topic.objects.all()[1]
        self.assertEqual(topic.selected, True)

    def test_home_page_redirects_after_POST(self):
        Topic.objects.create(title='CCI Suite', text='CCI Suite Text', selected=True)
        Topic.objects.create(title='CCI Dashboard', text='CCI Dashboard Text', selected=False)

        request = HttpRequest()
        request.method = 'POST'
        request.POST['topic'] = 'CCI Dashboard'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_home_page_only_changes_report_when_exists(self):
        Topic.objects.create(title='CCI Suite', text='CCI Suite Text', selected=True)
        Topic.objects.create(title='CCI Dashboard', text='CCI Dashboard Text', selected=False)

        request = HttpRequest()
        request.method = 'POST'
        request.POST['topic'] = 'Worldbank'

        home_page(request)

        topic = Topic.objects.all()[0]
        self.assertEqual(topic.selected, True)

    def test_home_page_displays_selected_topic_info(self):
        Topic.objects.create(title='CCI Suite', text='CCI Suite Text', selected=True)
        Topic.objects.create(title='CCI Dashboard', text='CCI Dashboard Text', selected=False)

        request = HttpRequest()
        response = home_page(request)

        self.assertIn('CCI Suite Text', response.content.decode())


class TopicModelTest(TestCase):

    def test_saving_and_retrieving_topics(self):

        first_topic = Topic()
        first_topic.text = 'The first (ever) report topic'
        first_topic.save()

        second_topic = Topic()
        second_topic.text = "Topic the second"
        second_topic.save()

        saved_topics = Topic.objects.all()
        self.assertEqual(saved_topics.count(), 2)

        first_saved_topic = saved_topics[0]
        second_saved_topic = saved_topics[1]
        self.assertEqual(first_saved_topic.text, 'The first (ever) report topic')
        self.assertEqual(second_saved_topic.text, 'Topic the second')
