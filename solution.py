import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--barbie', type=int, default=50)
parser.add_argument('--cars', type=int, default=50)
parser.add_argument('--movie', type=str, default='other')

args = parser.parse_args()
d = {'melodrama': 0,
     'football': 100,
     'other': 50}
if not (0 <= args.cars <= 100):
    args.cars = 50
if not (0 <= args.barbie <= 100):
    args.barbie = 50
print(f'boy: {(100 - args.barbie + args.cars + d[args.movie]) // 3}')
print(f'girl: {100 - (100 - args.barbie + args.cars + d[args.movie]) // 3}')
