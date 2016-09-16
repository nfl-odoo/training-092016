import openerplib

HOST = 'localhost'
PORT = 8069
DB = 'test_db'
USER = 'admin'
PASS = 'admin'

connection = openerplib.get_connection(
        hostname=HOST,
        database=DB,
        login=USER,
        password=PASS,
        protocol='xmlrpc',
        port=PORT,
        )

session_model = connection.get_model('academy.session')
sessions = session_model.search_read([])

for session in sessions:
    print "Session %s (%s seats)" %(
        session.get('name', 'N/A'),
        session.get('number_of_seat', 'N/A'),
        )