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
# self.env['academy.session']
session_model = connection.get_model('academy.session')
partner_model = connection.get_model('res.partner')
sessions = session_model.search_read([])
attendees = partner_model.search([])[5:8]

import ipdb; ipdb.set_trace()

for session in sessions:
    print "Session %s (%s seats)" %(
        session.get('name', 'N/A'),
        session.get('number_of_seat', 'N/A'),
        )

    print "Populating sessions (%s)....         " %session.get('id'),
    if not session.get('instructor_id') or session.get('instructor_id')[0] not in attendees:
        session_model.write(session.get('id'), {
            'attendee_ids': [(0, 0, {
                'name': 'Nicola2',
                'login': 'test@example.be',
                'test_ids': [(0, 0, {
                    'test_name': 'bsfbfs',
                    })],
                })],
            })
        print "[OK]"
    else:
        print "[NOK]"
