|  **`Travis CI Status`**   |
|-------------------|
|[![Build Status](https://travis-ci.org/ulisesojeda/dictionary_map.svg?branch=master)](https://travis-ci.org/ulisesojeda/dictionary_map)|

|  **`PyPi`**   |
|-------------------|
|[![PyPI version](https://badge.fury.io/py/dict-map.svg)](https://badge.fury.io/py/dict-map)|
Dictionary Mapping
=======================

Apply a map-like function over a Python dictionary and return a new dictionary
with the same keys and its values evaluated.

## Installation
`$ pip install dict-map`

### API
```python
dict_map(func, value, deep);
```
- `func`  
  Type *function*  
  Mapping function

- `value`  
  Type *dictionary*  
  Dictionary to mp

- `deep`[False]  
  Type *Boolean*  
  Recurse over nested dictionaries

## How to use
```python
import dict_map as dict_map
value = {2:2, 3:3, 4:{5:5, 6:6}}
func = lambda x: x**2
print(dict_map.dict_map(func, value, False))
#{2: 4, 3: 9, 4: {5: 5, 6: 6}}
print(dict_map.dict_map(func, value, True))
#{2: 4, 3: 9, 4: {5: 25, 6: 36}}
```

#### Notes
Inspired by [browser-object-map](https://github.com/juliomatcom/browser-object-map)

#### MIT Licensed
Copyright (c) 2017 Ulises Ojeda
