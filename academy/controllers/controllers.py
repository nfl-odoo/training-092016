# -*- coding: utf-8 -*-
from openerp import http

class Academy(http.Controller):
    @http.route('/academy/session/<model("academy.session"):session>/', auth='public', website=True)
    def session(self, session):
        return http.request.render('academy.template_session', {
            'session': session,
            })

    @http.route('/academy/course/<model("academy.course"):course>/', auth='public', website=True)
    def course(self, course):
        sessions = course.session_ids
        total_attendee = sum([session.number_attendee for session in sessions])
        return http.request.render('academy.template_course', {
            'course': course,
            'total_attendee': total_attendee,
            })

#     @http.route('/academy/academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy.listing', {
#             'root': '/academy/academy',
#             'objects': http.request.env['academy.academy'].search([]),
#         })

#     @http.route('/academy/academy/objects/<model("academy.academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy.object', {
#             'object': obj
#         })