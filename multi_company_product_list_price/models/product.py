from odoo import api, models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    list_price = fields.Float(company_dependent=True)

    @api.depends('company_id')
    def _compute_currency_id(self):
        main_company = self.env['res.company']._get_main_company()
        for template in self:
            template.currency_id = self.env.company.sudo().currency_id.id or template.company_id.sudo().currency_id.id or main_company.currency_id.id
