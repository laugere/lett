import os


class Views:
    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def main(self):
        self.cls()
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ Bienvenue sur Lett         ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ 1. Bibliothèque            ┃")
        print("┃ 2. Configuration           ┃")
        print("┃ 0. Sortir                  ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        return int(input("Votre choix : "))

    def list(self, config):
        self.cls()
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ Bibliothèque               ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        folders = config.getFolders()
        iterator = 0
        for folder in folders:
            series = config.getAllFilesFolder(folder)
            for serie in series:
                iterator += 1
                print("┃ {0}. {1}".format(iterator, serie))
        print("┃ 0. Retour                  ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        return int(input("Votre choix : "))

    def config(self, config):
        self.cls()
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ Configurations             ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ 1. Dossiers de recherche   ┃")
        for folder in config.getParam("CFG_FOLDER"):
            print("┃    - {0}".format(folder))
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        return int(input("Modification N° ou 0 pour fermer : "))

    def config_addFolder(self, config):
        self.cls()
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ Ajout dossier de recherche ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ Chemin d'accès :           ┃")
        config.addFolder(input())
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    def exit(self):
        self.cls()
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ Au revoir...               ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
