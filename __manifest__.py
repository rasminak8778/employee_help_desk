{
    'name': 'Employee Help Desk',
    'version': '17.0.1.0.0',
    'description': 'Employee can enquiry with Help Desk Team',
    'category': 'Employees/Employee Help Desk',
    'summary': 'Employee can Generate ticket through website and raise enquiry regarding the isssues in company',
    'installable': True,
    'application': True,
    'depends': [
        'hr',
        'website',
        'base'
        ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/website_helpdesk_menu.xml',
        'data/website_heldesk_list_menu.xml',
        # 'data/website_order_menu.xml',
        'views/help_desk_views.xml',
        'views/helpdesk_ticket_page_views.xml',
        'views/helpdesk_list_views.xml',
        'views/submit_ticket_views.xml',
        'views/help_desk_menu.xml',
        # 'views/order_details_views.xml',
    ]
}
