from __future__ import absolute_import
from celery import Celery
app = Celery('test_celery',
             broker='amqp://admin:admin@10.122.18.20:5672/storageBackup',
             backend='amqp://admin:admin@10.122.18.20:5672/storageBackup',
             include=['test_celery.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
    task_routes = {
        'proj.tasks.add': {'queue': 'hipri'},
    },
)

