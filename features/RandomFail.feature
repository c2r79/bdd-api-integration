@prod_health @wednesday
Feature: Making test randomly fail

    Scenario: Number is less than 5
        Given a randomly generated number thats less than 5
        Then the test fails