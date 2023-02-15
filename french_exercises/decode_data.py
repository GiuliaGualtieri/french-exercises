# %%
import random

import pandas as pd

from french_exercises.model import f_decode_input

# %% tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = ["read-data", "model"]
product = None

# %%
dict_QA = {"question": [], "answer": []}

df = pd.read_csv(upstream["read-data"]["data"])

dict_QA = {'question' : [], 'answer' : [], 'answers' : []}

list_punctuation_to_remove = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~)Ã©ª'

def check_prediction(to_mask, predictions):
    list_ok = []
    list_ko = []
    predictions2 = None
    for prediction in predictions:
        prediction.translate(str.maketrans('', '', list_punctuation_to_remove))
        if len(prediction)<2:
            list_ko.append(prediction)
        elif len(prediction)< 7 and len(prediction)<(len(to_mask)-2):
            list_ko.append(prediction)
        else:
            list_ok.append(prediction)
    if list_ko:
        txt2 = "Un possible synonyme de "+to_mask+" est <mask>."
        predictions2 = f_decode_input(txt2)
        predictions2 = [el.translate(str.maketrans('', '', list_punctuation_to_remove)) for el in predictions2]
        predictions2 = [el for el in predictions2 if len(el)>1]
        list_ok.extend(predictions2)
    return list_ok

for row in df.iterrows():
    words = row[1]['new'].split()
    rnd = random.randint(0,len(words)-1)
    to_mask = words[rnd]
    while len(to_mask)<2:
        rnd = random.randint(0,len(words)-1)
        to_mask = words[rnd]    
    words[rnd] = '<mask>'
    to_txt = ''
    for el in words:
        to_txt += el + ' '
    txt = to_txt[:-1]
    predictions = f_decode_input(txt)
    predictions = check_prediction(to_mask, predictions)
    if to_mask not in predictions:
        predictions = predictions[:-1]
        predictions.append(to_mask)
    dict_QA['question'].append(txt)
    dict_QA['answer'].append(to_mask)
    dict_QA['answers'].append(predictions)

# %%
df["question"] = dict_QA["question"]
df["answer"] = dict_QA["answer"]
df["answers"] = dict_QA["answers"]

# %% Save the output
df.drop(labels=["original", "check"], axis=1, inplace=True)
df.to_csv(product["data"], index=False)
