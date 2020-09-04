# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#
#    Copyright (c) All rights reserved:
#        (c) 2015  TM_FULLNAME
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#
###############################################################################
{
    'name': 'HR Employee Excel export',
    'summary': 'HR Employee Excel export',
    'version': '1.0',
    'description': """HR Employee Excel export""",
    'author': 'CodersFort',
    'website': 'http://www.codersfort.com',
    'license': 'AGPL-3',
    'category': 'HR',
    'depends': [
        'base',
        'hr',
        'report_xlsx',
    ],
    'data': [
        'wizard/hr_employee_excel_report.xml',
    ],
    'installable': True
}
