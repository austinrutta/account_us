******
Design
******

The account_us module adds a chart of accounts that is based on a hybrid of
United States GAAP_ and IFRS_ financial accounting standards, so hopefully this
could be used as a starting point for accounting with either approach.

Influential, but possibly temporary, conclusions
------------------------------------------------

There are decisions to be made on when to model transactions with financial
accounts and analytic accounts. Here are some conclusions I have come to:

- Analytic accounts should be used for `segment reporting`_ and `cost
  centers`_. A lot of redundant financial accounts can be avoided this way.

  This may change with current discussion about `company subdivisions`_.

- To satisfy income tax reporting needs, use a higher granularity of financial
  accounts than is required for financial accounting to differentiate types of
  expenditures (i.e. more detailed sub-accounts).

Chart structure
---------------

Unlike countries such as France, Spain, and Sweden, the United States does not
have a national chart of accounts, nor does any of its states (to my knowledge)
have an official state chart of accounts. Because of this, the structure of of
this chart has materialized over time from various publicly available,
informational sources.  Some parts are more fleshed out than others. Note the
`license`_. But there is an expectation that financial reporting from public
companies (at least) will follow the Accounting Standards Codifications
(`ASC`_) published by the US-based Financial Accounting Standards Board
(`FASB`_).

Sources consulted
.................

* https://asc.fasb.org/
* https://github.com/tryton/account_fr and https://github.com/tryton/account_be (for help with Tryton account types and general inspiration)
* https://en.wikipedia.org/wiki/Chart_of_accounts
* https://web.archive.org/web/20160825052543/https://nccs.urban.org/projects/ucoa.cfm
  * and derivative Tryton module (archived): https://code.google.com/archive/p/tryton-ucoa/
* http://www.ifrs-gaap.com/en/chart-of-accounts-us-gaap/
* http://www.ifrs-gaap.com/en/basic-IFRS-chart-of-accounts/
* https://www.gaap.cz/sites/default/files/upload/pdf/1-GAAP-IFRS.pdf
* http://www.eprentise.com/blog/designing-a-chart-of-accounts/designing-a-global-chart-of-accounts-and-taking-advantage-of-oracle-e-business-suite-release-12/
* http://www.dwmbeancounter.com/BCTutorSite/Courses/ChartAccounts/lesson02-6.html
* https://www.sba.gov/sites/default/files/files/inv_charts_of_accounts.pdf
* https://www.sba.gov/sites/default/files/files/inv_standards.pdf
* https://www.irs.gov/publications/p15
* https://www.irs.gov/publications/p15b
* https://www.irs.gov/publications/p463
* https://www.irs.gov/publications/p535
* https://www.irs.gov/publications/p542
* https://www.law.cornell.edu/uscode/text/26/274

Sources that would be good to consider more
...........................................

* https://www.accountingtools.com/articles/2017/5/14/reduce-the-chart-of-accounts
* https://bugs.tryton.org/issue9642 (Aligning with existing IFRS efforts for Tryton)
* https://discuss.tryton.org/t/how-to-create-your-country-localization-module-for-accounts/2758
* https://danielpocock.com/adapting-localizing-tryton-for-your-country-free-open-source-accounting-software/
* https://www.fmtconsultants.com/design-scalable-chart-accounts/

Tax chart structure
-------------------

On the other hand, sales and use taxes in the US are handled at the state
(subdivision) level. Each state has prescribed its own chart of of taxes and
tax codes.  Due to the immense task of compiling tax information for all 50
states, I have taken the path of grouping state taxes into separate submodules
according to legal jurisdiction. This is a more iterative and flexible approach
for small and medium business to take and doesn't necessitate integration with
a 3rd-party like TaxJar or AvaTax. Contributions are welcome.

Currently existing tax modules (in some level of completeness) include:

-  `account_us_ut <https://github.com/pentandra/account_us_ut>`_ (Utah)

.. _GAAP: https://en.wikipedia.org/wiki/Generally_Accepted_Accounting_Principles_(United_States)
.. _IFRS: https://en.wikipedia.org/wiki/International_Financial_Reporting_Standards
.. _segment reporting: https://asc.fasb.org/section&trid=2134533
.. _cost centers: https://en.wikipedia.org/wiki/Cost_centre_(business)
.. _company subdivisions: https://discuss.tryton.org/t/brands-or-subdivisions/3537/4
.. _ASC: https://asc.fasb.org/
.. _FASB: https://fasb.org/
.. _license: ../LICENSE
