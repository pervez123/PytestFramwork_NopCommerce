class LoginTestData:

    login_credentials = [{'user_name': 'admin@yourstore.com', 'password': 'admin', "expected_result": "pass"},
                         {'user_name': 'admin@yourstore.com', 'password': 'invalid', "expected_result": "fail"},
                         {'user_name': 'invalid.com', 'password': 'admin', "expected_result": "fail"},
                         {'user_name': 'invalid.com', 'password': 'invalid', "expected_result": "fail"},
                         ]
