# Copyright 2024 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Sale Order Type Email Template",
    "version": "1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "website": "https://bit.ly/numigi-com",
    "license": "AGPL-3",
    "category": "Sale",
    "depends": [
        "sale_order_type",
    ],
    "summary": "Sends different email template based on the sale order type.",
    "data": [
        "views/sale_order_type_views.xml",
    ],
    "installable": True,
}
