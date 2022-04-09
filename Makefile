db-downgrade:
	pipenv run flask db downgrade

db-history:
	pipenv run flask db history

db-migrate:
	pipenv run flask db migrate

db-upgrade:
	pipenv run flask db upgrade

local-server:
	pipenv run gunicorn SampleServer:app --bind 0.0.0.0:3000

fix-subdependencies:
	pipenv lock --pre --clear