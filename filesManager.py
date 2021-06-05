from os import listdir, walk
from os.path import isfile, join


class FilesManager:
    def readFolder(self, folderPath):
        series = {}
        for root, directories, files in walk(folderPath, topdown=False):
            for name in files:
                serieName = name.split('-')[0]
                serieEpisodeNumber = name.split('-')[1]
                if serieName not in series:
                    series[serieName] = []
                series[serieName].append(
                    {"path": join(root, name), "number": serieEpisodeNumber})

        return series
