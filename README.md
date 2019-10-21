# stockapp-django-vue-docker

A basic inventory application using Django, VueJS, PostgreSQL and Docker

This system is to asses my coding skills and current level in application development using the tools and frameworks listed above.

The system uses Django Rest Framework as a backend with PostgreSQL as the database, and a seperate VueJS application for the frontend.
It was dockerized using two dockerfiles one for the frontend and one for the backend both of which are run via docker-compose.
The frontend uses Axiom to communicate to the API, and the backend has CORS Headers that allow access to all incoming requests.

Testing will be added later today
