from behave import *
import requests


@given(u'user is on the adMarketplace careers page')
def step_impl(context):
    assert(requests.get('https://www.admarketplace.com/careers').status_code) == 200


@when(u'user clicks on either \'View all open roles\' cta buttons')
def step_impl(context):
    context.job_list = requests.get(
        'http://jobs.jobvite.com/careers/admarketplace/')
    assert(context.job_list.status_code) == 200


@then(u'a list of open positions is displayed')
def step_impl(context):
    assert('Director of Quality Engineering (QA / SDET)' in context.job_list.text)


@then(u'\'Director of Quality Engineering (QA / SDET)\' is still available')
def step_impl(context):
    assert(requests.get(
        'http://jobs.jobvite.com/admarketplace/job/o67Xcfw6').status_code) == 200
