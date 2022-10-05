# Created by Kevin at 10/3/22
Feature: Testing features for customer services page
  # Amazon.com

  Scenario: User can see 'Welcome to Amazon Customer Service'
    Given Open Amazon page
    When Click on Customer Service
    Then Customer Service page shows

  Scenario: Verify there are 9 links in main service center
    Given Open Amazon page
    When Click on Customer Service
    Then Verify 9 Customer Service links

  Scenario: User can see 'Search our help library'
    Given Open Amazon page
    When Click on Customer Service
    Then Verify - Search our help library

  Scenario: Verify search bar functionality
    Given Open Amazon page
    When Click on Customer Service
    Then Verify - help search bar is present

  Scenario: User can see 'All help topics'
    Given Open Amazon page
    When Click on Customer Service
    Then Verify - All help topics

  Scenario: User can see 'Recommended Topics' section
    Given Open Amazon page
    When Click on Customer Service
    Then Verify - help topics section exists