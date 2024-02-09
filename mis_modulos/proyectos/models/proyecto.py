# -*- coding:utf-8 -*-

from odoo import fields, models

class Proyecto(models.Model):
  # El nombre técnico del modelo, usualmente en formato 'nombre_del_modulo.nombre_del_modelo'
  _name = "proyectos.proyecto"  
  _description = 'Modelo de Proyecto'

  name = fields.Char(string = 'Nombre')
  description = fields.Text(string="Descripcion")
  start_date = fields.Date(string= 'Fecha Inicio')
  end_date = fiels.Date(string = 'Fecha Fin')
  manager_id = fields.Many2one('res.users', string= 'Responsable')
  state = fields.Selection([('nuevo', 'Nuevo'), ('en_progreso', 'En progreso'), ('completado', 'Completado')], string= 'Estado del proyecto')
  users_ids = fields.Many2many('res.users', string='Usuarios asignados')
  task_ids = fields.One2many('proyectos.tarea', string = 'Tareas')
  budget = fields.Float(string= 'Presupuesto')
  priority = fields.Selection([('baja', 'Baja'), ('media', 'Media'), ('alta', 'Alta')] ,string = 'Prioridad')
  