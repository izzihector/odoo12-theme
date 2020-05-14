# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields,models

class ResLanguage(models.Model):
    _inherit = 'res.lang'
        
    image =fields.Binary("Flag")
     
