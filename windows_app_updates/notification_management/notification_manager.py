
import requests
import json
import sqlite3
from ai_algorithms import AIModel

class Notification:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NotificationManager:
    def __init__(self):
        self.notifications = []
        self.db_connection = sqlite3.connect('notification_data.db')
        self.create_notification_table()
        self.ai_model = AIModel()

    def create_notification_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS notifications
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           title TEXT,
                           content TEXT)''')
        self.db_connection.commit()

    def send_notification(self, notification):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO notifications (title, content) VALUES (?, ?)", (notification.title, notification.content))
            self.db_connection.commit()
            self.notifications.append(notification)
        except sqlite3.Error as e:
            print("Error occurred while sending notification:", e)

    def customize_preferences(self, user, frequency, content_types, delivery_method):
        user.preferences = {
            'frequency': frequency,
            'content_types': content_types,
            'delivery_method': delivery_method
        }

    def personalize_message(self, user, app_name, update_info):
        if 'productivity' in user.preferences['content_types'] and app_name == 'Microsoft Office':
            message = f"New update for {app_name} available: {update_info}"
            personalized_notification = self.ai_model.predict(message)
            self.send_notification(Notification("Update Available", personalized_notification))

    def collect_feedback(self, user, notification, feedback):
        if feedback == 'not interested':
            # Adjust algorithm to prioritize relevant notifications
            pass

    def fetch_external_data(self, app_store_url):
        try:
            response = requests.get(app_store_url)
            if response.status_code == 200:
                return json.loads(response.text)
            else:
                print("Failed to fetch data from app store API:", response.text)
                return None
        except requests.exceptions.RequestException as e:
            print("Error occurred during API call:", e)
            return None