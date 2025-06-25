import pandas as pd
import numpy as np
import re
import tldextract
import matplotlib.pyplot as plt
import warnings
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Suppress warnings
warnings.filterwarnings('ignore')


def extract_features(url):
    extracted = tldextract.extract(url)
    return {
        'url_length': len(url),
        'has_ip': 1 if re.search(r'(\d{1,3}\.){3}\d{1,3}', url) else 0,
        'has_at': 1 if '@' in url else 0,
        'count_dots': url.count('.'),
        'is_https': 1 if url.startswith('https') else 0,
        'tld': extracted.suffix
    }


def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        if 'URL' not in df.columns or 'Label' not in df.columns:
            raise ValueError("Dataset must contain 'URL' and 'Label' columns.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit()
    except Exception as e:
        print(f"Error loading data: {e}")
        exit()


def preprocess_data(df):
    features = df['URL'].apply(extract_features)
    X = pd.DataFrame(features.tolist())
    X = pd.get_dummies(X, columns=['tld'])

    df['Label'] = df['Label'].astype(str).str.lower().str.strip()
    label_map = {'bad': 1, 'good': 0}  # Adjust based on your dataset
    y = df['Label'].map(label_map)

    valid_rows = y.notna()
    X = X.loc[valid_rows]
    y = y.loc[valid_rows].astype(int)

    print("\nValid labels:", y.value_counts(dropna=False))
    return train_test_split(X, y, test_size=0.2, random_state=42), X.columns


def train_and_evaluate(X_train, X_test, y_train, y_test):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    return model


def plot_feature_importance(model, feature_names):
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]

    plt.figure(figsize=(12, 5))
    plt.title("Feature Importance")
    plt.bar(range(len(feature_names)), importances[indices])
    plt.xticks(range(len(feature_names)), feature_names[indices], rotation=90)
    plt.tight_layout()
    plt.show()
