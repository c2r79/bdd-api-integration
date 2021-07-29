@3rd_parties @prod_health
Feature: Jobvite integration on careers page

    Testing basic integration points
    Scenario: Users can access open positions via careers page
        Given user is on the adMarketplace careers page
        When user clicks on either 'View all open roles' cta buttons
        Then a list of open positions is displayed
        And 'Director of Quality Engineering (QA / SDET)' is still available