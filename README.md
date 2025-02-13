# python_api

[![](https://img.shields.io/badge/Python-3.8.2-yellow.svg)](https://www.python.org/downloads/) [![](https://img.shields.io/badge/Angular-v15-1976d2.svg)](https://angular.io/) [![](https://img.shields.io/badge/Docker-blue.svg)](https://www.docker.com/) [![](https://img.shields.io/badge/Bitnami-MySQL-red.svg)](https://hub.docker.com/r/bitnami/mysql)

This example is actually three examples in one (sorry, crunched for time!):

1. A basic CRUD REST API with backing database and minimum viable User Interface built in Angular.
2. A suite of [Machine Learning models](backend/ml/README.md) built to *teach* a computer how to use (Classical, [Zero Order](https://www.thoughtscript.io/papers/000000000001)) logic (*Statistically*, through Linear Regression rather than to stipulate Boolean Algebra as such through *Imperative* programming languages) whilst adding XOR, NAND, and Biconditional. Philosophically this aligns with [Putnam's](https://philpapers.org/rec/PUTILE) approach.
    * Unit Tests are supplied in the Python scripts.
3. To expose those Machine Learning models through an API accessible only through [Postman](postman/Python%20ML%20API.postman_collection.json) since examples about how to do this easily seem lacking.
    * Integration Tests are defined in the Postman Collection.

## Use

Run the following from the root dir:

```bash
docker-compose up

# If using Docker Compose Engine V2:
docker compose up
```

That should spin up each subservice. Otherwise, you can launch each service individually by:

1. Commenting out everything in `docker-compose.yml` except for:

    ```yml
    services:
      mysql:
       image: 'bitnami/mysql:8.0'
      ports:
        - '3306:3306'
      environment:
        - ALLOW_EMPTY_PASSWORD=yes
        - MYSQL_USER=example
        - MYSQL_PASSWORD=example
        - MYSQL_DATABASE=example
        - MYSQL_AUTHENTICATION_PLUGIN=mysql_native_password
    ```

    Then launching the MySQL subservice via `docker-compose up`.
2. From within `/angular` run `npm i && npm i angular/cli -g`, then `ng serve -o` to spin up the Angular frontend.
3. From within `/backend` run:

    ```bash
    cd ml 
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    python3 ml-conjunction.py
    python3 ml-disjunction.py 
    python3 ml-implication.py
    python3 ml-negation.py
    python3 ml-nand.py
    python3 ml-xor.py
    python3 ml-biconditional.py
    python3 ml-triviality-f.py
    python3 ml-triviality-t.py
    python3 ml-nor.py
    ```

   To generate the Machine Learning models.

4. Lastly, to start the backend service - from within `/backend` run:

    ```bash
    cd backend 
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    python3 main.py
    ```

> Generally speaking, the necessary config, settings, and commands are available within [docker-compose.yml](docker-compose.yml), backend [dockerfile](backend/dockerfile), frontend [dockerfile](angular/dockerfile), [angular.json](angular/angular.json), and [main.py](backend/server/main.py), respectively. So, please make recourse to those if you encounter problems.

## Notes

> **NOTE**: `MYSQL_AUTHENTICATION_PLUGIN=mysql_native_password` is deprecated in `8.4` - for now I've pinned the version to `8.0` which is likely the closest to what I was using in early Spring 2024 - you may need to clean your local images and volumes via something like `docker system prune --volumes` since the Bitnami container may throw the following error message otherwise: `The designated data directory /bitnami/mysql/data/ is unusable.`) 

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

Generates Boolean, bivalent, classical, logic results from ***Deep Learning Linear Regression*** models (it doesn't use in-built programmatic, native, Boolean clauses or ***Automated Theorem Proving*** techniques). 

Also, inferences are included that exceed the standard Boolean operations (**Material Conditional**/**Implication**, **Conjunction**, **Disjunction**, **Negation** - for example: **NAND**).

> This mirrors research into how one might try to ***teach*** a computer logic ***rather than just stipulate how logic works*** like we do within programming languages. Read more [here](backend/ml/README.md).

1. **Negation**
    * "NOT" - Reverses the truth value of the supplied expression.
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
    * "AND" - Evaluates `True` only if both conjuncts are `True`.
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
    * "Material Implication" - Evaluates `False` only if the antecedant is `True` and the consequent `False`. (Not to be confused with the imperative conditional - e.g. `if { ... }` in most programming languages.)
    * Supply sequences of `0,1` (antecedant `False`, consequent `True`), `1,1` (antecedant `True`, consequent `True`), `1,0` (antecedant `True`, consequent `False`), `0,0` (antecedant `False`, consequent `False`).
    * Each result will contain two parts with each entry in the first mapped to the result in the second by same index:  
        * `1,0` at index `i` will map to `false` at index `i`.
    * Docker `POST http://localhost:5001/api/logic/implication?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`
    * Standalone `POST http://localhost:5000/api/logic/implication?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`

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
    * "OR" - Evaluates `True` if either disjunct is `True` (or both).
    * Supply sequences of `0,1` (left disjunct `False`, right disjunct `True`), `1,1` (left disjunct `True`, right disjunct `True`), `1,0` (left disjunct `True`, right disjunct `False`), `0,0` (left disjunct `False`, right disjunct `False`).
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
    * "NOT-AND" - Evaluates `True` only if the expression isn't a `True` **Conjunction**.
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

1. **XOR**
    * "Exclusive OR" - Evaluates `True` only if neither disjunct is the same. (Evaluates `True` if either disjunct is `True` but not both.)
    * Supply sequences of `0,1` (left disjunct `False`, right disjunct `True`), `1,1` (left disjunct `True`, right disjunct `True`), `1,0` (left disjunct `True`, right disjunct `False`), `0,0` (left disjunct `False`, right disjunct `False`).
    * Each result will contain two parts with each entry in the first mapped to the result in the second by same index:  
        * `1,0` at index `i` will map to `true` at index `i`.
    * Docker `POST http://localhost:5001/api/logic/xor?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1|0,0|1,0|1,0|0,1`
    * Standalone `POST http://localhost:5000/api/logic/xor?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1|0,0|1,0|1,0|0,1`

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
                false,
                true,
                true,
                false,
                false,
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

1. **Biconditional**
    * "Two Directional Material Conditionals" ("Necessary and Sufficient") - Evaluates `True` if both sides are the same.
    * Supply sequences of `0,1` (left side `False`, right side `True`), `1,1` (left side `True`, right side `True`), `1,0` (left side `True`, right side `False`), `0,0` (left side `False`, right side `False`).
    * Each result will contain two parts with each entry in the first mapped to the result in the second by same index:  
        * `1,0` at index `i` will map to `false` at index `i`.
    * Docker `POST http://localhost:5001/api/logic/biconditional?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1|0,0|1,0|1,0|0,1|0,0|1,1`
    * Standalone `POST http://localhost:5000/api/logic/biconditional?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1|0,0|1,0|1,0|0,1|0,0|1,1`

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
                1,
                0
            ],
            [
                0,
                1
            ],
            [
                0,
                0
            ],
            [
                1,
                1
            ]
        ],
        [
            [
                true,
                true,
                false,
                false,
                true,
                true,
                false,
                false,
                true,
                false,
                false,
                false,
                true,
                true
            ]
        ]
    ]
    ``` 

1. **Triviality-T**
    * "Triviality-T" - Evaluates `True` regardless. (Consequence of the [Principle of Explosion](https://dimap.ufrn.br/~jmarcos/papers/JM/01-CM-ECNSQL.pdf) or *ex contradictione sequitur quodlibet* or *Triviality* - a logic that collapses into *Triviality* is insufficient for reasoning. Also, here to better fill out the [Hasse Diagram](http://finitegeometry.org/sc/16/logic.html) and Lattice.)
    * Supply sequences of `0,1` (left argument `False`, right argument `True`), `1,1` (left argument `True`, right argument `True`), `1,0` (left argument `True`, right argument `False`), `0,0` (left argument `False`, right argument `False`).
    * Each result will contain two parts with each entry in the first mapped to the result in the second by same index:  
        * `1,0` at index `i` will map to `true` at index `i`.
    * Docker `POST http://localhost:5001/api/logic/trivialityt?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`
    * Standalone `POST http://localhost:5001/api/logic/trivialityt?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`

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
                true,
                true,
                true,
                true,
                true,
                true,
                true
            ]
        ]
    ]
    ``` 

1. **Triviality-F**
    * "Triviality-F" - Evaluates `False` regardless. (Consequence of the [Principle of Explosion](https://dimap.ufrn.br/~jmarcos/papers/JM/01-CM-ECNSQL.pdf) or *ex contradictione sequitur quodlibet* or *Triviality* - a logic that collapses into *Triviality* is insufficient for reasoning. Also, here to better fill out the [Hasse Diagram](http://finitegeometry.org/sc/16/logic.html) and Lattice.)
    * Supply sequences of `0,1` (left argument `False`, right argument `True`), `1,1` (left argument `True`, right argument `True`), `1,0` (left argument `True`, right argument `False`), `0,0` (left argument `False`, right argument `False`).
    * Each result will contain two parts with each entry in the first mapped to the result in the second by same index:  
        * `1,0` at index `i` will map to `false` at index `i`.
    * Docker `POST http://localhost:5001/api/logic/trivialityt?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`
    * Standalone `POST http://localhost:5001/api/logic/trivialityt?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`

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
                false,
                false,
                false,
                false,
                false,
                false,
                false
            ]
        ]
    ]
    ``` 

1. **NOR***
    * "Neither Nor" - Evaluates `True` only if neither disjunct is `True`.
    * Supply sequences of `0,1` (left disjunct `False`, right disjunct `True`), `1,1` (left disjunct `True`, right disjunct `True`), `1,0` (left disjunct `True`, right disjunct `False`), `0,0` (left disjunct `False`, right disjunct `False`).
    * Each result will contain two parts with each entry in the first mapped to the result in the second by same index:  
        * `1,0` at index `i` will map to `false` at index `i`.
    * Docker `POST http://localhost:5001/api/logic/nor?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`
    * Standalone `POST http://localhost:5001/api/logic/nor?test=1,1|0,0|1,0|0,1|1,1|0,0|1,0|0,1`

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
                false,
                false,
                false,
                true,
                false,
                false
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
