class Test:
    def __init__(self, nPersons: int, preferences):
        self.nPersons = nPersons
        self.preferences = preferences

def print_tests(tests):
    for i, test in enumerate(tests):
        print(f"\n Test #{i + 1}:")
        print(f"  Número de personas: {test.nPersons}")
        print("  Preferencias:")
        for j, preference in enumerate(test.preferences):
            a, b, c = preference
            print(f"    Persona #{j + 1}: A={a}, B={b}, C={c}")

def get_inputs():
    #Variable declarations
    nTests = 0
    nPersons = 0
    A = 0
    B = 0
    C = 0
    tests = []

    #Get input
    nTests = int(input("Ingrese el número de pruebas:"))
    assert 1 <= nTests <= 2, "Número de pruebas fuera de rango (1 <= T <= 2)"

    for i in range (nTests):
        preferences = []

        nPersons = int(input("Ingrese el número de personas:"))
        assert 1 <= nPersons <= 5000, "Número de personas fuera de rango(1 <= N <= 5000)"
        
        for j in range (nPersons):
            A = int(input("Ingrese el porcentaje de preferencia de A:"))
            B = int(input("Ingrese el porcentaje de preferencia de B:"))
            C = int(input("Ingrese el porcentaje de preferencia de C:"))

            #Input validation
            assert 0 <= A <= 10000, "A fuera de rango"
            assert 0 <= B <= 10000, "B fuera de rango"
            assert 0 <= C <= 10000, "C fuera de rango"
            assert A + B + C <= 10000, "La suma de A, B y C sobrepasa 10000"

            
            preferences.append((A, B, C))

        tests.append(Test(nPersons, preferences))
    return tests


def get_max_satisfied(test):
    preferences = test.preferences[:]
    beverage = [0] * 3
    maxSatisfied = 0
    return get_max_helper(maxSatisfied, beverage, preferences)

#This functions uses backtracking and recursion to get the max number of people satisfied
def get_max_helper(maxSatisfied, beverage, remainingPreferences):
    #Base case
    if(len(remainingPreferences) == 0):
        return maxSatisfied
    
    #Auxiliar variable to get the new beverage
    auxBeverage = beverage[:]
    a, b, c = remainingPreferences[0]
    
    #Condition: fraction of beverage must be greater than
    #their A, B or C, else they wont like it.
    auxBeverage[0] = max(beverage[0], a)
    auxBeverage[1] = max(beverage[1], b)
    auxBeverage[2] = max(beverage[2], c)

    #Simple pruning based on the problem conditions
    if(auxBeverage[0] + auxBeverage[1] + auxBeverage[2] > 10000):
        return maxSatisfied
    
    del remainingPreferences[0]

    #Recursion with backtracking
    return max(get_max_helper(maxSatisfied + 1, auxBeverage, remainingPreferences[:]),
               get_max_helper(maxSatisfied, beverage, remainingPreferences[:]))

#Main function
def main():
    tests = get_inputs()
    print_tests(tests)
    for i, test in enumerate(tests):
        print("Caso #", i+1, ": ", get_max_satisfied(test))

main()