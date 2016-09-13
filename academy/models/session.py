# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Session(models.Model):
    _name = 'academy.session'

    name = fields.Char(string='Name')
    start_date = fields.Date(string='Starting Date')
    duration = fields.Integer(string='Duration')
    number_of_seat = fields.Integer(string='# Seats')
    instructor_id = fields.Many2one('res.partner', string='Instructor')
    course_id = fields.Many2one('academy.course', string='Course')
    attendee_ids = fields.Many2many(
        comodel_name='res.partner',
        relation='session_partner_rel',
        column1='session_id',
        column2='partner_id',
        string='Partners',
        )


# class SessionPartnerRel(models.Model):
#     _name = 'session_partner_rel'

#     status = fields.Selection([
#         ('100', 'Sure To Come !'),
#         ('75', 'Almost Sure'),
#         ('50', 'Maybe'),
#         ('25', 'Not Likely'),
#         ('0', 'Nope!'),
#         ], string='Status')


