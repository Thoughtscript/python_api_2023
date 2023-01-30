#!/usr/bin/env bash

# sleep 3.5 && cd docker && docker-compose-up

cd ml && python3 ml-conjunction.py && python3 ml-disjunction.py && python3 ml-implication.py && python3 ml-negation.py &

# sleep 7.5 && cd ../reactAppSrc && npm i && npm run build-parcel-prod && npx serve &

# sleep 10.5 && cd ../reactAppSrc && npm i && npm run build-parcel-prod && npx serve &

wait