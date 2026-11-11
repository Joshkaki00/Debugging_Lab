const { addToCart, removeFromCart, itemCount, cartTotal } = require('../src/cart');

describe('addToCart', () => {
  test('adds a new product to an empty cart', () => {
    const cart = addToCart([], 'sku-mug', 1);
    expect(cart).toEqual([{ id: 'sku-mug', qty: 1 }]);
  });

  test('adds different products as separate line items', () => {
    let cart = [];
    cart = addToCart(cart, 'sku-mug', 1);
    cart = addToCart(cart, 'sku-tshirt', 2);
    expect(cart).toEqual([
      { id: 'sku-mug', qty: 1 },
      { id: 'sku-tshirt', qty: 2 },
    ]);
  });
});

describe('removeFromCart', () => {
  test('removes the matching product', () => {
    const cart = [
      { id: 'sku-mug', qty: 1 },
      { id: 'sku-tshirt', qty: 2 },
    ];
    expect(removeFromCart(cart, 'sku-mug')).toEqual([{ id: 'sku-tshirt', qty: 2 }]);
  });
});

describe('itemCount', () => {
  test('adds up quantities across line items', () => {
    const cart = [
      { id: 'sku-mug', qty: 1 },
      { id: 'sku-tshirt', qty: 2 },
    ];
    expect(itemCount(cart)).toBe(3);
  });
});

describe('cartTotal', () => {
  test('multiplies price by quantity for each line item', () => {
    const cart = [
      { id: 'sku-mug', qty: 2 },
      { id: 'sku-sticker', qty: 1 },
    ];
    const prices = { 'sku-mug': 12, 'sku-sticker': 3.5 };
    expect(cartTotal(cart, prices)).toBe(27.5);
  });
});
