
import os
import random

#imgspath = 'images' #path to images
path = 'C:/Users/kolli/Desktop/umbc/606/room-inference-using-object-detection/dataset/smallDataset/images/'
images = []
for i in os.listdir(path):
    temp = path+i
    images.append(temp)
# train and test split... adjust it if necessary
trainlen = round(len(images)*.80)
vallen = round(len(images)*.10)
testlen = round(len(images)*.10)
#print('total, train, test dataset size -',trainlen+testlen,trainlen,testlen)
print(f'trainlen: {trainlen}')
print(f'vallen: {vallen}')
print(f'testlen: {testlen}')
random.shuffle(images)
test = images[:testlen]
val = images[testlen:testlen+vallen]
train = images[vallen+testlen:vallen+testlen+trainlen]

with open('train.txt', 'w') as f:
    for item in train:
        f.write("%s\n" % item)
with open('test.txt', 'w') as f:
    for item in test:
        f.write("%s\n" % item)
with open('val.txt', 'w') as f:
    for item in val:
        f.write("%s\n" % item)