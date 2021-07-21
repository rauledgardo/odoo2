# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import fields, osv, models, api
from odoo.tools.translate import _
import logging
_logger = logging.getLogger(__name__)

import pdb

#from .warning import warning
import requests
from odoo.addons.meli_oerp.melisdk.meli import Meli
from odoo.addons.meli_oerp.models.versions import *

mapping_meli_sku_regex = {
    "alephcrm": [
        {
            "regex": r"([a-zA-Z0-9]+[\-]+)([A-Z0-9]+[^x])",
            "group": 1,
            "test": "A12-848ERZEREx10"
        },
        {
            "regex": r"([A-Z0-9]+[^-x]$)",
            "group": 0,
            "test": "DF848ERZERE"
        }
    ]
}

# Mapping table
# "Cód SKU Propio Mercado Libre": "SKU ODOO"
mapping_meli_sku_defaut_code = {
    "904254AX50": "Y051",
    "904254AX100": "Y068",
    "904254AX200": "Y050",
    "904254AX500": "Y069",
    "901799X10": "Y015",
    "901793+902862": "Y081",
    "902852+902862": "Y082",
    "901793+902076": "Y083",
    "902852+902076": "Y084",
    "902386 + 902414": "Y086",
    "902387 + 902414": "Y087",
    "902388 + 902414": "Y088",
    "902389 + 902414": "Y089",
    "902390 + 902414": "Y090",
    "902391 + 902414": "Y091",
    "902395 + 902414": "Y092",
    "902386 + 902415": "Y093",
    "902387 + 902415": "Y094",
    "902388 + 902415": "Y095",
    "902389 + 902415": "Y096",
    "902390 + 902415": "Y097",
    "902391 + 902415": "Y098",
    "902395 + 902415": "Y099",
    "901543 + 901383": "Y045",
    "901386 + 901383": "Y009",
    "902801 + 901383": "Y071",
    "903113 + 901383": "Y072",
    "903649 + 901383": "Y073",
    "903650 + 901383": "Y074",
    "901543 + 902438": "Y000",
    "901386 + 902438": "Y075",
    "903113 + 902438": "Y076",
    "903649 + 902438": "Y077",
    "903377+901697": "Y067",
    "902770+901697": "Y066",
    "904371x10": "Y053",
    "904371X50": "Y060",
    "901386+901383": "Y009",
    "904371x10vc": "Y053",
    "904371x50vc": "Y060",
    "904371x100vc": "Y061",
    "900618x500": "Y070",
    "904432x10": "Y078",
    "904432x50": "Y079",
    "904432x100": "Y080",
    "904254x2000": "Y064",
    "Y100": "Y100",
    "Y101": "Y101",
    "Y104": "Y104",
    "Y102": "Y102",
    "Y103": "Y103",
    "900473x10": "Y030",
    "901609x10": "Y029",
    "903684x10": "Y031",
    "903683x10": "Y033",
    "903509": "Y105",
    "903682": "Y032"
}

class meli_oerp_sku_rule(models.Model):

    _name = "meli_oerp.sku.rule"
    _description = "Meli Sku Rule"

    name = fields.Char(string="Name",help="Sku Name received",required=True,index=True)
    type = fields.Selection([('map','Map'),('regex','Formula')],string="Rule type", index=True, default='map')

    sku = fields.Char(string="Sku",help="Sku Map in Odoo",required=False,index=True)
    barcode = fields.Char(string="Barcode",help="Barcode Map in Odoo",required=False,index=True)

    formula = fields.Char(string="Formula",help="Sku Regex Formula",required=False,index=True)
    group = fields.Char(string="Group",help="Sku Regex Group",required=False)
    test = fields.Char(string="Test",help="Sku Regex Test",required=False)

    security_virtual_stock_to_pause = fields.Float(string="Virtual Stock", default=False )
    security_quantity_stock_to_pause = fields.Float(string="Quantity Stock", default=False )

    _sql_constraints = [
        ('unique_meli_oerp_sku_rule', 'unique(name)', 'Rule name already exists!')
    ]

    def map_to_sku(self, name ):

        sku = None
        maps = self.search([('name','=',str(name)),('type','=','map')])

        if len(maps)==1:
            sku = maps[0].sku
        #else:
        #    _logger.error("Sku Map duplicates:"+str(name))

        return sku

    def resolve_to_sku(self, name ):
        sku = None
        return sku
