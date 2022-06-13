*****
Usage
*****

This is a detailed chart of accounts, suitable for a medium to large company
(it should also work just fine for a small company too) fiduciarily required or
just desirous to report using `GAAP`_ standards commonly practiced in the
United States.

Currently, this module only supports corporate accounting. For partnership or
other types of business entity support, `email`_ or `file an issue`_ to
discuss.

Performance note
----------------

The nesting for some accounts currently goes 8 levels deep. This is not at all
performant on the Accounts or Account Templates `tree view`_ if you try to
expand all the accounts at once. `Just don't do it`_.

.. _GAAP: https://en.wikipedia.org/wiki/Generally_Accepted_Accounting_Principles_(United_States)
.. _file an issue: https://github.com/pentandra/account_us/issues
.. _email: https://pentandra.com/company/#contact
.. _tree view: https://docs.tryton.org/projects/server/en/latest/topics/views/index.html#tree
.. _Just don't do it: https://discuss.tryton.org/t/tree-view-performance-with-deeply-nested-chart-of-accounts/5353/2
