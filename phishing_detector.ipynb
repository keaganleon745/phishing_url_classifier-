import pandas as pd
import numpy as np
import re
import tldextract
import matplotlib.pyplot as plt
import warnings
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

warnings.filterwarnings('ignore')

# Load the dataset (adjust file name if needed)
df = pd.read_csv('phishing_site_urls.csv')  # CSV must have 'URL' and 'Label' columns
df.head()

# Extracts features from a URL string
def extract_features(url):
    extracted = tldextract.extract(url) # Separates subdomain, domain, and suffix
    return {
        'url_length': len(url),
        'has_ip': 1 if re.search(r'(\d{1,3}\.){3}\d{1,3}', url) else 0, # Checks for IP address in URL
        'has_at': 1 if '@' in url else 0, # Checks if "@" is used (phishing trick)
        'count_dots': url.count('.'), # Total dots can indicate subdomain misuse
        'is_https': 1 if url.startswith('https') else 0, # HTTPS is a good sign
        'tld': extracted.suffix # Extract top-level domain ("com", "org")
    }

# Apply feature extraction to each URL
features = df['URL'].apply(extract_features)
X = pd.DataFrame(features.tolist())

# One-hot encode TLDs (top-level domains)
X = pd.get_dummies(X, columns=['tld'])

# Convert target labels to binary values
y = df['Label'].map({'phishing': 1, 'legitimate': 0})

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate performance
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Visualize
importances = model.feature_importances_
indices = np.argsort(importances)[::-1] # Sort by importance (descending)
feature_names = X.columns

plt.figure(figsize=(12, 5))
plt.title("Feature Importance")
plt.bar(range(X.shape[1]), importances[indices])
plt.xticks(range(X.shape[1]), feature_names[indices], rotation=90)
plt.tight_layout()
plt.show()
