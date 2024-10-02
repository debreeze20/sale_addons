# -*- coding: utf-8 -*-
{
    "name": "Product Template Custom SP",
    "summary": "Short (1 phrase/line) summary of the module's purpose",
    "description": """
Long description of module's purpose
    """,
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    "category": "Uncategorized",
    "version": "0.1",
    "depends": ["base", "product",],
    "data": [
        "data/product_attribute_custom.xml",
        "data/punch_hole_data.xml",
        "security/ir.model.access.csv",
        "views/product_product_custom_views.xml",
        "views/product_template_custom_view.xml",
        "views/material_film_info_view.xml",
        "views/product_template_attribute_value_custom_view.xml",
        "views/product_attribute_value_custom_view.xml",
        "views/product_product_custom_views.xml",
        'views/res_partner_view.xml',
    ],
}
