from behave import *

use_step_matcher("re")


@given("we have behave 2")
def step_impl(context):
    print('test01')


@when("we implement a test 2")
def step_impl(context):
    print('test02')


@then("behave 2 will test it for us!123")
def step_impl(context):
    print('test03')