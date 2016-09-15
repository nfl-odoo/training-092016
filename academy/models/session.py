# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError as VE
from datetime import timedelta


class Session(models.Model):
    _name = 'academy.session'

    name = fields.Char(string='Name')
    start_date = fields.Date(string='Starting Date')
    end_date = fields.Date(
        compute='_get_end_date',
        inverse='_set_end_date',
        string='Ending Date',
        store=True,
        )
    duration = fields.Integer(string='Duration')
    number_of_seat = fields.Integer(string='# Seats')
    instructor_id = fields.Many2one(
        'res.partner',
        string='Instructor',
        domain="[('is_instructor', '=', True)]",
        default=lambda self: self._get_default_instructor(),
        )
    instructor_user_id = fields.Many2one('res.users', related='instructor_id.user_id', store=True)
    course_id = fields.Many2one('academy.course', string='Course')
    attendee_ids = fields.Many2many(
        comodel_name='res.partner',
        relation='session_partner_rel',
        column1='session_id',
        column2='partner_id',
        string='Partners',
        )
    number_attendee = fields.Integer(compute='_get_number_attendee', string='Number of Attendees', store=True)
    taken_seat = fields.Float(compute='_get_taken_seat', string='Percentage Seats Taken')
    percentage_per_day = fields.Integer("Percentage per day", default=100)
    color = fields.Integer(string="Color")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done')], default='draft')

    _sql_constraints = [
        ('duration_positive', 'CHECK(duration >= 0)', 'Duration must be positive.'),
    ]

    @api.one
    @api.depends('number_of_seat', 'attendee_ids')
    def _get_taken_seat(self):
        self.taken_seat = self.number_of_seat and 100. * len(self.attendee_ids) / self.number_of_seat

    def _get_default_instructor(self):
        my_user = self.env["res.users"].search([('id', '=', self._uid)])
        my_partner = my_user.partner_id
        if not my_partner.is_instructor:
            return
        return my_partner.id

    @api.onchange('number_of_seat', 'attendee_ids')
    def _onchange_seats(self):
        def _warning(message):
            return {
                'warning': {
                    'title': "Warning",
                    'message': message,
                    }
            }

        if self.number_of_seat < 0:
            return _warning("Number of Seats must be positive.")
        if self.number_of_seat < len(self.attendee_ids):
            return _warning("You should have more seats than attendees.")

    @api.one
    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_attendees(self):
        if self.instructor_id in self.attendee_ids:
            raise VE("Instructor in Attendees !")


    @api.one
    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        if not self.start_date or not self.duration:
            return

        start = fields.Datetime.from_string(self.start_date)
        duration = timedelta(days=self.duration - 1)
        self.end_date = start + duration

    @api.one
    @api.depends('start_date', 'end_date')
    def _set_end_date(self):
        if not self.start_date or not self.end_date:
            return

        start_date =fields.Datetime.from_string(self.start_date)
        end_date = fields.Datetime.from_string(self.end_date)
        self.duration = (end_date - start_date).days + 1

    @api.one
    @api.depends('attendee_ids')
    def _get_number_attendee(self):
        self.number_attendee = len(self.attendee_ids)

    @api.one
    def set2draft(self):
        self.state = 'draft'

    @api.one
    def set2confirm(self):
        self.state = 'confirm'

    @api.one
    def set2done(self):
        self.state = 'done'

    # def auto_confirm(self):
    #     if self.taken_seat > 50 and self.state == 'draft':
    #         self.state = 'confirm'

    # def auto_confirm_vals(self, vals):
    #     if vals.get('taken_seat') > 50 and self.state == 'draft':
    #         vals.update({
    #             'state': 'confirm'
    #             })
    #     return vals

    # @api.one
    # def write(self, vals):
    #     new_vals = self.auto_confirm_vals(vals)
    #     return super(Session, self).write(new_vals)

    # @api.model
    # def create(self, vals):
    #     new_vals = self.auto_confirm_vals(vals)
    #     return super(Session, self).create(vals)

