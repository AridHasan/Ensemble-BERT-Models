import pandas as pd

df = pd.read_csv('arabic.csv', sep=',')

random_seed = 2814

train_df = df.sample(frac=0.9, random_state=random_seed)
valid_df = df.drop(train_df.index)

assert len(df) == len(train_df) + len(valid_df), "Dataset sizes don't add up"

train_df.to_csv('data/arabic/train.csv', index=False, sep=',', header=['id', 'text', 'label'])
valid_df.to_csv('data/arabic/dev.csv', index=False, sep=',', header=['id', 'text', 'label'])
