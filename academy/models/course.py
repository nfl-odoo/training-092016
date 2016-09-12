# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Course(models.Model):
    _name = 'academy.course'
    _rec_name = 'title'

    title = fields.Char(string='Title', required=True)
    desc = fields.Text(string='Description')
    resp_id = fields.Many2one('res.users', string='Responsible')
    session_ids = fields.One2many('academy.session', 'course_id', string="Sessions")