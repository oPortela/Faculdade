from random import randint, choice, shuffle

def first_missing(arr: list, **args) -> int:
    a1 = args.get('a1', min(arr))
    an = args.get('an', max(arr))
    n  = args.get('n', len(arr))
    sn = (a1 + an)* n/2
    return sn - sum(arr)

def get_arr() -> dict: #   ---Dados para teste---
    a1 = randint(-100, 100)
    n = randint(50, 200)
    incr = choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    an = a1 + n*incr
    arr = [i for i in range(a1, an, incr)]
    shuffle(arr)
    selected = choice(arr)
    arr.remove(selected)
    return locals()

if __name__ == '__main__':
    params = get_arr()
    print('-'*50)
    print(params)
    selected = params.pop('selected')
    assert selected == first_missing(**params)
    print('Success!'.center(50, '='))