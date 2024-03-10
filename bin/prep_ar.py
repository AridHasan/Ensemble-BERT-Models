import csv
import re

def remove_url(t):
    #t = ' '.join(re.sub("([@#][A-Za-z0-9_]+)|(\w+:\/\/\S+)"," ", t).split())
    t = re.sub(r"http\S+", "", t)
    return t.lower()

def convert_label(label):
    if label == 'positive':
        label = 2
    elif label == 'neutral':
        label = 1
    elif label == 'negative':
        label = 0
    return label

header = ['id', 'text', 'label']

astd = []
data = []
with open('data/arabic/Tweets.txt') as f:
    lines = f.read().strip().split("\n")
    print(len(lines))
    i=1
    for line in lines:
        d = line.split('\t')
        if d[1] == 'NEG':
            data.append([i, d[0], 0])
        elif d[1] == 'POS':
            data.append([i, d[0], 2])
        elif d[1] == 'NEUTRAL':
            data.append([i, d[0], 1])
        i+=1
aids = []
with open('data/arabic/SemEval2017-task4-train.subtask-A.arabic.txt') as f:
    lines = f.read().strip().split('\n')
    for l in lines:
        d = l.split('\t')
        data.append([d[0], remove_url(d[2].replace('"', '')), convert_label(d[1])])
        aids.append(d[0])
print(len(data))
with open('data/arabic/SemEval2017-task4-train.subtask-BD.arabic.txt') as f:
    lines = f.read().strip().split('\n')
    for l in lines:
        d = l.split('\t')
        if d[0] not in aids:
            data.append([d[0], remove_url(d[3]), convert_label(d[2])])

with open('arabic.csv', 'w') as f:
    writer = csv.writer(f)
    for d in data:
        writer.writerow(d)

with open('data/arabic/test.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    with open('data/arabic/SemEval2017-task4-test.subtask-A.arabic.txt') as f:
        lines = f.read().strip().split('\n')
        for l in lines:
            d = l.split('\t')
            writer.writerow([d[0], remove_url(d[2].replace('"', '')), convert_label(d[1])])
            #aids.append(d[0])

