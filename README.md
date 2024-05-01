# python_api

[![](https://img.shields.io/badge/Python-3.8.2-yellow.svg)](https://www.python.org/downloads/) [![](https://img.shields.io/badge/Angular-v15-1976d2.svg)](https://angular.io/) [![](https://img.shields.io/badge/Docker-blue.svg)](https://www.docker.com/) [![](https://img.shields.io/badge/Bitnami-MySQL-red.svg)](https://hub.docker.com/r/bitnami/mysql)

Run the following from the root dir:

```bash
docker-compose up
```

That should spin up each subservice. (**NOTE:** the `backend` service will continually restart until the `mysql` service has fully initialized) Otherwise you can launch each service individually by:

1. Commenting out everything in `docker-compose.yml` except for:

    ```yml
    services:
      mysql:
       image: 'bitnami/mysql:latest'
      ports:
        - '3306:3306'
      environment:
        - ALLOW_EMPTY_PASSWORD=yes
        - MYSQL_USER=example
        - MYSQL_PASSWORD=example
        - MYSQL_DATABASE=example
        - MYSQL_AUTHENTICATION_PLUGIN=mysql_native_password
    ```

    Then launching the MySQL subservice via `docker-compose-up`.
1. From within `/angular` run `npm i && npm i angular/cli -g`, then `ng serve -o` to spin up the Angular frontend.
1. From within `/backend` run:

    ```bash
    cd ml 
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    python3 ml-conjunction.py
    python3 ml-disjunction.py 
    python3 ml-implication.py
    python3 ml-negation.py
    ```

   To generate the Machine Learning models.

1. Lastly, to start the backend service - from within `/backend` run:

    ```bash
    cd backend 
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    python3 main.py
    ```

> Generally speaking, the necessary config, settings, and commands are available within [docker-compose.yml](docker-compose.yml), backend [dockerfile](backend/dockerfile), frontend [dockerfile](angular/dockerfile), [angular.json](angular/angular.json), and [main.py](backend/server/main.py) respectively. So make recourse to those if you encounter problems.

## Angular Frontend

Will be exposed on:
* Docker: `http://localhost:4201`
* Standalone: `http://localhost:4200`

## API Endpoints

API endpoints are exposed through Docker or by running each subservice individually.

### Test API

A test endpoint to verify that requests are getting through and the app is exposed correctly through Docker:
* Docker `http://localhost:5001/api/hello`
* Standalone `http://localhost:5000/api/hello`

### Logic API

Generates Boolean, bivalent, classical, logic results from ***Deep Learning Linear Regression*** models (it doesn't use simple programmatic, *native*, Boolean clauses or ***Automated Theorem Proving*** techniques). Also, inferences that exceed the standard Boolean operations (**Material Conditional**/**Implication**, **Conjunction**, **Disjunction**, **Negation** - for example, adding **NAND**).

> This mirrors research into how one would ***teach*** a computer logic ***rather than stipulate how logic works*** like we do within programming languages. Read more [here](backend/ml/README.md).

1. **Negation**
    * Supply sequences of `0,0` (`False`) or `1,1` (`True`)
    * Will reject any invalid pair (e.g. - `1,0`, `0,1`)
    * Each result will contain two parts with each entry in the first mapped to the result in the second by same index:
        * `1,1` at index `i` will map to `false` at index `i`.
    * Docker: `POST http://localhost:5001/api/logic/negation?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`
    * Standalone: `POST http://localhost:5000/api/logic/negation?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`

    Response:
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

1. **Conjunction**
    * Supply sequences of `0,1` (left conjunct `False`, right conjunct `True`), `1,1` (left conjunct `True`, right conjunct `True`), `1,0` (left conjunct `True`, right conjunct `False`), `0,0` (left conjunct `False`, right conjunct `False`).
    * Each result will contain two parts with each entry in the first mapped to the result in the second by same index:  
        * `1,1` at index `i` will map to `true` at index `i`.
    * Docker `POST http://localhost:5001/api/logic/conjunction?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`
    * Standalone `POST http://localhost:5000/api/logic/conjunction?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`

    Response:
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

1. **Implication**
    * Supply sequences of `0,1` (antecedant `False`, consequent `True`), `1,1` (antecedant `True`, consequent `True`), `1,0` (antecedant `True`, consequent `False`), `0,0` (antecedant `False`, consequent `False`).
    * Each result will contain two parts with each entry in the first mapped to the result in the second by same index:  
        * `1,0` at index `i` will map to `false` at index `i`.
    * Docker `POST http://localhost:5001/api/logic/implication?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`
    * Standalone `POST http://localhost:5000/api/logic/implication?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`

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

1. **Disjunction**
    * Supply sequences of `0,1` (left conjunct `False`, right conjunct `True`), `1,1` (left conjunct `True`, right conjunct `True`), `1,0` (left conjunct `True`, right conjunct `False`), `0,0` (left conjunct `False`, right conjunct `False`).
    * Each result will contain two parts with each entry in the first mapped to the result in the second by same index:  
        * `1,0` at index `i` will map to `true` at index `i`.
    * Docker `POST http://localhost:5001/api/logic/disjunction?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`
    * Standalone `POST http://localhost:5000/api/logic/disjunction?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`

    Response:
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

1. **NAND**
    * Supply sequences of `0,1` (left conjunct `False`, right conjunct `True`), `1,1` (left conjunct `True`, right conjunct `True`), `1,0` (left conjunct `True`, right conjunct `False`), `0,0` (left conjunct `False`, right conjunct `False`).
    * Each result will contain two parts with each entry in the first mapped to the result in the second by same index:  
        * `1,0` at index `i` will map to `true` at index `i`.
    * Docker `POST http://localhost:5001/api/logic/nand?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`
    * Standalone `POST http://localhost:5000/api/logic/nand?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`

    Response:
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
                false,
                true,
                true,
                true,
                false,
                true,
                true,
                true
            ]
        ]
    ]
    ```

### DB API

Supports RESTful CRUD (***CREATE***, ***READ***, ***UPDATE***, ***DELETE***) operations against a backing MySQL DB.

> Check out the [Example SQL Domain](backend/server/domain/__init__.py) entry.

1. **Scan**
    * Retrieve all prepopulated entries from the MySQL DB.
    * Docker `GET http://localhost:5001/api/db/examples`
    * Standalone `GET http://localhost:5000/api/db/examples`

    Response:
    ```JSON
    ["{ id: 1, name: 'example_a' }","{ id: 2, name: 'example_b' }","{ id: 3, name: 'example_c' }","{ id: 4, name: 'example_d' }"]
    ```

