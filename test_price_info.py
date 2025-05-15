import price_info as PInfo

def test_cost_of_fruit():
    fruit_name = 'watermelon'
    fruit_quanity = 5
    expected_result = 32.50
    test_result = PInfo.cost_of_fruits(fruit_name,fruit_quanity)
    assert (test_result == expected_result)
    # assert(PInfo.cost_of_fruits('watermelon',5) == 32.50)

def test_total_cost():
    expected_result = 46.75
    test_result = PInfo.total_cost_shopping()
    assert (test_result == expected_result)