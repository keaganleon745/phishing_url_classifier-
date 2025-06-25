# Entry point to run the phishing URL classifier
from phishing_detector import (
    load_data,
    preprocess_data,
    train_and_evaluate,
    plot_feature_importance
)

def main():
    print("Phishing URL Classifier starting...\n")
    
    # Step 1: Load dataset
    df = load_data('phishing_site_urls.csv')

    # Step 2: Preprocess features and labels
    (X_train, X_test, y_train, y_test), feature_names = preprocess_data(df)

    # Step 3: Train the model and display evaluation results
    model = train_and_evaluate(X_train, X_test, y_train, y_test)

    # Step 4: Plot most important features
    plot_feature_importance(model, feature_names)
    
    print("\nDone!")

if __name__ == '__main__':
    main()
