#%%
from sklearn.datasets import fetch_openml

# %%
mnist= fetch_openml('mnist_784',version=1)
mnist.keys()
dict_keys(['data', 'target','feature_names','DESCR', 'details',
         'categories','url'])
# %%
