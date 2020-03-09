import numpy as np


def nand_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # AND gate weight, bias에 부호만 반대로
    b = 0.7
    y = np.sum(w * x) + b
    print(y)
    if y <= 0:
        return 0
    else:
        return 1


if __name__ == "__main__":
    print(nand_gate(0, 1))
