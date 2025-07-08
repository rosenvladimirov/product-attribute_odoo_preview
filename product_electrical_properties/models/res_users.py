# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, SUPERUSER_ID, _, Command


class Users(models.Model):
    _name = "res.users"
    _inherit = ['res.users', 'nexar.client.mixin']
