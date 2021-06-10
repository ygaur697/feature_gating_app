
  

1. Run following commands to get the result using the default user ( refer the default structure at the last of this doc) in main_file and to run tests (test_feature_gating_module)

```

python3 main_file.py

python3 -m unittest test_feature_gating_module.py

```
2. Assumptions Taken
	* Every expression is to be separated by space.
	* AllOf and NoneOf operators currently support only numerics ( This can be upgraded to string input by upgrading utils **convert_string_to_int** function)
	* For Simplicity currently logical operators(&&) are used instead of their equivalent symbols (AND or and), list of same is provided below in the documentation



3. List of Operators with example expression
	* AllOf

	* NoneOf

	* ( >=)

	* <=

	* ( >)

	* (<)

	* &&

	* ||

	* Between

	* ==  

4. Though Currently the user is passed as an object to the function **is_allowed**, its extensible to a class object (refer class User and enum_data.py) if need be.

  

5. This module can be upgraded to involve new operators and attributes in case the need arises.
	* Build model for the operator
	* Update **compute_expression** file ( OPERATORS and PRIORITY dict())

Default user attributes:

```

user = {

"age": 7,

"gender": "male",

"past_order_amount": 10,

"salary": 10000,

"height": 169,

'city': 'Delhi'

}

```