\# WareBot Healthcare AI — Model Card



\## 1. Model Overview



\*\*Project:\*\* WareBot Healthcare AI



\*\*Task:\*\* Healthcare text intent classification



\*\*Model:\*\* TF-IDF + Logistic Regression



\*\*Serving Layer:\*\* FastAPI



\*\*Purpose:\*\* The system classifies short healthcare-related text into predefined healthcare intent categories. It is an experimental NLP component for healthcare administration and prototyping.



This system is not intended to provide medical diagnosis, treatment recommendations, or clinical decisions.



\## 2. Intended Use



The model can be used for:



\* Healthcare text intent classification

\* Prototype healthcare NLP applications

\* Categorizing short patient-related queries

\* Demonstrating an API-based machine learning workflow



The model should not be used for:



\* Clinical diagnosis

\* Emergency medical decisions

\* Treatment recommendations

\* Patient risk assessment

\* Autonomous clinical decision-making



\## 3. Dataset



The project uses the provided synthetic healthcare datasets.



The labelled NLP dataset contains:



\* 42 labelled text samples

\* 6 intent categories

\* 7 samples per intent



The six intent categories are:



1\. fever

2\. malaria

3\. diabetes

4\. cold\_flu

5\. hypertension

6\. general\_query



The project also contains a synthetic healthcare symptoms dataset and healthcare test-case data.



No real patient data was intentionally used in the project.



\## 4. Data Preprocessing



The text classification pipeline uses:



\* Lowercase text processing

\* TF-IDF feature extraction

\* Unigram and bigram features

\* Stratified train/test splitting



The dataset was divided into:



\* 80% training data

\* 20% testing data



The split used `random\_state=42` for reproducibility.



\## 5. Model Architecture



```text

Healthcare Text

&#x20;      |

&#x20;      v

Text Preprocessing

&#x20;      |

&#x20;      v

TF-IDF Vectorization

&#x20;      |

&#x20;      v

Logistic Regression

&#x20;      |

&#x20;      v

Predicted Healthcare Intent

```



The trained TF-IDF vectorizer and Logistic Regression model are stored in the project `models` directory.



\## 6. Model Training



Two Logistic Regression configurations were evaluated using MLflow.



| Configuration   |   C | Max Iterations | Accuracy | Macro F1 |

| --------------- | --: | -------------: | -------: | -------: |

| Configuration 1 | 1.0 |           1000 |   55.56% |    0.478 |

| Configuration 2 | 0.1 |           1000 |   22.22% |    0.208 |



The best configuration was:



\* Logistic Regression

\* C = 1.0

\* max\_iter = 1000



The best configuration achieved:



\*\*Accuracy: 55.56%\*\*



\*\*Macro F1: 0.478\*\*



\## 7. API Deployment



The model is served using FastAPI.



\### Health Endpoint



```text

GET /

```



Example response:



```json

{

&#x20; "status": "healthy",

&#x20; "service": "WareBot Healthcare AI"

}

```



\### Prediction Endpoint



```text

POST /predict

```



Example request:



```json

{

&#x20; "text": "I have high temperature"

}

```



The API returns the submitted text and predicted healthcare intent.



\## 8. Testing



Three integration tests were implemented:



1\. Health check

2\. Prediction endpoint

3\. Empty text handling



Test result:



\*\*3 tests passed\*\*



A 50-concurrent-request load test was



