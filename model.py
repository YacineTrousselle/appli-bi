class Societaire:
    def __init__(self, sexe, revenu, nb_enf, code_statut, type_client, adhesion_annee, dem_annee, dem_id=None):
        self.sexe = sexe
        self.revenu = revenu
        self.nb_enf = nb_enf
        self.code_statut = code_statut
        self.type_client = type_client
        self.adhesion_annee = adhesion_annee
        self.dem_annee = dem_annee
        self.dem_id = dem_id


class Demissionaire:
    def __init__(self, sexe, revenu, nb_enf, code_statut, type_client, adhesion_annee, dem_annee, dem_id, tranche_age_adhesion,
                 tranche_age_dem):
        self.sexe = sexe
        self.revenu = revenu
        self.nb_enf = nb_enf
        self.code_statut = code_statut
        self.type_client = type_client
        self.adhesion_annee = adhesion_annee
        self.dem_annee = dem_annee
        self.dem_id = dem_id
        self.tranche_age_adhesion = tranche_age_adhesion
        self.tranche_age_dem = tranche_age_dem
