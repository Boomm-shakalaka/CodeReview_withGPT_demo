@Test
public void testIncreaseQuantity() {
    cart.addProduct("Be A Good Person");

    String product = "Air Fryer Squad";
    cart.addProduct(product);
    cart.increaseQuantity(product, 1);
    cart.clickUpdate();
    assertEquals(cart.getQuantity(product), 2);
}