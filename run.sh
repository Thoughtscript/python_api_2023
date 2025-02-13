#!/usr/bin/env bash

echo 'The following represent how to run the scripts in python or js without docker (you will still need to spin up the database):'
echo
echo "'''"
echo 'cd backend/ml && python3 ml-conjunction.py &'
echo 'cd backend/ml && python3 ml-disjunction.py &'
echo 'cd backend/ml && python3 ml-implication.py &'
echo 'cd backend/ml && python3 ml-negation.py &'
echo 'cd backend/ml && python3 ml-nand.py &'
echo 'cd backend/ml && python3 ml-xor.py &'
echo 'cd backend/ml && python3 ml-biconditional.py &'
echo 'sleep 3.5 && cd angular && npm i && ng serve -o &'
echo 'sleep 5.5 && cd backend/server && python3 main.py &'
echo 'wait'
echo "'''"
echo 

# If using Docker Compose Engine V2 uncomment:
# docker compose up
docker-compose up