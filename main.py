from phishing_detector import (
    load_data,
    preprocess_data,
    train_and_evaluate,
    plot_feature_importance
)

def main():
    print("Phishing URL Classifier starting...\n")
    df = load_data('phishing_site_urls.csv')
    (X_train, X_test, y_train, y_test), feature_names = preprocess_data(df)
    model = train_and_evaluate(X_train, X_test, y_train, y_test)
    plot_feature_importance(model, feature_names)
    print("\nDone!")

if __name__ == '__main__':
    main()
