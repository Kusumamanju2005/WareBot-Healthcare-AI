\# Baseline Model Report



\## 1. Objective



The objective of this baseline experiment is to establish an initial benchmark for healthcare-related text intent classification before applying more advanced NLP techniques.



\## 2. Dataset



The provided labelled dataset contains 42 healthcare text samples across six intent categories:



\- fever

\- malaria

\- diabetes

\- cold\_flu

\- hypertension

\- general\_query



The dataset contains three fields:



\- text

\- intent

\- confidence



\## 3. Preprocessing



The text data was converted into numerical features using TF-IDF vectorization.



The vectorizer used:



\- Lowercase text processing

\- Unigrams and bigrams

\- TF-IDF feature representation



The dataset was divided into:



\- Training: 80%

\- Testing: 20%



A fixed random state of 42 was used for reproducibility.



\## 4. Baseline Model



A Logistic Regression classifier was used as the baseline machine learning model.



The trained model and TF-IDF vectorizer were saved in the `models/` directory.



\## 5. Evaluation Results



| Metric | Result |

|---|---:|

| Test samples | 9 |

| Accuracy | 0.56 |

| Macro F1-score | 0.48 |

| Weighted F1-score | 0.48 |



\### Classification Results



The baseline model achieved an overall accuracy of approximately \*\*56%\*\* on the test set.



The classification results show that performance varies between intent categories. This is expected because the dataset is very small, with only 42 labelled samples.



\## 6. Benchmark



The baseline accuracy of \*\*56%\*\* will be used as the initial benchmark.



Future improvements can be compared against this result using the same evaluation methodology.



\## 7. Limitations



The baseline dataset is small, containing only 42 samples. Therefore, the evaluation result should not be considered representative of real-world clinical performance.



The dataset is also intent-labelled rather than entity-labelled. Therefore, this baseline does not evaluate clinical NER extraction of diagnosis, medication, or follow-up information.



\## 8. Next Steps



Future work will focus on:



1\. Improving healthcare text preprocessing.

2\. Developing custom clinical NER.

3\. Extracting diagnosis, medication, and follow-up information.

4\. Producing structured JSON output.

5\. Evaluating the complete clinical note processing pipeline.

6\. Comparing improved approaches against the 56% baseline.

