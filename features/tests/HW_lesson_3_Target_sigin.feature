Feature: Target Sing In test
  # Enter feature description here

  Scenario: A logged out user can navigate to sing in
    Given Open target.com
    When Click Sign in from right side navigation menu
    Then Verify Sign In form opened
