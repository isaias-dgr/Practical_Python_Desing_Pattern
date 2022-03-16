Feature: Compute factorial
    In order to play with aloe
    As beginnners
    We'll implement factorial

    Scenario: Facturoal of 0
        Given I have the number 0
        When I compute its factorial
        Then I see the number 1