1. **Get One**
    * Retrieve one Example by ID.
    * Docker `GET http://localhost:5001/api/db/example/1`
    * Standalone `GET http://localhost:5000/api/db/example/1`

    Response:
    ```JSON
    ["{ id: 1, name: 'example_a' }"]
    ```

1. **Create Example**
    * Create an Example with `form-data`.
    * Docker `POST http://localhost:5001/api/db/example`
    * Standalone `POST http://localhost:5000/api/db/example`

    Request Body `form-data`:

    ```
    name created
    ```
    Response:

    ```JSON
    [
        "{ id: 5, name: 'created' }"
    ]
    ```

1. **Update Example**
    * Update an Example by ID
        * Docker `PUT http://localhost:5001/api/db/example/1`
        * Standalone `PUT http://localhost:5000/api/db/example/1`

    Request Body `form-data`:

    ```
    name updated    
    ```

    Response:
    ```JSON
    [
        "{ id: 1, name: 'updated' }"
    ]
    ```

1. **Delete Example**
    * Delete an Example by ID
        * Docker `DELETE http://localhost:5001/api/db/example/1`
        * Standalone `DELETE http://localhost:5000/api/db/example/1`

    Request Body `form-data`:
    ```
    name updated
    ```
    Response:
    ```JSON
    [
        "{ id: 1, name: 'updated' }"
    ]
    ```

## Resources and Links

1. https://towardsdatascience.com/how-to-insert-dummy-data-into-databases-using-flask-sqlalchemy-9c59efab4527