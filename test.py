import factoriel

def test_factorial_of():
    assert factoriel.factorial_of(55,factoriel.Factorial_type.ITERATIVE) == 12696403353658275925965100847566516959580321051449436762275840000000000000
    assert factoriel.factorial_of(5 ,factoriel.Factorial_type.ITERATIVE) == 120
    assert factoriel.factorial_of(10,factoriel.Factorial_type.ITERATIVE) == 3628800
    return 0

def test_factorial_of_iterative():
    assert factoriel.factorial_of_iterative(55) == 12696403353658275925965100847566516959580321051449436762275840000000000000
    assert factoriel.factorial_of_iterative( 5) == 120
    assert factoriel.factorial_of_iterative(10) == 3628800
    return 0

def test_factorial_of_recursive():
    assert factoriel.factorial_of_recursive(55) == 12696403353658275925965100847566516959580321051449436762275840000000000000
    assert factoriel.factorial_of_recursive( 5) == 120
    assert factoriel.factorial_of_recursive(10) == 3628800
    return 0

def main():
    test_factorial_of_recursive()
    test_factorial_of_iterative()
    test_factorial_of()