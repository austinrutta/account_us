Account US Module
#################

The account_us module adds a chart of accounts that is based on a hybrid of
United States GAAP and IFRS financial accounting standards, so hopefully this
could be used as a starting point for accounting with either approach.

- Expenses (5) are classified according to the type of expense not the
  structure of the organization (the `cost center
  <https://en.wikipedia.org/wiki/Cost_centre_(business)>`_). Until tryton
  supports cost centers, add the organizational structure through the account
  name, for example::
  
    telephone expense—sales
