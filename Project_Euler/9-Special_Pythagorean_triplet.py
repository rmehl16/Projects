import math

def getPythTriplet(component_sum):
    for a in range(1, component_sum):
        for b in range(a, component_sum):
            for c in range(b, component_sum):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    print("Element 1: {}\nElement 2: {}\nElement 3: {}\nProduct: {}".format(a, b, c, a*b*c))
                    return a*b*c


if __name__ == '__main__':
    component_sum = 1000
    res = getPythTriplet(component_sum)
    print(res)