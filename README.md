# Python REST API

* This source code provides a minimal REST API implementation with FastAPI

## Swagger
  * \<url>/docs

## Commands
* **installation:** `make install` *install all packages from requirements*
* **run:** `make run` *build swagger definitions and starts the server on development mode listening to file changes*
* **lint:** `make lint` *linter rules with flake8*
* **test:** `make test` *unit and integration tests*
* **build:** `make build` *build docker image with latest change*
* **deploy:** `make deploy` *run docker deploy*

## Scaffolding
* authentication `authentication abstraction`
* config `server settings, DB connection, Logger, etc`
* controllers `routes configuration`
* database `setup database connection and register orm models`
* models `classes representing entities. They are also used to normalize data`
* schemas `classes that allows fastapi document swagger input/output routes`
* respositories `data abstraction layers`
* * psql `psql repos`
* services `business logic to be used primary by controllers`
* setup `migrations and seeds for all dbs`
* utils
* tests `test setup`

## Technologies
* [Uvicorn](https://www.uvicorn.org/) - Lightning-fast ASGI server
* [FastApi](https://fastapi.tiangolo.com/) - Api framework
* [SqlAlchemy](https://www.sqlalchemy.org/) - Database ORM
* [PyTest](https://docs.pytest.org/en/stable/) - Testing Framework library
* [MakeFile](https://www.gnu.org/software/make/manual/html_node/Simple-Makefile.html) - Task Runner

## Requirements
* python >= 3.7
* pip >= 3.7

## Recommendations
* Use virtualenv to manage dependencies per project. (Virtualenvwrapper is recommended)