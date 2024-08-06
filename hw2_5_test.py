import hw2_5

def test_km_to_miles():
    assert abs(hw2_5.km_to_miles(1) - 0.621371) < 0.0001, 'Failed on 1'
    assert abs(hw2_5.km_to_miles(2) - 1.24274) < 0.0001, 'Failed on 2'
    assert abs(hw2_5.km_to_miles(10) - 6.21371) < 0.0001, 'Failed on 10'
    print('All tests passed!')

if __name__ == "__main__":
    test_km_to_miles()