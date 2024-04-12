# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HelpDesk(models.Model):
    """manage cleaning services"""
    _name = 'help.desk'
    _description = 'Help Desk Tickets'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Subject', required=True,
                       help='Give your problems', tracking=True)
    description = fields.Char(string='Description', help='Give details')
    employee_id = fields.Many2one('hr.employee', string='Employee',
                                  help='Employee name')
    manager_id = fields.Many2one('hr.employee', string='Manager',
                                 help='Employee Manager', readonly=True)
    website = fields.Boolean(default=False)
    state = fields.Selection(selection=[('new', 'New'), ('progress',
                                                         'In Progress'),
                                        ('hold', 'On Hold'),
                                        ('done', 'Done'), ('cancelled',
                                                           'Cancelled')],
                             default='new',
                             tracking=True)
    @api.model
    def create(self, vals):
        if vals.get('employee_id'):
            employee = self.env['hr.employee'].browse(vals['employee_id'])
            vals['manager_id'] = employee.parent_id.id
        return super(HelpDesk, self).create(vals)

    def get_ticket_url(self):
        """Function defined for getting corresponding
                records url for using website"""
        print('hi')
        menu_id = self.env.ref('emp_help_desk.menu_helpdesk_ticket_list').id
        print('menu_id', menu_id)
        action = self.env.ref(
            'emp_help_desk.help_desk_ticket_record').id
        print('action', action)
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        print('base_url',base_url)
        base_url += (
                    '/web#id=%d&cids=1&menu_id=%d&action=%d&model=help.desk&view_type=form' %
                    (self.id, menu_id, action))
        print('base_url', base_url)

        return base_url
    def action_complete(self):
        """function for button complete"""
        if (self.state == "new"):
            self.write({
                'state': "progress"
        })
        elif (self.state == "progress"):
            self.write({
                'state': "hold"
        })
        elif (self.state == "hold"):
            self.write({
                'state': "done"
        })

    def action_cancel(self):
        self.write({
            'state': "cancelled"
        })
        # self.write({'manager_id': self.env['hr.employee'].id})
