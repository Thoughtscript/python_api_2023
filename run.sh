#!/usr/bin/env bash

# sleep 3.5 && cd docker && docker-compose-up

cd ml && python3 ml-conjunction.py && python3 ml-disjunction.py && python3 ml-implication.py && python3 ml-negation.py &

sleep 3.5 && cd angular && npm i && ng serve -o &

sleep 5.5 && cd server && python3 main.py &

wait