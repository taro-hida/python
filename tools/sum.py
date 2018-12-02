import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', type=str)
args = parser.parse_args()

with open(args.filename) as f:
  nums = f.read().splitlines()


print(nums)
num = 0
for i in nums:
  num += int(i)

print(num)
