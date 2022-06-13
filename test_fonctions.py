from main import count_char, check_if_maj, check_if_special, check_if_valid_password

def test_count_char():
    input = "Bonjour"
    expected = 7
    result = count_char(input)
    assert expected == result



def test_check_if_maj():
    input1 = "Bonjour"
    expected1 = True

    input2 = "Bonjourrrr"
    expected2 = True

    input3 = "bonjourrrr"
    expected3 = False

    assert expected1 == check_if_maj(input1)
    assert expected2 == check_if_maj(input2)
    assert expected3 == check_if_maj(input3)
    

def test_check_if_special():
    input1 = "Bonjour!!"
    expected1 = True

    input2 = "Bonjourrrr!"
    expected2 = True

    input3 = "bonjourrrr"
    expected3 = False

    assert expected1 == check_if_special(input1)
    assert expected2 == check_if_special(input2)
    assert expected3 == check_if_special(input3)

    

def test_check_if_valid_password():
    input1 = "BonjourToutLeMonde!!"
    expected1 = True

    input2 = "HelloWord"
    expected2 = False

    input3 = "bonjourrrr"
    expected3 = False

    assert expected1 == check_if_valid_password(input1)
    assert expected2 == check_if_valid_password(input2)
    assert expected3 == check_if_valid_password(input3)
