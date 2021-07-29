Feature: Testing github action flow live

    Scenario: Pushing a new test to view workflow
        Given My final interview is today
        When I push this test
        Then it should work