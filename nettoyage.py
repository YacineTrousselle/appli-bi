import datetime

import numpy as np
import pandas as pd

from model import Demissionaire, Societaire


def nettoie_dem(demissionaire_data):
    return Demissionaire(
        sexe=demissionaire_data['CDSEXE'],
        revenu=demissionaire_data['MTREV'],
        nb_enfants=demissionaire_data['NBENF'],
        code_statut=demissionaire_data['CDTMT'],
        type_client=demissionaire_data['CDCATCL'],
        adhesion_annee=parse_year(demissionaire_data['DTADH']),
        dem_annee=demissionaire_data['ANNEEDEM'],
        tranche_age_adhesion=demissionaire_data['RANGAGEAD'],
        tranche_age_dem=demissionaire_data['RANGAGEDEM'],
        situation_familiale=demissionaire_data['CDSITFAM'],
    )


def nettoie_soc(societaire_data):
    return Societaire(
        sexe=societaire_data['CDSEXE'],
        revenu=societaire_data['MTREV'],
        nb_enfants=societaire_data['NBENF'],
        code_statut=societaire_data['CDTMT'],
        type_client=societaire_data['CDCATCL'],
        adhesion_annee=parse_year(societaire_data['DTADH']),
        dem_annee=parse_year(societaire_data['DTDEM']),
        situation_familiale=societaire_data['CDSITFAM'],
    )


def parse_year(date_string):
    try:
        return pd.to_datetime(date_string, format='%d/%m/%Y').year
    except BaseException as e:
        print('Error parsing date:', date_string, e)
        return '1900'


def filtre_soc(societaires: list) -> list:
    numerical_fields = ['revenu']
    for numerical_field in numerical_fields:
        values = np.array([societaire.__dict__[numerical_field] for societaire in societaires])
        median = np.median(values)
        q1 = np.percentile(values, 25)
        q3 = np.percentile(values, 75)
        print(f"{numerical_field} - Médiane: {median}, Q1: {q1}, Q3: {q3}, Moyenne: {values.mean():.2f}")

    return societaires


def filtre_revenu(societaires: list):
    df = pd.DataFrame([vars(soc) for soc in societaires])
    df_zero = df[df['revenu'] == 0]
    df_non_zero = df[df['revenu'] > 0]

    print(f'Proportion de revenu a 0: {len(df_zero) * 100 / len(df):.2f}%')
    print('Revenu > 0:', df_non_zero['revenu'].describe())
    q1, q2, q3 = df_non_zero['revenu'].quantile([0.25, 0.5, 0.75])
    print(f'Q1: {q1}, Q2: {q2}, Q3: {q3}')
    iqr = (q3 - q1)
    seuil_max = q3 + 2.5 * iqr
    print(f'Seuil: {seuil_max:.2f}')

    df_aber = df_non_zero[df_non_zero['revenu'] > seuil_max]
    print(f'{len(df_aber)} revenus aberrants')
    print(df_aber)

    df['a_revenu'] = df['revenu'] > 0
    df['revenu_reduit'] = df['revenu'].clip(upper=seuil_max)


def preprocess(societaires: list) -> pd.DataFrame:
    df = pd.DataFrame([vars(soc) for soc in societaires])

    annee_courante = datetime.datetime.now().year

    df['a_demissionne'] = df['dem_annee'] != 1900
    df['a_revenu'] = df['revenu'] > 0

    seuil_revenu = 100000
    df['revenu'] = df['revenu'].clip(upper=seuil_revenu)
    df['anciennete'] = annee_courante - df['adhesion_annee']

    df = df.drop(columns=['dem_annee'])
    df = df[df['revenu'] >= 0]

    return df


def analyze_and_process(df: pd.DataFrame):
    print('Pourcentage de démissionnaires:' + str(len(df[df['a_demissionne'] == True]) * 100 // len(df)) + '%')
    df = upsample_non_demissionnaires(df)
    print('Pourcentage de démissionnaires apres upsample:' + str(
        len(df[df['a_demissionne'] == True]) * 100 // len(df)) + '%')

    print(df.describe())


def upsample_non_demissionnaires(df: pd.DataFrame) -> pd.DataFrame:
    df_0 = df[df['a_demissionne'] == False]
    df_1 = df[df['a_demissionne'] == True]
    df_0_upsampled = df_0.sample(n=len(df_1), replace=True, random_state=42)

    return pd.concat([df_1, df_0_upsampled])
