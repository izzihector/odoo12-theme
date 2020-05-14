# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name" : "Website Language Selector",
    
    "author" : "Softhealer Technologies",
        
    "website": "https://www.softhealer.com",
    
    "support": "info@softhealer.com",   

    "version":"13.0.1",

    "category": "Website",
    
    "summary": """language select website module, set website language app, add language in website, select website language odoo""",
    
    "description": """This module usefull to give language selection option in website.""",
    
    "depends" : ['website'],
    
    "data" : [
        'views/res_language.xml',
            ],            
    
    "images": ['static/description/background.png',],
                  
    "auto_install": False,
    "application" : True,    
    "installable" : True,
    
    "price": 9,
    "currency": "EUR"   
}
