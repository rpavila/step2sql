Converter STEP file to SQL

1) Create schema in database

Execute this command to create all tables in metadata

$ python migrate.py --dialect postgresql --host localhost --dbname custom_database --username myuser --password userpassword create

2) Drop schema in database

$ python migrate.py --dialect postgresql --host localhost --dbname custom_database --username myuser --password userpassword create