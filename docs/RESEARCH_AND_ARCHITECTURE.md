\# WareBot Healthcare AI



\## Milestone 1 — Research + Architecture Design



\### Project Objective



The goal of this project is to build a clinical note summarization pipeline for healthcare administration.



The system will accept a doctor voice transcript as text and:



1\. Extract diagnosis information.

2\. Extract medication information.

3\. Extract follow-up information.

4\. Convert the extracted information into structured JSON.

5\. Generate a concise summary for the patient record using an LLM.

6\. Evaluate the pipeline using the provided 30 test cases.



No real patient data will be used.



\---



\## 1. Research Review



\### Research 1 — Clinical Named Entity Recognition



\*\*Source:\*\* Systematic review of clinical Natural Language Processing and Named Entity Recognition research.



Clinical NER research commonly identifies medical entities such as problems, tests, treatments, medications, and other clinical concepts.



\*\*Relevance to this project:\*\*



The WareBot system needs to identify important clinical entities from doctor transcripts. The project will focus on three custom entity categories:



\* DIAGNOSIS

\* MEDICATION

\* FOLLOW\_UP



\*\*Key takeaway:\*\*



Clinical NER is suitable for converting unstructured clinical text into structured medical information.



\---



\### Research 2 — Large Language Models for Clinical Text Summarization



\*\*Source:\*\* Research on Large Language Models for clinical text summarization.



Large language models can be used to summarize clinical conversations and medical documentation. However, clinical summarization requires attention to correctness, completeness, and avoidance of unsupported information.



\*\*Relevance to this project:\*\*



After extracting structured clinical information, an LLM will generate a concise summary suitable for a patient record.



\*\*Key takeaway:\*\*



LLM summarization can reduce lengthy clinical text while preserving important information, but the output must be evaluated for factual consistency.



\---



\### Research 3 — spaCy EntityRecognizer



\*\*Source:\*\* Official spaCy EntityRecognizer documentation.



spaCy provides a trainable Named Entity Recognition component that identifies labelled spans of text and stores recognized entities in the document.



\*\*Relevance to this project:\*\*



spaCy will be used to develop the custom NER component for:



\* Diagnosis

\* Medication

\* Follow-up



\*\*Key takeaway:\*\*



spaCy provides a practical framework for training and evaluating a custom NER model using labelled examples.



\---



\## 2. Proposed System Architecture



```text

Doctor Voice Transcript

&#x20;         |

&#x20;         v

&#x20;    Text Input

&#x20;         |

&#x20;         v

&#x20; Text Preprocessing

&#x20;         |

&#x20;         v

&#x20;  Custom spaCy NER

&#x20;         |

&#x20;         +----------------------+

&#x20;         |          |           |

&#x20;         v          v           v

&#x20;     Diagnosis  Medication   Follow-up

&#x20;         |          |           |

&#x20;         +----------+-----------+

&#x20;                    |

&#x20;                    v

&#x20;            Structured JSON

&#x20;                    |

&#x20;                    v

&#x20;             LLM Summarizer

&#x20;                    |

&#x20;                    v

&#x20;         Patient Record Summary

&#x20;                    |

&#x20;                    v

&#x20;         Evaluation on 30 Notes

```



\---



\## 3. Main Components



\### 3.1 Input Layer



The system accepts doctor voice transcripts as text.



The initial project implementation will use text transcripts rather than direct speech-to-text processing.



\### 3.2 Text Preprocessing



The preprocessing stage will:



\* Normalize text.

\* Remove unnecessary whitespace.

\* Preserve clinically meaningful words.

\* Prepare text for the NER model.



\### 3.3 Custom NER



A custom spaCy NER model will identify:



```text

DIAGNOSIS

MEDICATION

FOLLOW\_UP

```



Example:



```text

Patient has diabetes and hypertension.

Started metformin 500 mg.

Follow up after two weeks.

```



Expected extraction:



```json

{

&#x20; "diagnosis": \[

&#x20;   "diabetes",

&#x20;   "hypertension"

&#x20; ],

&#x20; "medication": \[

&#x20;   "metformin 500 mg"

&#x20; ],

&#x20; "follow\_up": \[

&#x20;   "after two weeks"

&#x20; ]

}

```



\### 3.4 Structured JSON



The extracted entities will be converted into a consistent JSON structure.



Target format:



```json

{

&#x20; "diagnosis": \[],

&#x20; "medications": \[],

&#x20; "follow\_up": \[]

}

```



\### 3.5 LLM Summarization



The structured information and relevant transcript information will be provided to an LLM to generate a concise clinical summary.



The summary should:



\* Preserve important clinical information.

\* Avoid inventing facts.

\* Avoid adding unsupported diagnoses or medications.

\* Remain concise.

\* Be suitable for a patient record.



\### 3.6 Evaluation



The final pipeline will be evaluated using the provided 30 test notes.



\---



\## 4. Evaluation Metrics



\### NER Precision



Measures how many extracted entities are correct.



```text

Precision = Correct Extracted Entities / Total Extracted Entities

```



\### NER Recall



Measures how many of the expected entities were successfully extracted.



```text

Recall = Correct Extracted Entities / Total Expected Entities

```



\### NER F1-score



Combines precision and recall.



```text

F1 = 2 × Precision × Recall / (Precision + Recall)

```



\### JSON Extraction Accuracy



Checks whether diagnosis, medication, and follow-up information is correctly represented in the required JSON structure.



\### Summary Quality



The generated summaries will be checked for:



\* Factual consistency

\* Completeness

\* Relevance

\* Conciseness

\* Unsupported information / hallucination



\### Test Case Success Rate



The final system will be tested against all 30 provided clinical test notes.



Target:



```text

30 / 30 test notes processed successfully

```



\---



\## 5. Data Sources



The project uses the following provided synthetic/client data packs:



\### Healthcare Symptoms Dataset



```text

aiml\_healthcare\_symptoms.csv

```



Shape:



```text

800 records × 17 columns

```



The dataset contains synthetic healthcare-related features including symptoms, vital measurements, and diagnosis.



\### Healthcare Test Cases



```text

aiml\_healthcare\_test\_cases.txt

```



Contains predefined validation and evaluation cases.



\### Labelled Samples



```text

aiml\_labelled\_samples.json

```



Contains:



```text

42 labelled samples

6 intents

```



The six intents are:



\* fever

\* malaria

\* diabetes

\* cold\_flu

\* hypertension

\* general\_query



These labelled samples will be inspected before deciding how they can support the NLP pipeline.



\---



\## 6. Data Privacy and Safety



Only the provided project data and synthetic examples will be used.



No real patient information will be uploaded or stored.



The system is intended as a clinical administration and summarization prototype, not as a replacement for medical professionals or clinical decision-making.



Generated summaries must be reviewed for factual correctness before being considered suitable for a patient record.



\---



\## 7. Initial Technology Stack



The planned technology stack is:



\* Python 3.11

\* spaCy

\* Natural Language Processing

\* LLM

\* pandas

\* JSON

\* Git

\* GitHub

\* Jupyter / VS Code



Additional libraries will be added only when required by the implementation.



\---



\## 8. Development Plan



\### Week 1



\* Research relevant clinical NLP approaches.

\* Inspect provided datasets.

\* Finalize architecture.

\* Create repository.

\* Create data pipeline skeleton.



\### Week 2–3



\* Prepare labelled NER data.

\* Build preprocessing pipeli



