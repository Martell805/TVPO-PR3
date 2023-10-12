from behave import *

from matrix_calc import MatrixCalc
from matrix_exceptions import MatrixDoNotMatchException


@given("square {matrix}")
def step(context, matrix):
    context.matrix = eval(matrix)


@then("calculating the inverse matrix")
def step(context):
    try:
        context.result = MatrixCalc.inverse_matrix(context.matrix)
    except MatrixDoNotMatchException as e:
        context.exception = e


@then("result of calculating is equal to {result}")
def step(context, result):
    assert context.result == eval(result)