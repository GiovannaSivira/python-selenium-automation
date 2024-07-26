
Feature: Target terms and conditions test
  # Enter feature description here

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open target main page
    When Click sign in page
    When Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Target Terms and Conditions page is opened
    And User can close new window and switch back to original