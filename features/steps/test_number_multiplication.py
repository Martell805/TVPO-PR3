from behave import *

from matrix_calc import MatrixCalc


@given('{matrix} with {number}')
def step(context, matrix, number):
    context.matrix = eval(matrix)
    context.number = eval(number)


@then("multiply matrix and number")
def step(context):
    try:
        context.result = MatrixCalc.number_multiplication(context.matrix, context.number)
    except Exception as e:
        context.exception = e

@then("result of multiplication is equal to {result}")
def step(context, result):
    assert context.result == eval(result)


@then("{exception} has been thrown")
def step(context, exception):
    assert isinstance(context.exception, eval(exception))
