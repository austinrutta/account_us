Account US Module
#################

The account_us module adds a chart of accounts that is based on a hybrid of
United States GAAP and IFRS financial accounting standards, so hopefully this
could be used as a starting point for accounting with either approach.

There are decisions to be made on when to model transactions with financial
accounts and analytic accounts. Here are some conclusions I have come to:

- Analytic accounts should be used for `segment reporting
  <https://asc.fasb.org/section&trid=2134533>`_. A lot of redundant financial
  accounts can be avoided this way.

- To satisfy income tax reporting needs, use a higher granularity of financial
  accounts than is required for financial accounting to differentiate types of
  expenditures.
