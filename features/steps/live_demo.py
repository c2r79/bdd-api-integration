from behave import *


@given(u'My final interview is today')
def step_impl(context):
    print('Given My final interview is today')


@when(u'I push this test')
def step_impl(context):
    print('When I push this test')


@then(u'it should work')
def step_impl(context):
    print('Then it should work')
