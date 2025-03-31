import pandas as pd

from nettoyage import nettoie_dem, nettoie_soc

if __name__ == '__main__':
    demissionaires =  pd.read_csv('donnees_banque/demissionaires.csv')
    societaires =  pd.read_csv('donnees_banque/societaires.csv')

    # TODO: clear Data


    demissionaires = [nettoie_dem(dem) for dem in demissionaires.to_dict(orient='records')]
    societaires = [nettoie_soc(soc) for soc in societaires.to_dict(orient='records')]

    all_societaires = societaires + [dem.to_societaire()  for dem in demissionaires]
