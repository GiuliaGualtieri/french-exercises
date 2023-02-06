# %%
import numpy as np
import pandas as pd

# %% tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = None
product = None

# %%
df = pd.DataFrame(np.zeros((1, 1)))
with open("data/in/lepetitprinceexupery.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        data = line.strip().split("\t")
        for el in data:
            phrases = el.strip().split(".")
            for phrase in phrases:
                df = pd.DataFrame(np.append(df.values, [[phrase]], axis=0))

# %%
list_punctuation_to_remove = "!#$%&()*+./:;<=>?@[\\]^_{|}~)"

# %%
def check_row_is_to_remove(row):
    # convert and remove punctuation
    new_row = row.translate(str.maketrans("", "", list_punctuation_to_remove))
    # we want it has at least 5 words.
    len_row = len(new_row.split())
    if len_row < 5:
        to_clean = "True"
    else:
        to_clean = "False"
    return [to_clean, new_row]


# %%
df.rename(columns={0: "original"}, inplace=True)

# %%
df[["check", "new"]] = [
    [check_row_is_to_remove(el)[0], check_row_is_to_remove(el)[1]]
    for el in df["original"]
]

# %%
df = df.loc[df["check"] == "False"]

# %%
df.head(10)

# %%
df.to_csv(product["data"], index=False)
