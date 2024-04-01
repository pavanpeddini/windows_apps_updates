# ai_algorithms.py
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

class AIModel:
    def __init__(self):
        self.model = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', RandomForestClassifier())
        ])

    def train_model(self, data, labels):
        """
        Function to train the AI model using historical data.
        
        Parameters:
        - data: Historical data used for training the AI model.
        - labels: Target labels for the data.
        
        Returns:
        - trained_model: Trained AI model.
        """
        self.model.fit(data, labels)
        print("AI model trained successfully")

    def predict(self, user_features):
        """
        Function to predict personalized notifications using the trained AI model.
        
        Parameters:
        - user_features: Features of the user for prediction.
        
        Returns:
        - personalized_notification: Personalized notification for the user.
        """
        personalized_notification = self.model.predict([user_features])
        print("Notification predicted successfully")
        return personalized_notification
