# Phishing URL Classifier with Python

This project is a simple machine learning tool to classify URLs as **phishing** or **legitimate** using basic features extracted from the URL string itself.

It uses **Python**, **scikit-learn**, and a public dataset from sources like [PhishTank](https://www.phishtank.com/) or [Kaggle](https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls?resource=download).

---

## Why This Project?

Phishing is one of the most common and effective attack vectors in cybersecurity. This project shows how machine learning (ML) can be applied to detect phishing attempts using features that can be derived without visiting the webpage.

---

## Features Used

- URL length
- Presence of IP address
- Use of `@` symbol
- Number of dots in the URL
- Top-level domain (TLD)
- HTTPS usage

These features help the model distinguish suspicious URLs from legitimate ones.

---

## Tools and Libraries

| Library          | Purpose                                                                          |
| ---------------- | -------------------------------------------------------------------------------- |
| **Python 3.x**   | The main programming language used for building and running the script           |
| **pandas**       | For loading, exploring, and manipulating the phishing dataset                    |
| **numpy**        | Used for numerical operations and array handling                                 |
| **scikit-learn** | For model training, evaluation, and preprocessing                                |
| **tldextract**   | Extracts top-level domains (TLDs) from URLs                                      |
| **matplotlib**   | Visualizes feature importance from the trained model                             |
| **re**           | Built-in Python module for working with regular expressions (e.g., IP detection) |
| **warnings**     | Used to suppress warnings during execution                                       |


---
## How to Run Program

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/phishing_url_classifier.git
cd phishing_url_classifier
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
or

```bash
pip install pandas scikit-learn tldextract matplotlib
```

### 3. Launch Python Script
```bash
python phishing_detector.py
```
## Example Results
Coming soon!
---
