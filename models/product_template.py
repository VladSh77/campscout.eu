from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def get_camp_availability(self):
        # Пошук пов'язаних активних подій (заїздів)
        event_tickets = self.env['event.event.ticket'].search([
            ('product_id', 'in', self.product_variant_ids.ids)
        ])
        events = event_tickets.mapped('event_id').filtered(lambda e: e.date_begin >= fields.Datetime.now())
        total_remaining = sum(events.mapped('seats_available'))
        return total_remaining
