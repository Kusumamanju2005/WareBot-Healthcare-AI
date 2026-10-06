\# Checkpoint 3 - Core Model Experiment Report



\## 1. Objective



The objective of this experiment was to train the primary healthcare text classification model using multiple hyperparameter configurations and track the experiments using MLflow.



\## 2. Primary Model



The primary model used was Logistic Regression with TF-IDF text features.



The dataset was split using:



\- 80% training data

\- 20% testing data

\- Random state: 42

\- Stratified split



\## 3. Experiment Configurations



Two Logistic Regression configurations were evaluated.



| Configuration | C | max\_iter | Accuracy | Macro F1 |

|---|---:|---:|---:|---:|

| Config 1 | 1.0 | 1000 | 55.56% | 0.478 |

| Config 2 | 0.1 | 1000 | 22.22% | 0.208 |



\## 4. Best Configuration



The best configuration was:



\- Model: Logistic Regression

\- C: 1.0

\- max\_iter: 1000

\- Vectorizer: TF-IDF

\- ngram range: (1, 2)

\- Accuracy: 55.56%

\- Macro F1: 0.478



The best configuration was selected based on Macro F1 score.



\## 5. Experiment Tracking



Experiments were tracked using MLflow under the experiment:



`WareBot\_Healthcare\_AI`



The following parameters and metrics were logged:



\- Model type

\- C value

\- max\_iter

\- TF-IDF configuration

\- Accuracy

\- Macro F1



The trained model was also logged as an MLflow artifact.



\## 6. Conclusion



Configuration 1 performed substantially better than Configuration 2 on the test set.



Configuration 1 achieved 55.56% accuracy and a Macro F1 score of 0.478, while Configuration 2 achieved 22.22% accuracy and a Macro F1 score of 0.208.



Therefore, Configuration 1 (`C=1.0`) is selected as the current best configuration.



\## 7. Limitations



The dataset contains only 42 labelled samples, resulting in a very small test set of 9 samples. Therefore, these results should be considered an experimental benchmark rather than evidence of clinical performance.



Further experimentation with more representative labelled data is required.

