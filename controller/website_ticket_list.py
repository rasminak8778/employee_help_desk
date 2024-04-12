from odoo import http, _
from odoo.http import request


class WebsiteTicket(http.Controller):
    @http.route(['/helpdesklist'], type='http', auth="public", website=True)
    def create_ticket_list(self):

        website_requests = request.env['help.desk'].sudo().search([])

        print('request.env.user.partner_id.id', request.env.user.partner_id.id)

        print('website_requests', website_requests)
        return request.render(
            "emp_help_desk.online_helpdesk_ticket_list_form",
            {'website_requests': website_requests})

