 # -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class FleetDriver(models.Model):
	_name = "fleet.driver"

	name = fields.Char(string="Name", size=100 , required=True)
	partner_id	= fields.Many2one('res.partner', string='Res Partner', required=True )
	employee_id	= fields.Many2one('hr.employee', string='Employee', required=True )

	_sql_constraints = [
		('cek_unik_partner','UNIQUE(partner_id)','Driver Must be Unique'),
		('cek_unik_employee','UNIQUE(employee_id)','Employee Must be Unique')
	]

	@api.onchange('partner_id')	
	def _change_partner_id(self):
		for record in self:
			record.name = record.partner_id.name

