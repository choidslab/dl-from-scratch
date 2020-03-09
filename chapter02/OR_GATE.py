import numpy as np


def or_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])  # AND gate와 차이는 weight, bias 값이 다르다.
    b = -0.2
    y = np.sum(w * x) + b
    print(y)
    if y <= 0:
        return 0
    else:
        return 1


if __name__ == "__main__":
    print(or_gate(0, 1))
