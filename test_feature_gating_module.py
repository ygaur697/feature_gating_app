import unittest
from unittest import result
from main_file import is_allowed
from compute_expression import infix_to_postfix, evaluate_postfix_expression

user = {
    "age": 24,
    "gender": "male",
    "past_order_amount": 10,
    "salary": 10000,
    "height": 169,
    'city': 'Delhi'
}


class TestGatingFeature(unittest.TestCase):

    def test_positive_result(self):
        expressions = ['( age AllOf [24,40,50] && gender == male ) && ( past_order_amount AllOf [10,20] )',
                       '( salary >= 10000 && height == 169 )',
                       '( city == delhi ) && ( past_order_amount AllOf [10,20,40] ) && age <= 30',
                       '( age AllOf [24,7] && gender == male ) || ( past_order_amount == 10 )'
                       ]
        for exp in expressions:
            result = is_allowed('Any_feature', exp, user)
            self.assertEqual(result, True)

    def test_negative_results(self):
        expressions = ['( age AllOf [24] && gender == female ) || ( past_order_amount == 1000 )',
                       '( salary >= 10000 && height > 169 )',
                       '( city == mumbai ) && ( past_order_amount AllOf [10,20,40] ) && age <= 30',
                       ]

        for exp in expressions:
            result = is_allowed('Any_feature', exp, user)
            self.assertEqual(result, False)

    def test_infix_to_postfix(self):
        infix_expression = '( age AllOf [24,7] && gender == male ) || ( past_order_amount == 10 )'
        result = infix_to_postfix(infix_expression)
        expected_result = ['age', '[24,7]', 'AllOf', 'gender',
                           'male', '==', '&&', 'past_order_amount', '10', '==', '||']
        self.assertEqual(result, expected_result)

    def test_postfix_expression(self):
        postfix_expression = evaluate_postfix_expression(
            ['age', '[24,7]', 'AllOf', 'gender', 'male', '==', '&&', 'past_order_amount', '10', '==', '||'], user)
        self.assertEqual(postfix_expression, True)
