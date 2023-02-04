# %% tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = ['read-data', 'model']
product = None


# %% [markdown]
# ## Decode the input
import pandas as pd
import random

# %%
dict_QA = {'question' : [], 'answer' : []}

df = pd.read_csv(upstream['read-data']['data'])

for row in upstream.iterrows():
    words = row[1]['new'].split()
    rnd = random.randint(0,len(words)-1)
    to_mask = words[rnd]
    words[rnd] = '<mask>'
    to_txt = ''
    for el in words:
        to_txt += el + ' '
    txt = to_txt[:-1]
    predictions = f_decode_input(txt)
    predictions.append(to_mask)
    dict_QA['question'].append(txt)
    dict_QA['answer'].append(predictions)

# %%
df['question'] = dict_QA['question']
df['answer'] = dict_QA['answer']

# %% Save the output
df.drop(labels = ['original','check'], axis = 1 , inplace = True)
df.to_csv(product['data'], index = False)
