Copy environments from [.env.example](.env.example) to .env

Then run the command: 
```sh
docker-compose up --build
```

If you want to populate the database with data:
```sh
docker-compose exec task sh
python manage.py loaddata database.json
```
