import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

from nettoyage import nettoie_dem, nettoie_soc, preprocess

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

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
    exit(0)

    data = []
    for soc in all_societaires:
        data.append(vars(soc) | {'cible': 0 if soc.dem_annee == 1900 else 1})

    df = pd.DataFrame(data)
    df = df.drop(columns=['dem_annee'])
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    df = pd.get_dummies(df, columns=['sexe', 'code_statut', 'type_client'])

    X = df.drop(columns=['cible'])
    y = df['cible']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        'Logistic Regression': LogisticRegression(),
        'Random Forest': RandomForestClassifier(),
        'SVM': SVC()
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print(f"=== {name} ===")
        print(classification_report(y_test, y_pred))

    print('FIN')
