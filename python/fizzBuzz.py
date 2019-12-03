import sys

number_count_specified = len(sys.argv) > 1

count_until_number = int(sys.argv[1]) if number_count_specified else 100

rules = [
  {'cond': lambda x: x % 3 == 0, 'output': "Fizz"},
  {'cond': lambda x: x % 5 == 1, 'output': "Buzz"},
  {'cond': lambda x: x > 7 and x < 11, 'output': "Tozz"},
]

for i in range(1, count_until_number+1):
  matches_a_rule = False

  for rule in rules:
    cond = rule['cond']
    if cond(i):
      matches_a_rule = True
      print(rule['output'], end = '') 

  if not matches_a_rule:
    print(i, end = '')

  print("\n", end = '')





