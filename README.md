# python_api

[![](https://img.shields.io/badge/Python-3.8.2-yellow.svg)](https://www.python.org/downloads/) [![](https://img.shields.io/badge/Angular-v15-1976d2.svg)](https://angular.io/) [![](https://img.shields.io/badge/Docker-blue.svg)](https://www.docker.com/) [![](https://img.shields.io/badge/Bitnami-MySQL-red.svg)](https://hub.docker.com/r/bitnami/mysql)

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

## Angular

```
npm install -g @angular/cli
```

Update:
```
ng update @angular/cli @angular/core
```

## Docker

```bash
cd ./docker
docker-compose up
```

## API Endpoints

### Negation

1. Will reject any invalid pair.

```
POST http://localhost:5000/api/logic/negation?test=1,1;0,0;1,0;0,1;1,1;0,0;1,0;0,1
```

```JSON
[
    [
        [
            1,
            1
        ],
        [
            0,
            0
        ],
        [
            1,
            1
        ],
        [
            0,
            0
        ]
    ],
    [
        [
            false,
            true,
            false,
            true
        ]
    ]
]
```

### Conjunction

```
POST http://localhost:5000/api/logic/conjunction?test=1,1;0,0;1,0;0,1;1,1;0,0;1,0;0,1
```

```JSON
[
    [
        [
            1,
            1
        ],
        [
            0,
            0
        ],
        [
            1,
            0
        ],
        [
            0,
            1
        ],
        [
            1,
            1
        ],
        [
            0,
            0
        ],
        [
            1,
            0
        ],
        [
            0,
            1
        ]
    ],
    [
        [
            true,
            false,
            false,
            false,
            true,
            false,
            false,
            false
        ]
    ]
]
```

### Implication

```
POST http://localhost:5000/api/logic/implication?test=1,1;0,0;1,0;0,1;1,1;0,0;1,0;0,1
```

```JSON
[
    [
        [
            1,
            1
        ],
        [
            0,
            0
        ],
        [
            1,
            0
        ],
        [
            0,
            1
        ],
        [
            1,
            1
        ],
        [
            0,
            0
        ],
        [
            1,
            0
        ],
        [
            0,
            1
        ]
    ],
    [
        [
            true,
            true,
            false,
            true,
            true,
            true,
            false,
            true
        ]
    ]
]
```

### Disjunction

```
POST http://localhost:5000/api/logic/disjunction?test=1,1;0,0;1,0;0,1;1,1;0,0;1,0;0,1
```

```JSON
[
    [
        [
            1,
            1
        ],
        [
            0,
            0
        ],
        [
            1,
            0
        ],
        [
            0,
            1
        ],
        [
            1,
            1
        ],
        [
            0,
            0
        ],
        [
            1,
            0
        ],
        [
            0,
            1
        ]
    ],
    [
        [
            true,
            false,
            true,
            true,
            true,
            false,
            true,
            true
        ]
    ]
]
```

### Scan Examples

```
GET http://localhost:5000/api/db/examples
```

```JSON
["{ id: 1, name: 'example_a' }","{ id: 2, name: 'example_b' }","{ id: 3, name: 'example_c' }","{ id: 4, name: 'example_d' }"]
```

### Get Example By ID

```
GET http://localhost:5000/api/db/example/1
```

```JSON
["{ id: 1, name: 'example_a' }"]
```

### Create Example

```
POST http://localhost:5000/api/db/example
```

Body `form-data`:

```
name created
```

```JSON
[
    "{ id: 5, name: 'created' }"
]
```

### Update Example By ID
```
PUT http://localhost:5000/api/db/example/1
```

Body `form-data`:
```
name updated
```

```JSON
[
    "{ id: 1, name: 'updated' }"
]
```

### Delete Example By ID

```
DELETE http://localhost:5000/api/db/example/1
```

Body `form-data`:
```
name updated
```

```JSON
[
    "{ id: 1, name: 'updated' }"
]
```

## Resources and Links

1. https://towardsdatascience.com/how-to-insert-dummy-data-into-databases-using-flask-sqlalchemy-9c59efab4527