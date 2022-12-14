# -*- coding: utf-8 -*-
"""data_loading.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ta7bBVHD-TNygE5w4fak2AhA83naTSca
"""
#!pip install anndata


import anndata as sc
import pandas as pd
from sklearn import preprocessing
import torch

def get_data(PATH_TRAIN, PATH_TEST):
  adata_train = sc.read_h5ad(PATH_TRAIN)
  data_raw = pd.DataFrame.sparse.from_spmatrix(adata_train.layers["counts"])
  data_X = pd.DataFrame.sparse.from_spmatrix(adata_train.X)

  adata_test = sc.read_h5ad(PATH_TEST)
  data_test_raw=pd.DataFrame.sparse.from_spmatrix(adata_test.layers["counts"])
  data_test_X=pd.DataFrame.sparse.from_spmatrix(adata_test.X)
  return adata_train, adata_test, data_raw, data_X,data_test_raw, data_test_X

def normalize(df):
  names=df.columns
  d = preprocessing.normalize(df.values, axis=0)
  scaled_df = pd.DataFrame(d, columns=names)
  return torch.tensor(scaled_df.values,dtype=torch.float32)


