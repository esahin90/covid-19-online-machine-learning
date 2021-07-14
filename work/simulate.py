import argparse
import datetime as dt
import time

from creme import metrics
from creme import stream
import numpy as np
import requests

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('speed_up', type=int, nargs='?', default=1)
    args = parser.parse_args()

    def sleep(td: dt.timedelta):
        if td.seconds >= 0:
            time.sleep(td.seconds / args.speed_up)


    def parse_float(val):
        if val:
            return float(val)
        else:
            return float("nan")

    params = {
        'target': 'new_confirmed',
        'converters': {col: parse_float
                       for col in ['new_confirmed', 'new_deceased', 'new_recovered',
                                   'new_tested', 'cumulative_confirmed', 'cumulative_deceased',
                                   'cumulative_recovered', 'cumulative_tested']},
        'parse_dates': {'date': '%Y-%m-%d'}
    }

    host = 'http://localhost:5000'
    mae = metrics.MAE()

    for i, (x, y) in enumerate(stream.iter_csv('epidemiology.csv', **params)):
        if any(isinstance(val, float) and np.isnan(val) for _, val in x.items()):
            continue

        sleep(dt.timedelta(seconds=1))
        features_dict = dict(x, date=x['date'].isoformat())

        r = requests.post(host + '/api/predict', json={
            'id': i,
            'features': features_dict
        })
        y_pred = r.json()["prediction"]
        print(f"{x['date'].timestamp()} - predicated new cases: {y_pred}")

        learn_request = requests.post(host + '/api/learn', json={'id': i, 'ground_truth': y})
        mae.update(y_true=y, y_pred=y_pred)

        print(f"Mean absolute error: {mae.get()}")
