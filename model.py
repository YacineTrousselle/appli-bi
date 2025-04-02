class Societaire:
    def __init__(self, sexe, revenu, nb_enf, code_statut, type_client, adhesion_annee, dem_annee, dem_id=None):
        self.sexe = sexe
        self.revenu = revenu
        self.nb_enf = nb_enf
        self.code_statut = code_statut
        self.type_client = type_client
        self.adhesion_annee = adhesion_annee
        self.dem_annee = dem_annee
        # self.dem_id = dem_id

    def __str__(self):
        return ('{'
                f'"sexe": "{self.sexe}", '
                f'"revenu": {self.revenu}, '
                f'"nb_enf": {self.nb_enf}, '
                f'"code_statut": "{self.code_statut}", '
                f'"type_client": "{self.type_client}", '
                f'"adhesion_annee": {self.adhesion_annee}, '
                f'"dem_annee": {self.dem_annee}, '
                # f'"dem_id": {self.dem_id if self.dem_id is not None else "null"}'
                '}')

    def __repr__(self):
        return self.__str__()

class Demissionaire:
    def __init__(self, sexe, revenu, nb_enf, code_statut, type_client, adhesion_annee, dem_annee, dem_id,
                 tranche_age_adhesion,
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

    def to_societaire(self) -> Societaire:
        return Societaire(
            sexe=self.sexe,
            revenu=self.revenu,
            code_statut=self.code_statut,
            nb_enf=self.nb_enf,
            type_client=self.type_client,
            adhesion_annee=self.adhesion_annee,
            dem_annee=self.dem_annee,
            dem_id=self.dem_id
        )
