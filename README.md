Copy environments from [.env.example](.env.example) to .env

Then run the command: 
```sh
docker-compose up --build
```

WARNING: you will not be able to use this application unless you have an [authentication-sync](https://github.com/gmalanchuk/authentication-sync) container running

If you want to populate the database with data:
```sh
docker-compose exec task sh
python manage.py loaddata database.json
```

If you want to use the pre-commit:
```sh
pre-commit install
```

Documentation address: http://localhost:8000/api/docs/
