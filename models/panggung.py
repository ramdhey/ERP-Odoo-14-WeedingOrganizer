from odoo import api, fields, models


class Panggung(models.Model):
    _name = 'wedding.panggung'
    _description = 'Atribut di Pangung'

    name = fields.Char(string='Nama',required=True)

    pelaminan = fields.Many2one(comodel_name='wedding.pelaminan', string='Tipe Pelaminan' , required=True,
    #Untuk memfilter yang harga nyalebih besar dari 100jt saja yang dapat muncul dengan cara berikut:
    #domain="[('harga','>','100000000')]")
    )
    
    bunga = fields.Selection(string='Tipe Bunga', selection=[('bunga mati','bunga hidup'),('bunga hidup','bunga mati')])
    
    accesoris = fields.Char(string='Accesoris Pelaminan')
    harga = fields.Char(compute='_compute_harga', string='Harga')
    
    @api.depends('pelaminan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.pelaminan.harga

    
    
    
