import filesManager
import json
import os.path
from os import path


class Config:
    def __init__(self):
        self.filesManager = filesManager.FilesManager()

        self.configPath = "config"
        if not path.exists(self.configPath):
            self.writeConfig()
        self.readConfig()

    def readConfig(self):
        configFile = open(self.configPath, "r")
        configJsonString = configFile.read()
        configJsonObject = json.loads(configJsonString)

        # Read all Config
        self.cfg_folder = configJsonObject['CFG_FOLDER']

    def writeConfig(self):
        configObject = {
            'CFG_FOLDER': self.cfg_folder
        }
        configObjectJson = json.dumps(configObject)
        configFile = open(self.configPath, "w")
        configFile.write(configObjectJson)

    def addFolder(self, folderPath):
        self.cfg_folder.append(folderPath)
        self.writeConfig()
    
    def getFolders(self):
        return self.cfg_folder
    
    def getAllFilesFolder(self, folderPath):
        return self.filesManager.readFolder(folderPath)

    def getParam(self, paramId):
        if paramId == "CFG_FOLDER":
            return self.cfg_folder
