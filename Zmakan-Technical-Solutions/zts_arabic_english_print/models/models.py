# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
	_inherit = 'product.template'

	arab_name = fields.Char(String="Arabic Name")
