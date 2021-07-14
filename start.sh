#!/bin/bash

chantilly init regression
chantilly run --host=0.0.0.0 &
BOARD_PID=$!

jupyter lab --NotebookApp.token='' --ip=0.0.0.0 --port=8888 --allow-root

kill $BOARD_PID
