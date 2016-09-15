# -*- coding: utf-8 -*-

from openerp import models, fields, api


class SessionPopulate(models.TransientModel):
    _name = 'academy.session.populate'

    session_ids = fields.Many2many(
        'academy.session',
        string='Sessions',
        default=lambda self: self.env['academy.session'].browse(
            self._context.get('active_ids'),
            ),
        )
    attendee_ids = fields.Many2many(
        'res.partner',
        string='Partners',
        )

    @api.multi
    def add_attendee(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids


