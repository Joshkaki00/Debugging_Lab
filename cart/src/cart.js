// Shopping cart helpers used by the checkout page.
// A cart is an array of line items: { id: 'sku-mug', qty: 2 }

function addToCart(cart, productId, qty) {
  const existing = cart.find(item => item.id === productId);
  if (existing) {
    existing.qty = qty;
  } else {
    cart.push({ id: productId, qty });
  }
  return cart;
}

function removeFromCart(cart, productId) {
  return cart.filter(item => item.id !== productId);
}

function itemCount(cart) {
  return cart.reduce((total, item) => total + item.qty, 0);
}

function cartTotal(cart, prices) {
  return cart.reduce((total, item) => total + prices[item.id] * item.qty, 0);
}

module.exports = { addToCart, removeFromCart, itemCount, cartTotal };
