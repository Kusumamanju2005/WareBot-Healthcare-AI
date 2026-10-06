import json
from pathlib import Path

import pandas as pd


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_symptoms():
    """Load the synthetic healthcare symptoms dataset."""
    path = DATA_DIR / "aiml_healthcare_symptoms.csv"
    return pd.read_csv(path)


def load_test_cases():
    """Load the provided healthcare test cases."""
    path = DATA_DIR / "aiml_healthcare_test_cases.txt"
    return path.read_text(encoding="utf-8")


def load_labelled_samples():
    """Load labelled NLP samples."""
    path = DATA_DIR / "aiml_labelled_samples.json"

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    symptoms = load_symptoms()
    test_cases = load_test_cases()
    labelled_samples = load_labelled_samples()

    print("Healthcare Symptoms:", symptoms.shape)
    print("Test Cases Loaded:", len(test_cases.splitlines()))
    print("Labelled Samples:", len(labelled_samples))


if __name__ == "__main__":
    main()