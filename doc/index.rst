Account US Module
#################

The account_us module adds a chart of accounts that is based on a hybrid of
United States GAAP and IFRS financial accounting standards, so hopefully this
could be used as a starting point for accounting with either approach.

There are decisions to be made on when to model transactions with financial
accounts and analytic accounts. Here are some conclusions I have come to:

- Analytic accounts should be used for `segment reporting
  <https://asc.fasb.org/section&trid=2134533>`_ and `cost centers
  <https://en.wikipedia.org/wiki/Cost_centre_(business)>`_. A lot of redundant
  financial accounts can be avoided this way.

- To satisfy income tax reporting needs, use a higher granularity of financial
  accounts than is required for financial accounting to differentiate types of
  expenditures.

- Taxes are separated into separate submodules according to legal jurisdiction.
  For example, in the US the laws governing sales and use tax are handled at
  the state (subdivision) level, so each state has its own file of taxes and
  tax codes. This is a more iterative and flexible approach for small and
  medium business to take and doesn't necessitate integration with a 3rd-party
  like TaxJar or AvaTax. Currently existing modules include:

  -  `account_us_ut <https://github.com/pentandra/account_us_ut>`_

--------

This is a work in progress, so use at your own risk.

Sources consulted:

* http://www.dwmbeancounter.com/BCTutorSite/Courses/ChartAccounts/lesson02-6.html
* http://www.ifrs-gaap.com/en/chart-of-accounts-us-gaap/
* http://www.ifrs-gaap.com/en/basic-IFRS-chart-of-accounts/
* http://www.eprentise.com/blog/designing-a-chart-of-accounts/designing-a-global-chart-of-accounts-and-taking-advantage-of-oracle-e-business-suite-release-12/
* http://nccs.urban.org/projects/ucoa.cfm
* https://www.sba.gov/sites/default/files/files/inv_charts_of_accounts.pdf
* https://www.sba.gov/sites/default/files/files/inv_standards.pdf
* https://asc.fasb.org/
* https://www.irs.gov/publications/p15
* https://www.irs.gov/publications/p15b
* https://www.irs.gov/publications/p463
* https://www.irs.gov/publications/p535
* https://www.irs.gov/publications/p542
* https://www.law.cornell.edu/uscode/text/26/274

Sources that would be good to consider more:

* https://www.accountingtools.com/articles/2017/5/14/reduce-the-chart-of-accounts
* https://bugs.tryton.org/issue9642 (Aligning with existing IFRS efforts for Tryton)
* https://discuss.tryton.org/t/how-to-create-your-country-localization-module-for-accounts/2758
* https://danielpocock.com/adapting-localizing-tryton-for-your-country-free-open-source-accounting-software/
* https://www.fmtconsultants.com/design-scalable-chart-accounts/
