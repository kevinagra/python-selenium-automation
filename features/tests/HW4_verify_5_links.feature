# Created by Kevin at 10/3/22

Feature: Practice with hamburger menu, verify count of column links


  Scenario: Hamburger menu is present
    Given Open Amazon page
    Then Verify hamburger menu is present


  Scenario: Verify correct amount of links in BestSellers page
    Given Open Amazon page
    When Click on Best Sellers
    Then Verify Best Sellers column has 5 links

