# Where to start

## Notebooks

#### [Covid19 Online Machine Learning](http://127.0.0.1:8888/doc/tree/covid19-online-machine-learning.ipynb)

This notebook is used for demonstrating, how to define Online Machine Learning models with Creme and deploy them on Chantilly. Several different models are defined inside this notebook and the dataset [GoogleCloudPlatform/covid-19-open-data](https://github.com/GoogleCloudPlatform/covid-19-open-data) is used for experimenting with the models.

#### [Intro into Creme](http://127.0.0.1:8888/doc/tree/intro_creme.ipynb)

A pretty small notebook for looking into different models available in creme

## Scripts

#### `python simulate.py`

```
# python simulate.py --help
usage: simulate.py [-h] [--file [FILE]] [speed_up]

positional arguments:
  speed_up

optional arguments:
  -h, --help     show this help message and exit
  --file [FILE]
```

Generates a datastream for Chantilly to evaluate deployed models on the [GoogleCloudPlatform/covid-19-open-data](https://github.com/GoogleCloudPlatform/covid-19-open-data) dataset.
