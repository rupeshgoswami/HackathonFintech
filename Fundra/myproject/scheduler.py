# scheduler.py

import os
import django
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management import call_command
from threading import Thread

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

def update_sentiment():
    call_command('update_sentiment')

scheduler = BackgroundScheduler()
scheduler.add_job(update_sentiment, 'interval', minutes=1)
scheduler.start()

# Function to keep the main thread alive
def keep_alive():
    import time
    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

# Run keep_alive in a separate thread
Thread(target=keep_alive, daemon=True).start()
