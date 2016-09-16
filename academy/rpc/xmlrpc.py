import xmlrpclib
import datetime

HOST = 'localhost'
PORT = 8069
DB = 'test_db'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%s/xmlrpc' %(HOST, PORT)

COURSE_TITLE = 'Math'
YEAR = 2017

# Login
uid = xmlrpclib.ServerProxy('%s/common' %ROOT).login(DB, USER, PASS)
print 'Logged as %s (uid: %s)' %(USER, uid)

proxy = xmlrpclib.ServerProxy('%s/object' %ROOT)


# Reading
sessions = proxy.execute(DB, uid, PASS,
    'academy.session',
    'search_read',
    [],
    ['name', 'start_date', 'number_of_seat'],
    )

for session in sessions:
    print 'Session %s will start %s and have %s of seats' %(
        session.get('name', 'N/A'),
        session.get('start_date', 'N/A'),
        session.get('number_of_seat', 'N/A'),
        )

course_ids = proxy.execute(DB, uid, PASS, 'academy.course', 'search', [('title', '=', COURSE_TITLE)])
if not course_ids:
    raise Exception("Could not find a course with title '%s'" %COURSE_TITLE)
course_id = course_ids[0]

first_day = datetime.date(YEAR, 1, 1)
last_day = datetime.date(YEAR, 12, 31)
first_monday_diff = datetime.timedelta(days=(7-first_day.weekday())%7)
first_monday = first_day + first_monday_diff
cur_monday = first_monday
all_monday = []
while cur_monday <= last_day:
    all_monday.append(cur_monday)
    cur_monday += datetime.timedelta(days=7)

for monday in all_monday:
    monday_str = monday.strftime("%Y-%m-%d")
    print "CREATING session for monday %s...          " %monday_str,
    proxy.execute(DB, uid, PASS, 'academy.session',
        'create', {
            'name': '%s Session - %s' %(
                COURSE_TITLE,
                monday_str,
                ),
            'course_id': course_id,
            'start_date': monday_str,
            'duration': 5,
        })
    print "[OK]"
