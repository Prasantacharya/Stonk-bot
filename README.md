# BoilerplateDiscordBot

BoilerplateDiscordBot is a boilerplate Discord Bot built based on my work on [BakedBeansBot](https://github.com/genericon/BakedBeansBot), [ComputerMan](https://github.com/johnnyapol/ComputerMan), and [Bonobot](https://github.com/chrisj1/Bonobot).

## Requirements

- [Python 3.8](https://www.python.org/downloads/)
- [`pipenv`](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv)

### Using Docker

Using Docker is generally recommended (but not stricly required) because it abstracts away some additional set up work.

The requirements for Docker are:

- [Docker CE](https://docs.docker.com/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup

You should create a `.env` file based on `example.env`. to pass environment variables (e.g. Discord Bot Token) to your program.

```
pipenv install # For creating a virtualenv
```

## Run the project

The project can either be run via `pipenv` or `docker-compose`.

### Run on the host

```
pipenv run start
```

### Run with Docker

```
pipenv run docker
```
