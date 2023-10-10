from behave import *

from matrix_calc import MatrixCalc


@given('{matrix} and {number}')
def step(context, matrix, number):
    context.matrix = eval(matrix)
    context.number = eval(number)


@then("multiply them")
def step(context):
    try:
        context.result = MatrixCalc.number_multiplication(context.matrix, context.number)
    except Exception as e:
        context.exception = e


@then("result matrix is equal to {result}")
def step(context, result):
    assert context.result == eval(result)


@then("exception {exception} is thrown")
def step(context, exception):
    assert isinstance(context.exception, eval(exception))
