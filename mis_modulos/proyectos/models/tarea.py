# -*- coding:utf-8 -*-

from odoo import fields, models

class Tarea(models.Model):
  # El nombre técnico del modelo, usualmente en formato 'nombre_del_modulo.nombre_del_modelo'
  _name = "proyectos.tarea"  
  _description = 'Modelo de Tarea'

  name = fields.Char(string= "Nombre")
  description = fields.Text(string = "Description")