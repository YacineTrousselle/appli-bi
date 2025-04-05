class Societaire:
    def __init__(self, sexe, revenu, nb_enfants, code_statut, type_client, adhesion_annee, dem_annee,
                 situation_familiale):
        self.sexe = sexe
        self.revenu = revenu
        self.nb_enfants = nb_enfants
        self.code_statut = code_statut
        self.type_client = type_client
        self.adhesion_annee = adhesion_annee
        self.dem_annee = dem_annee
        self.situation_familiale = situation_familiale

    def __str__(self):
        return ('{'
                f'"sexe": "{self.sexe}", '
                f'"revenu": {self.revenu}, '
                f'"nb_enfants": {self.nb_enfants}, '
                f'"code_statut": "{self.code_statut}", '
                f'"type_client": "{self.type_client}", '
                f'"adhesion_annee": {self.adhesion_annee}, '
                f'"dem_annee": {self.dem_annee}, '
                f'"situation_familiale": {self.situation_familiale}'
                '}')

    def __repr__(self):
        return self.__str__()


class Demissionaire:
    def __init__(self, sexe, revenu, nb_enfants, code_statut, type_client, adhesion_annee, dem_annee,
                 tranche_age_adhesion,
                 tranche_age_dem, situation_familiale):
        self.sexe = sexe
        self.revenu = revenu
        self.nb_enfants = nb_enfants
        self.code_statut = code_statut
        self.type_client = type_client
        self.adhesion_annee = adhesion_annee
        self.dem_annee = dem_annee
        self.tranche_age_adhesion = tranche_age_adhesion
        self.tranche_age_dem = tranche_age_dem
        self.situation_familiale = situation_familiale

    def to_societaire(self) -> Societaire:
        return Societaire(
            sexe=self.sexe,
            revenu=self.revenu,
            code_statut=self.code_statut,
            nb_enfants=self.nb_enfants,
            type_client=self.type_client,
            adhesion_annee=self.adhesion_annee,
            dem_annee=self.dem_annee,
            situation_familiale=self.situation_familiale,
        )
