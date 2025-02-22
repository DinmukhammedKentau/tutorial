import os

path = "."
allElements = os.listdir(path)
print(allElements)
allDirs, allFiles = [], []
for element in allElements:
    if os.path.isdir(os.path.join(path, element)):
        allDirs.append(element)
for element in allElements:
    if os.path.isfile(os.path.join(path, element)):
        allFiles.append(element)
print("Files", allFiles)
print("Directories:", allDirs)
print("all files and directories:", allElements)
""".-точка агымдагы папканы билдиреди"""
