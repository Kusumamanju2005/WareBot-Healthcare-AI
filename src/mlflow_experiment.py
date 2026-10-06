import json
from pathlib import Path

import mlflow
import mlflow.sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "aiml_labelled_samples.json"


def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    texts = [item["text"] for item in data]
    labels = [item["intent"] for item in data]

    return texts, labels


def train_and_log(X_train, X_test, y_train, y_test, config_name, C, max_iter):
    vectorizer = TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
    )

    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    model = LogisticRegression(
        C=C,
        max_iter=max_iter,
        random_state=42,
    )

    with mlflow.start_run(run_name=config_name):
        model.fit(X_train_tfidf, y_train)

        predictions = model.predict(X_test_tfidf)

        accuracy = accuracy_score(y_test, predictions)
        f1 = f1_score(y_test, predictions, average="macro")

        mlflow.log_param("model", "LogisticRegression")
        mlflow.log_param("C", C)
        mlflow.log_param("max_iter", max_iter)
        mlflow.log_param("vectorizer", "TF-IDF")
        mlflow.log_param("ngram_range", "(1,2)")

        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("macro_f1", f1)

        mlflow.sklearn.log_model(model, "model")

        print(f"{config_name}")
        print(f"  C = {C}")
        print(f"  max_iter = {max_iter}")
        print(f"  Accuracy = {accuracy:.4f}")
        print(f"  Macro F1 = {f1:.4f}")
        print()

    return accuracy, f1


def main():
    texts, labels = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        texts,
        labels,
        test_size=0.2,
        random_state=42,
        stratify=labels,
    )

    mlflow.set_experiment("WareBot_Healthcare_AI")

    configurations = [
        ("config_1", 1.0, 1000),
        ("config_2", 0.1, 1000),
    ]

    results = []

    for config_name, C, max_iter in configurations:
        accuracy, f1 = train_and_log(
            X_train,
            X_test,
            y_train,
            y_test,
            config_name,
            C,
            max_iter,
        )

        results.append(
            {
                "config": config_name,
                "C": C,
                "max_iter": max_iter,
                "accuracy": accuracy,
                "macro_f1": f1,
            }
        )

    best = max(results, key=lambda x: x["macro_f1"])

    print("=" * 50)
    print("BEST CONFIGURATION")
    print("=" * 50)
    print(best)


if __name__ == "__main__":
    main()