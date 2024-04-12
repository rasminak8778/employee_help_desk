from odoo import http, _
from odoo.http import request


class WebsiteTicket(http.Controller):
    @http.route(['/helpdesk'], type='http', auth="public", website=True)
    def create_ticket_page(self):
        """function defined for employees can raise helpdesk tickets in
         webpage
        """
        employees = request.env['hr.employee'].sudo().search([])
        return (request.render
                ("emp_help_desk.online_helpdesk_ticket_registration_form",
                 {'employees': employees}))

    @http.route(['/create/ticket/'], type='http', auth="public", methods=['POST'],
                website=True)
    def create_helpdesk_ticket(self, **kw):
        """function for creating a helpdesk record in help desk module
        through website"""
        print('kw', kw)
        ticket_vals = {
            'name': kw.get('name'),
            'description': kw.get('description'),
            'employee_id': int(kw.get('employee_id')),
            'website': True
        }
        request.env['help.desk'].sudo().create(ticket_vals)
        return request.render(
            "emp_help_desk.online_helpdesk_ticket_thankyou_form", {})
