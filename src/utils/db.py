import toml
from sqlmodel import Session, create_engine, text
from psycopg2 import OperationalError, DatabaseError


def database_connection(connection_name: str) -> Session:
    try:
        with open('secrets.toml', 'r') as secrets:
            config = toml.load(secrets)
            _DIALECT = config[connection_name]['dialect']
            _HOST = config[connection_name]['host']
            _PORT = config[connection_name]['port']
            _DATABASE = config[connection_name]['database']
            _USERNAME = config[connection_name]['username']
            _PASSWORD = config[connection_name]['password']

        engine = create_engine(f'{_DIALECT}://{_USERNAME}:{_PASSWORD}@{_HOST}:{_PORT}/{_DATABASE}')
        return Session(engine)

    except (FileNotFoundError, KeyError, ValueError, OperationalError, DatabaseError) as e:
        print(f"Hahahaha: {e}")
        raise

# if __name__ == '__main__':
#     user = User('123', 'Habib', 'hahmed.y2k@gmail.com', 'password', 'student')
#     session = database_connection('postgresql')
#     session.add(user)
