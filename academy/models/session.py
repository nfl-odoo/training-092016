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