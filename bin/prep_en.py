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

with open('data/english/train.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'text', 'label'])
    fns = ['twitter-2013dev-A.txt', 'twitter-2013test-A.txt', 'twitter-2013train-A.txt',
           'twitter-2014sarcasm-A.txt', 'twitter-2014test-A.txt',
           'twitter-2015test-A.txt', 'twitter-2015train-A.txt',
           'twitter-2016dev-A.txt', 'twitter-2016train-A.txt', 'twitter-2016test-A.txt', 'twitter-2016devtest-A.txt']
    for fn in fns:
        with open(f'data/english/{fn}') as f:
            print(f'reading{fn}')
            lines = f.read().strip().split("\n")
            for l in lines:
                d = l.split('\t')
                # print(d[0])
                writer.writerow([d[0], remove_url(d[2]), convert_label(d[1])])
    """with open(f'data/english/sms-2013test-A.tsv') as f:
        print(f'reading{fn}')
        lines = f.read().strip().split("\n")
        for l in lines:
            d = l.split('\t')
            writer.writerow([d[0], remove_url(d[3]), convert_label(d[2])])
    with open(f'data/english/livejournal-2014test-A.tsv') as f:
        print(f'reading{fn}')
        lines = f.read().strip().split("\n")
        for l in lines:
            d = l.split('\t')
            writer.writerow([d[0], remove_url(d[3]), convert_label(d[2])])"""

with open('data/english/dev.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'text', 'label'])
    with open(f'data/english/sms-2013test-A.tsv') as f:
        print(f'reading{fn}')
        lines = f.read().strip().split("\n")
        for l in lines:
            d = l.split('\t')
            writer.writerow([d[0], remove_url(d[3]), convert_label(d[2])])
    with open(f'data/english/livejournal-2014test-A.tsv') as f:
        print(f'reading{fn}')
        lines = f.read().strip().split("\n")
        for l in lines:
            d = l.split('\t')
            writer.writerow([d[0], remove_url(d[3]), convert_label(d[2])])
    """with open('data/english/twitter-2016devtest-A.txt') as f:
        lines = f.read().strip().split("\n")
        for l in lines:
            d = l.split('\t')
            writer.writerow([d[0], remove_url(d[2]), convert_label(d[1])])"""

with open('data/english/test.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'text', 'label'])
    with open('data/english/SemEval2017-task4-test.subtask-A.english.txt') as f:
        lines = f.read().strip().split("\n")
        for l in lines:
            d = l.split('\t')
            writer.writerow([d[0], remove_url(d[2]), convert_label(d[1])])
