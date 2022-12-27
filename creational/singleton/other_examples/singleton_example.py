from pattern import Calculator


calculator1 = Calculator()
score1 = calculator1.calc_exam(1,2,3,4,5)
print(score1)


calculator2 = Calculator()
score2 = calculator2.calc_exam(1,2,3,4,5)
print(score2)


print(calculator1 is calculator2)


# 15
# 15
# True
