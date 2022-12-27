class Calculator:
    @classmethod
    def calc_exam(cls, *score):
        return sum(score)


calculator1 = Calculator

score1 = calculator1.calc_exam(1,2,3,4,5)

calculator2 = Calculator
score2 = calculator2.calc_exam(1,2,3,4,5)


print(calculator1 is calculator2)
