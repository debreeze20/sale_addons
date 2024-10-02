# -*- coding: utf-8 -*-

{
    "name": "Sales Custom Breef Studio",
    "version": "17.0.0.0",
    "category": "",
    "summary": "Sales Custom Breef Studio",
    "description": """ Sales Custom Breef Studio

    """,
    "author": "Breef Studio",
    "website": "breefstudio.com",
    "price": 1000,
    "currency": "USD",
    "depends": [
        "base",
        "company_custom",
        "hr",
        "sale",
    ],
    "data": [
        "views/sale_custom_views.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'static/src/js/sale_order_custom.js',
        ],
    },
    "qweb": [],
    "auto_install": False,
    "installable": True,
}
