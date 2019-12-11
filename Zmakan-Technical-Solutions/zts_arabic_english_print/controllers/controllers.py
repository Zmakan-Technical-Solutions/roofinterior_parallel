# -*- coding: utf-8 -*-
# from odoo import http


# class /odoo13/custom/addons/ztsArabicInvoice(http.Controller):
#     @http.route('//odoo13/custom/addons/zts_arabic_invoice//odoo13/custom/addons/zts_arabic_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//odoo13/custom/addons/zts_arabic_invoice//odoo13/custom/addons/zts_arabic_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/odoo13/custom/addons/zts_arabic_invoice.listing', {
#             'root': '//odoo13/custom/addons/zts_arabic_invoice//odoo13/custom/addons/zts_arabic_invoice',
#             'objects': http.request.env['/odoo13/custom/addons/zts_arabic_invoice./odoo13/custom/addons/zts_arabic_invoice'].search([]),
#         })

#     @http.route('//odoo13/custom/addons/zts_arabic_invoice//odoo13/custom/addons/zts_arabic_invoice/objects/<model("/odoo13/custom/addons/zts_arabic_invoice./odoo13/custom/addons/zts_arabic_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/odoo13/custom/addons/zts_arabic_invoice.object', {
#             'object': obj
#         })
