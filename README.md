# API-Demo
Demo for building a RESTful API with Flask


# Setup
**Python setup**
install python
`wget  https://bootstrap.pypa.io/get-pip.py`
`python3 get-pip.py`
`python3 -m pip install pipenv`

**App setup**
`pipenv install`
`cp .env.example .env`
*update env variables*
`make db-upgrade`
`make local-server`