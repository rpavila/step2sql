import argparse
from schema import *

__author__ = 'rpavila'

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Database schema migrations.')
    parser.add_argument('--dialect', help='Dialect is a database name such as \'mysql\', \'oracle\', \'postgresql\' etc.')
    parser.add_argument('--driver', help='Driver is the name of a DBAPI, such as \'psycopg2\', \'pyodbc\', \'cx_oracle\', etc.')
    parser.add_argument('--host', default='localhost', help='Database hostname')
    parser.add_argument('--dbname', help='Database name')
    parser.add_argument('--username', help='Username to database connection')
    parser.add_argument('--password', help='Password to database connection')
    parser.add_argument('--port', help='Database port')
    parser.add_argument('operation', help='Operation to execute schema migrations, such as \'create\' or \'drop\' ')

    args = parser.parse_args()

    engine = create_engine('%s%s://%s:%s@%s/%s' % (args.dialect, '' if args.driver is None else '+' + args.driver, args.username, args.password, args.host, args.dbname))
    if args.operation == 'create':
        Base.metadata.create_all(engine)
    elif args.operation == 'drop':
        Base.metadata.drop_all(engine)
    else:
        print 'Unknow operation [%s]' % (args.operation)
        parser.print_help()