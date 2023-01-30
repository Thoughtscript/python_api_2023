# python_api

[![](https://img.shields.io/badge/Python-3.8.2-yellow.svg)](https://www.python.org/downloads/) [![](https://img.shields.io/badge/React-18.2.0-orange.svg)](https://reactjs.org) [![](https://img.shields.io/badge/parcel-2.7.0-royalblue.svg)](https://parceljs.org/) [![](https://img.shields.io/badge/Docker-blue.svg)](https://www.docker.com/)

## Python3

To install dependencies into a [Python 3.8.2](https://www.python.org/downloads/) **Virtual Environment** (venv):

```bash
python3 -m pip install --upgrade pip
python3 -m venv MY_ENV
source MY_ENV/Scripts/activate
```

Then, after activating the selected environment:

```bash
python3 -m pip install -r requirements.txt
```

```bash
pip install numpy
```

Verify versions using:

```bash
pip freeze
```

Clear environment PIP dependencies:

```bash
pip uninstall -y -r <(pip freeze)
```

## Docker

```bash
cd ./docker
docker-compose up
```