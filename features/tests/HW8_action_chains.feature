# Created by Kevin at 11/9/22
Feature: To practice action chains
"""
1. Make another test scenario using a dropdown and search for an item in a different Amazon department.
2. Opens https://www.amazon.com/gp/product/B074TBCSC8 (or any other product from the closing category),
hovers over New Arrivals, then verifies that the user sees the deals.
"""


  Scenario: Use dropdown, and search for item in different dept (1)
    Given Open Amazon page
    When Select Movies & TV department
    And Search for sinatra
    Then Verify Movies & TV department is selected


#  Scenario: Use dropdown, and search for item in different dept (2)
#    Given Open Amazon page
#    When Select department by value movies-tv
#    And Search for sinatra
#    Then Verify Movies & TV department is selected


  Scenario: Hover over New Arrivals, and then verify deals are there
    Given Open Kitty Cat Hoodie page
    When Hover over New Arrivals
    Then Verify user can see deals

