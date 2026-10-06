\# Checkpoint 4 - Integration and Load Testing Report



\## 1. Objective



The objective of this checkpoint was to integrate the healthcare text classification model into a serving layer, create integration tests, and evaluate the API under 50 concurrent requests.



\## 2. Serving Layer



The trained healthcare text classification model was integrated into a FastAPI application.



The API provides:



\- GET `/` - health check endpoint

\- POST `/predict` - healthcare text intent prediction endpoint



The API loads the trained TF-IDF vectorizer and Logistic Regression model from the project models directory.



\## 3. API Integration



The prediction endpoint accepts healthcare text in JSON format.



Example request:



```json

{

&#x20; "text": "I have high temperature"

}

