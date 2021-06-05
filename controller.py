import views
import config


class Controller:
    def __init__(self):
        self.view = None
        self.config = config.Config()

    def menu_select(self, index=0):
        select = 999
        while select != 0:
            # Display menu
            if index == 0:
                self.view = views.Views()
                select = self.view.main()

            # Select
            # Configuration
            if index == 0 and select == 1:
                self.view.list(self.config)
            elif index == 0 and select == 2:
                sub_select = self.view.config(self.config)
                if sub_select != 0:
                    # add folder
                    if sub_select == 1:
                        self.view.config_addFolder(self.config)

        self.view.exit()
