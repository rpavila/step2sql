Converter STEP file to SQL

1) Execute this command to create all tables in metadata

$ python migrate.py --dialect postgresql --host localhost --dbname custom_database --username myuser --password userpassword create

2) Execute this command to delete all tables in metadata

$ python migrate.py --dialect postgresql --host localhost --dbname custom_database --username myuser --password userpassword create