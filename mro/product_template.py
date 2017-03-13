# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2017 CodUP (<http://codup.com>).
#
##############################################################################

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _name = "product.template"
    _inherit = "product.template"

    @api.multi
    @api.depends('categ_id')
    def _check_category(self):
        parts_category = self.env.ref('mro.product_category_mro', raise_if_not_found=False)
        for product in self:
            product.is_parts = product.categ_id.id == parts_category.id

    is_parts = fields.Boolean(compute='_check_category', store=True)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
