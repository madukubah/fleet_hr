# -*- coding: utf-8 -*-

{
    'name': 'Fleet HR',
    'version': '1.0',
    'author': 'Technoindo.com',
    'category': 'Fleet HR Management',
    'depends': [
        'fleet',
        'hr',
    ],
    'data': [
        'views/menu.xml',
        "views/fleet_driver.xml",

        "security/ir.model.access.csv",
    ],
    'qweb': [
        # 'static/src/xml/cashback_templates.xml',
    ],
    'demo': [
        # 'demo/sale_agent_demo.xml',
    ],
    "installable": True,
	"auto_instal": False,
	"application": False,
}
