import pandas as pd

from model import Demissionaire


def nettoie_dem(demissionaire_data):
    demissionaire = Demissionaire(
        sexe=demissionaire_data['CDSEXE'],
        revenu=demissionaire_data['MTREV'],
        nb_enf=demissionaire_data['NBENF'],
        code_statut=demissionaire_data['CDTMT'],
        type_client=demissionaire_data['CDCATCL'],
        adhesion_annee=pd.to_datetime(demissionaire_data['DTADH'], format='%d/%m/%Y').dt.year,
        dem_annee=demissionaire_data['ANNEEDEM'],
        dem_id=demissionaire_data['ID'],
        tranche_age_adhesion=demissionaire_data['RANGAGEAD'],
        tranche_age_dem=demissionaire_data['RANGAGEDEM'],
    )


def nettoie_soc(societaires):
    for soc in societaires:
        pass
