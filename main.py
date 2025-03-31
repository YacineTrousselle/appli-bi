import pandas as pd

from nettoyage import nettoie_dem, nettoie_soc

if __name__ == '__main__':
    demissionaires =  pd.read_csv('donnees_banque/demissionaires.csv').to_dict(orient='records')
    societaires =  pd.read_csv('donnees_banque/societaires.csv').to_dict(orient='records')

    demissionaires = [nettoie_dem(dem) for dem in demissionaires]
    societaires = [nettoie_soc(soc) for soc in societaires]

    all_societaires = societaires + [dem.to_societaire()  for dem in demissionaires]

    print(all_societaires[:10])
