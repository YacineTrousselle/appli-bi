import pandas as pd
from pandas._libs.parsers import ParserError

from model import Demissionaire, Societaire


def nettoie_dem(demissionaire_data):
    return Demissionaire(
        sexe=demissionaire_data['CDSEXE'],
        revenu=demissionaire_data['MTREV'],
        nb_enf=demissionaire_data['NBENF'],
        code_statut=demissionaire_data['CDTMT'],
        type_client=demissionaire_data['CDCATCL'],
        adhesion_annee=parse_year(demissionaire_data['DTADH']),
        dem_annee=demissionaire_data['ANNEEDEM'],
        dem_id=demissionaire_data['ID'],
        tranche_age_adhesion=demissionaire_data['RANGAGEAD'],
        tranche_age_dem=demissionaire_data['RANGAGEDEM'],
    )


def nettoie_soc(societaire_data):
    return Societaire(
        sexe=societaire_data['CDSEXE'],
        revenu=societaire_data['MTREV'],
        nb_enf=societaire_data['NBENF'],
        code_statut=societaire_data['CDTMT'],
        type_client=societaire_data['CDCATCL'],
        adhesion_annee=parse_year(societaire_data['DTADH']),
        dem_annee=parse_year(societaire_data['DTDEM']),
        dem_id=None,
    )


def parse_year(date_string):
    try:
        return pd.to_datetime(date_string, format='%d/%m/%Y').dt.year
    except BaseException:
        return None
