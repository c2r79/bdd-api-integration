from behave import *
import random


@given(u'a randomly generated number thats less than 5')
def step_impl(context):
    context.random_num = random.randint(0, 10)


@then(u'the test fails')
def step_impl(context):
    assert(context.random_num) > 5
