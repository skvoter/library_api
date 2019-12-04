# library_api

To run tests:

`docker-compose -p test run -p 8000 
--rm web-django py.test`

> We could use separate docker-compose.test.yml file but since this project doesn't really big we can just use the prefix

To run service:

`docker-compose up`

> All the variables are passed to docker-compose file and to the Dockerfile from the `.env` . Usually we dont wanna share files like this through GitHub 

> Bitnami postgresql images are used since they support replication out of the box and are actively supported

Also to support replication inside of the django i've used yandex's [django_replicated](https://github.com/yandex/django_replicated/) module since it's working and fully covered with tests. It provides middleware and decorators to ensure that all the data retrieval goes from the replica database and writings are happening at the master one. This feature is not covered by tests as the module is already covered by them.

Service has 3 endpoints:

* `/api/reader?id=<id>` - get reader info and all the books assigned to them
* `/api/export_readers_csv/` - get CSV file with all the readers info
* `/api/export_books_csc/` - get CSV file with all the books info

