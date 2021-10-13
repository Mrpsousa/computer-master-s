#!/usr/bin/env python
# coding: utf-8

import numpy as np


def read_data():
    nl = np.float_(input().split(' '))
    print(nl)
    dl = []
    for i in np.arange(nl[0]-nl[1]):
        dl.append(np.float_(input().split(' ')))
        
    train = np.vstack((dl))
    test = np.float_(input().split(' '))
    
    return train, test


def predict(train):
    return np.mean(np.mean(train[:, train.shape[1]-1]))


train, test = read_data()

print(f'Treino: {train}')
print(f'Teste: {test}')
print(predict(train))
