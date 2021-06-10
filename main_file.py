
from compute_expression import infix_to_postfix, evaluate_postfix_expression


def main_function():
    user = {
        "age": 7,
        "gender": "male",
        "past_order_amount": 10,
        "salary": 10000,
        "height": 169,
        'city': 'Delhi'
    }
    # Assumption -> Conditional Expression is space seperated
    is_the_feature_allowed = is_allowed(
        'Same Day Delivery', '( age AllOf [24,7] && gender == male ) || ( past_order_amount == 10 )', user)
    print('Feature allowed?',is_the_feature_allowed)


def is_allowed(feature_name: str, conditional_expression: str, user_attributes):
    
    postfix_expression = infix_to_postfix(conditional_expression)
    result = evaluate_postfix_expression(postfix_expression, user_attributes)
    return result


main_function()
