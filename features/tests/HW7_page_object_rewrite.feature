# Created by Kevin at 10/26/22
Feature: #Rewrite these scenarios with Page Object pattern:

#1
  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opened


  Scenario: 'Your Shopping Cart is empty' shown if no product added
     Given Open Amazon page
     When Click on cart icon
     Then Verify Your Shopping Cart is empty - text present

#2
  Scenario: Add a product to cart
    Given Open Amazon page
    When Search for toy
    When Click on first result
    When Add to Cart

