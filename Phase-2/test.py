import shutil
import os

imagesList = os.listdir('dataset/smallDataset/images')
labelsList = os.listdir('dataset/smallDataset/labels')

for i in imagesList:
    if i.split('.')[0]+'.txt' in labelsList:
        pass
    else:
        shutil.move('dataset/smallDataset/images/' + i, 'dataset/smallDataset/' + i)