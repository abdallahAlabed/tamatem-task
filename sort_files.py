import os

filesPath = os.path.join(os.path.dirname(__file__), r'one-k-files-main\files')

def getFullFileName(file):
    return os.path.join(filesPath, file)

# read file name and extract subfolder name from it
def getSubFolderPath(file):
    return os.path.join(filesPath, file[0:file.find('-')])

# Checks if file needs a new subfolder and creates it
def createSubFolder(file):
    path = getSubFolderPath(file)
    if(not os.path.isdir(path)):
        os.makedirs(path)

# Move the file to the subfolder
def moveFile(file):
    if(os.path.isfile(getFullFileName(file))):
        os.rename(getFullFileName(file), os.path.join(getSubFolderPath(file),file))

# loop through files for sorting
for file in os.listdir(filesPath):
    createSubFolder(file)
    moveFile(file)
