from behave import *

from matrix_calc import MatrixCalc
from matrix_exceptions import MatrixDoNotMatchException


@given('{matrix1} and {matrix2}')
def step(context, matrix1, matrix2):
    context.matrix1 = eval(matrix1)
    context.matrix2 = eval(matrix2)


@then("multiply them")
def step(context):
    try:
        context.result = MatrixCalc.multiply(context.matrix1, context.matrix2)
    except Exception as e:
        context.exception = e


@then("result matrix is equal to {result}")
def step(context, result):
    assert context.result == eval(result)


@then("exception {exception} is thrown")
def step(context, exception):
    assert isinstance(context.exception, eval(exception))
