# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.model import fields
from trytond.pool import Pool, PoolMeta

class CreateChart(metaclass=PoolMeta):
    __name__ = 'account.create_chart'

    def default_properties(self, fields):
        pool = Pool()
        ModelData = pool.get('ir.model.data')
        defaults = super().default_properties(fields)
        template_id = ModelData.get_id('account_us.root')
        if self.account.account_template.id == template_id:
            defaults['account_receivable'] = self.get_account(
                    'account_us.1200')
            defaults['account_payable'] = self.get_account(
                    'account_us.2100')
            return defaults
