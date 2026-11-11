// Replays the steps from the customer's bug report and prints the cart.
// Run with: npm start

const { addToCart, itemCount, cartTotal } = require('./cart');

const prices = {
  'sku-mug': 12.0,
  'sku-tshirt': 25.0,
  'sku-sticker': 3.5,
};

const steps = [
  ['sku-mug', 1],
  ['sku-tshirt', 2],
  ['sku-sticker', 3],
  ['sku-mug', 1],
];

let cart = [];
for (const [productId, qty] of steps) {
  console.log(`Customer clicks "Add to cart": ${qty} x ${productId}`);
  cart = addToCart(cart, productId, qty);
}

console.log('\nCart:');
console.table(cart);
console.log(`Items in cart: ${itemCount(cart)}`);
console.log(`Total: $${cartTotal(cart, prices).toFixed(2)}`);
