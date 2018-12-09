from behave import *

use_step_matcher("re")


@given("we have behave 1")
def step_impl(context):
    print('test01')


@when("we implement a test 1")
def step_impl(context):
    print('test02')

@then("behave 1 will test it for us!")
def step_impl(context):
    print("test03")