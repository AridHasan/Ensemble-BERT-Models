# CS6765 Project: Ensemble Language Models for Multilingual Sentiment Analysis

In this project, we explored sentiment analysis using four pretrained language models. Moreover, we proposed two ensemble models. For detailed information about our experiments and proposed model please read the project report.

### Project Report


[http://arxiv.org/abs/2403.06060](http://arxiv.org/abs/2403.06060)


## Dataset

- English and Arabic: [SemEval 2017](https://alt.qcri.org/semeval2017/task4/index.php?id=data-and-tools)
- Arabic Additional Trainset: [ASTD](https://github.com/mahmoudnabil/ASTD)

### Preparing Data
Run the following commands in commandline
```
# For preparing English dataset
python bin/prep_en.py
# For preparing Arabic dataset
python bin/prep_ar.py
python bin/split_ar.py
```
## Running Experiments
**GPU uses is highly recommended. Otherwise, to complete the experiments might take several days.**

### Fine-tune Language Models (RoBERTa, AraBERTv02, multilingual BERT, XLM-RoBERTa)
To fine-tune language models, please run the following command and run all the cell in notebook
```
jupyter notebook CS6765_finetuning_lm.ipynb
```

### Ensemble Models

#### Ensemble model with Feed Forward Network
To run the code, please enter the following command. This notebook is designed to train both English and Arabic language jointly.
```
jupyter notebook CS6765-ensemble_with_feed_forward.ipynb
```

#### Ensemble model with Multi-head Attention followed by a Feed Forward Network
To run the code, please enter the following command. This notebook is designed to train both English and Arabic language jointly.
```
jupyter notebook CS6765-ensemble_with_attn_ff.ipynb
```

#### Ensemble model with Multi-head Attention followed by a Feed Forward Network
To run the code, please enter the following command. This notebook is designed to train language specific ensemble model.
```
jupyter notebook CS6765-ensemble_model_train_with_lang_specific_data.ipynb
```

### Calculate Model Performance
To calculate the model performances, please run the following command:
```
jupyter notebook Calculate_performace.ipynb
```

### Cite
If you follow this notebook, please cite:

```
@article{hasan2023ensemble,
  title={Ensemble Language Models for Multilingual Sentiment Analysis},
  author={Hasan, Md Arid},
  journal={arXiv preprint arXiv:},
  year={2024}
}
```


