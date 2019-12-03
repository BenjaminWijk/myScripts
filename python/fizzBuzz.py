import sys

no_of_args = len(sys.argv)

if no_of_args > 1:
  count_until_number = int(sys.argv[1])
else:
  count_until_number = 100

rules = [
  {'expr': lambda x: x % 3 == 0, 'output': "Fizz"},
  {'expr': lambda x: x % 5 == 1, 'output': "Buzz"},
  {'expr': lambda x: x > 7 and x < 11, 'output': "Tozz"},
]

for i in range(1, count_until_number+1):
  matches_a_rule = False

  for rule in rules:
    expr = rule['expr']
    if expr(i):
      matches_a_rule = True
      print(rule['output'], end = '') 

  if not matches_a_rule:
    print(i, end = '')

  print("\n", end = '')





