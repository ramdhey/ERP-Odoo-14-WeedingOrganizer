from odoo import api, fields, models


class Partner(models.Model):
    _name = 'wedding.partner'
    _description = 'Class Partner'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    notelp = fields.Char(string='No.Telp')
    
    
    
