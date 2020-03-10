## Jupyter Notebook 파일(.ipynb)을 markdown(.md) 파일로 변환하기
  - `nbconvert` 라이브러리를 이용하면 쉽게 변환 가능
  - `pip install nbconvert`
  - 아래의 파이썬 코드는 .ipynb로 작성된 파이썬 코드를 markdown으로 변환한 결과이다.

```python
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
```
    0.3
    1
    


