# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.modules.account.tests import create_chart
from trytond.modules.company.tests import create_company, set_company
from trytond.tests.test_tryton import ModuleTestCase, with_transaction


class AccountUSTestCase(ModuleTestCase):
    'Test Account US module'
    module = 'account_us'

    @with_transaction()
    def test_create_chart(self):
        company = create_company()
        with set_company(company):
            create_chart(company, chart=self.module + '.root')


del ModuleTestCase
