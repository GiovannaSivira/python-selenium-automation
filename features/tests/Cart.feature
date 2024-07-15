Feature: Test for Cart functionality


  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open Target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown



   Scenario: Add a product into the shopping cart
     Given Open target main page
     When Search for make up
     When Click 'add to cart' when you found the product you like
     When Click 'add to cart' under choose options
     Then Verify product has been added to cart