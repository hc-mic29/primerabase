# -*- coding: utf-8 -*-

{
    'name': 'Datafast Payment Acquirer',
    'category': 'Accounting/Payment',
    'summary': 'Payment Acquirer: Datafast Implementation',
    'version': '1.0',
    'description': """Datafast Payment Acquirer""",
    'depends': ['payment'],
    'data': [
        'views/payment_views.xml',
        'views/payment_datafast_templates.xml',
        'data/payment_acquirer_data.xml',
        'data/payment_paypal_email_data.xml',
    ],
    'installable': True,
    'post_init_hook': 'create_missing_journal_for_acquirers',
}
