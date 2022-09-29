# Created by Kevin at 9/26/22
Feature: Amazon test cases

  Scenario: User can see 'Sign in' page
    Given Open Amazon page
    When Clicks on returns & orders link
    Then Sign in page appears

  Scenario: User can see their cart is empty
    Given Open Amazon page
    When Click on empty cart
    Then Your Amazon Cart is empty

  Scenario: User can add a product into cart, and see it in cart
    Given Open Amazon page
    When Search for apple pencil
    When Click on first result
    When Add to Cart
    Then Verify item(s) line is shown