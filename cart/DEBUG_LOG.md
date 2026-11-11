# DB-2: The disappearing cart items

## Bug report
Customer added mug, t-shirt, stickers, then another mug. Cart only showed one mug.

## Expected
Same SKU added twice should keep one line item and sum quantities (mug qty 2).

## Actual
Second add left mug at qty 1.

## Finding
Around `cart/src/cart.js` line 7:

```js
existing.qty = qty; // overwrites old qty with the new click amount
```

That assignment replaces the existing quantity instead of adding to it. No duplicate SKU lines — the line stayed, but the qty was wrong.

## Why tests missed it
Existing tests only covered new products and different SKUs. Nothing added the same product twice.

## Fix
```js
existing.qty += qty;
```

Added test: `increments qty when the same product is added again`.

## Root cause
`addToCart` set quantity to the latest add amount instead of accumulating, so repeat adds for the same SKU silently dropped prior qty.
