from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api


class many2many(models.Model):
    _name = 'many2many.many2many'
    _description = 'many2many.many2many'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()    

    test_ids = fields.Many2many(
        string='field_name',
        comodel_name='h.h',
        relation='relacion',
        column1='many_id',
        column2='h_id',
    )
    
    
   
    
    
   
    
    
    
   
    
    
    @api.model
    def default_get(self, fields):           
        domain=[('id','>','2')]       
        valor= self.env['h.h'].search(domain)
        lista=[]
        for nuevo in valor:
            lista.append(nuevo.id)
        #raise ValidationError("llego {}".format(lista))
        self.write({'h_id':[(6,0,lista)]})         
        res = super(many2many, self).default_get(fields)     
        return res
    
    
 
class nuevo(models.Model):   
    _name = 'n.n'
    _description = 'n.n'
    
    name = fields.Char(
        string='nombre',
    )
    
    
    
    

class History(models.Model):   
    _name = 'h.h'
    _description = 'h.h'
    

    name = fields.Char(
        string='nombre',
    )
    modulo = fields.Char(
        string='modulo',
    )

    modelo = fields.Char(
        string='modelo',
    )

    nuevo_campo="proband"

    campo = fields.Char(
        string='campo',
    )

    anterior = fields.Char(
        string='anterior',
    )

    actual = fields.Char(
        string='actual',
    )

   
        
        



    
  
    
    