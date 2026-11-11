# cart bug log

found the bug around line 7 in cart.js.

i expected it to run correctly, not duplicating or not updating products/skus quantities.

line 7: `existing.qty = qty` — thought that caused a updating skus somehow.

after looking through: it overwrites the old quantity with the new one. no duplicate line, just wrong qty.

wrote a test that fails because of the bug instead of proceeding past it.

fix: `existing.qty += qty`

cart does correct now.
