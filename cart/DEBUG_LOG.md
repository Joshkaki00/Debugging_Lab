# cart bug log

found the bug around line 7 in cart.js.

expected: run correctly, not duplicating products/skus.

line 7: `existing.qty = qty` — thought that caused a duplicate somehow.

after looking through: it overwrites the old quantity with the new one. no duplicate line, just wrong qty.

wrote a test that fails because of the bug instead of proceeding past it.

fix: `existing.qty += qty`

cart does correct now.
