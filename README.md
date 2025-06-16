# Phishing URL Classifier with Python

This project is a simple machine learning tool to classify URLs as **phishing** or **legitimate** using basic features extracted from the URL string itself.

It uses **Python**, **scikit-learn**, and a public dataset from sources like [PhishTank](https://www.phishtank.com/) or [Kaggle](https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls?resource=download).

---

## Why This Project?

Phishing is one of the most common and effective attack vectors in cybersecurity. This project demonstrates how **machine learning** can be applied to detect phishing attempts using features that can be derived without visiting the webpage.

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

- Python 3.x
- Jupyter Notebook
- [pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)
- [tldextract](https://github.com/john-kurkowski/tldextract)
- re (regex)
- matplotlib (optional for visualization)

---

