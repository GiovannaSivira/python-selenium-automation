Feature: Target main page search tests

  Scenario: User can search for a product on target
  Scenario: User can search for a purse
    Given Open target main page
    When Search for product
    Then Verify search worked
    When Search for purse
    Then Verify search results shown for purse
    Then Verify correct search results URL opens for purse


  Scenario: User can search for sunglasses
    Given Open target main page
    When Search for sunglasses
    Then Verify search results shown for sunglasses
    Then Verify correct search results URL opens for sunglasses

  Scenario: User can search for a lipstick
    Given Open target main page
    When Search for lipstick
    Then Verify search results shown for lipstick
    And Verify correct search results URL opens for lipstick

#  Scenario Outline: User can search for a product
#    Given Open target main page
#    When Search for <product>
#    Then Verify search results shown for <expected_result>
#    And Verify correct search results URL opens for <expected_result>
#    Examples:
#    |product  |expected_result    |
#    |coffee   |coffee             |
#    |tea      |tea                |
#    |iphone   |iphone             |