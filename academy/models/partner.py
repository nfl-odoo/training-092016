# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    is_instructor = fields.Boolean(string="Instructor")
    session_ids = fields.Many2many(
        comodel_name='res.partner',
        relation='session_partner_rel',
        column1='partner_id',
        column2='session_id',
        string='Session',
        )


    # expr="//field[@name='supplier']/../../.." position="after"
    # expr="//notebook" position="inside"