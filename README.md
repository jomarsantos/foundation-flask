# foundation-flask
Boiler plate for a Python/Flash REST API

## Setup via Docker
- Make sure you have Docker installed
- Run `docker-compose up`
- Use `docker ps` to check containers are up and running
- Use `docker-compose down` to shut down containers

## Database Migrations
- `docker ps` to get the id of app container
- `docker exec -it <id> bash`
- `flask db migrate`
- `flask db upgrade`
