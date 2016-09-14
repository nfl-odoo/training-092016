# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Course(models.Model):
    _name = 'academy.course'
    _rec_name = 'title'

    title = fields.Char(string='Title', required=True)
    desc = fields.Text(string='Description')
    resp_id = fields.Many2one('res.users', string='Responsible')
    session_ids = fields.One2many('academy.session', 'course_id', string="Sessions")

    _sql_constraints = [
        (
            '_check_diff_title_desc',
            'CHECK(title != academy_course.desc)',
            'Title and Description must be different !',
            ),
        (
            '_uniq_title',
            'UNIQUE(title)',
            'Title must be unqiue !',
            ),
    ]

    @api.one
    def copy(self, default=None):
        default = default or {}
        default.update({
            'title': '%s (Copy)' %self.title,
            })
        return super(Course, self).copy(default)
