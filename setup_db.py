#!/usr/bin/env python
import os

#user = "langestrst01"
#project = "datasolutions"

def setup_topics():
    #site_folder = '/home/%s/%s/' % (user, project)
    #run('cd %s' % (site_folder,))
    #run('rm db.sqlite3')
    #run('python3 manage.py migrate --noinput')
    Topic.objects.create(title='CCI C-Suite', text='CCI Suite Text', selected=True)
    Topic.objects.create(title='CCI Dashboard', text='CCI Dashboard Text', selected=False)

if __name__ == "__main__":

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datasolutions.settings")

    from reports.models import Topic
    #from fabric.api import run

    setup_topics()
