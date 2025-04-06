import os

import pandas as pd
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

from nettoyage import nettoie_dem, nettoie_soc, preprocess, analyze_and_process

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

def plot_model_metrics(models: dict, X_test, y_test, y_preds: dict, save_dir='fig/models'):
    os.makedirs(save_dir, exist_ok=True)

    scores = {
        'accuracy': {},
        'precision': {},
        'recall': {},
        'f1': {}
    }

    for name, y_pred in y_preds.items():
        scores['accuracy'][name] = metrics.accuracy_score(y_test, y_pred)
        scores['precision'][name] = metrics.precision_score(y_test, y_pred)
        scores['recall'][name] = metrics.recall_score(y_test, y_pred)
        scores['f1'][name] = metrics.f1_score(y_test, y_pred)

    for metric, values in scores.items():
        plt.figure(figsize=(6,4))
        plt.bar(values.keys(), values.values(), color='skyblue')
        plt.title(f'{metric.upper()} comparison')
        plt.ylabel(metric)
        plt.ylim(0, 1)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig(f"{save_dir}/{metric}_comparison.png")
        plt.close()

def save_classification_reports(y_test, y_preds: dict, save_dir='fig'):
    os.makedirs(save_dir, exist_ok=True)
    report_path = os.path.join(save_dir, 'classification_reports.txt')

    with open(report_path, 'w') as f:
        for name, y_pred in y_preds.items():
            f.write(f"=== {name} ===\n")
            f.write(classification_report(y_test, y_pred))
            f.write('\n' + '='*40 + '\n\n')

if __name__ == '__main__':
    demissionaires = pd.read_csv('donnees_banque/demissionaires.csv')
    societaires = pd.read_csv('donnees_banque/societaires.csv')
    soc = societaires.to_dict(orient='records')[0]

    demissionaires = [nettoie_dem(dem) for dem in demissionaires.to_dict(orient='records')]
    societaires = [nettoie_soc(soc) for soc in societaires.to_dict(orient='records')]
    all_societaires = societaires + [dem.to_societaire() for dem in demissionaires]

    preprocessed_societaires = preprocess(all_societaires)
    preprocessed_societaires.to_csv('donnees_banque/preprocessed_societaires.csv', index=False)

    print(preprocessed_societaires.columns)
    print(len(preprocessed_societaires))
    print(preprocessed_societaires.describe())
    print(preprocessed_societaires['anciennete'])

    processed_societaires = analyze_and_process(preprocessed_societaires)

    colonne_cible = 'a_demissionne'
    X = processed_societaires.drop(columns=[colonne_cible])
    y = processed_societaires[colonne_cible]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        'Logistic Regression': LogisticRegression(),
        'Random Forest': RandomForestClassifier(),
        'SVM': SVC()
    }

    y_preds = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        y_preds[name] = y_pred
        print(f"=== {name} ===")
        print(classification_report(y_test, y_pred))

    plot_model_metrics(models, X_test, y_test, y_preds)
    save_classification_reports(y_test, y_preds)

    print('FIN')
