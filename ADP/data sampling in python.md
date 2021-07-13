# 데이터샘플링 in python



## train_test_split 함수 이용



#### ● 모듈 불러오기

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
```



---



#### ● 데이터 불러오기

```pyhton
iris = datasets.load_iris()
iris.data
```

![image](https://user-images.githubusercontent.com/80219821/125239514-b978e300-e323-11eb-8011-5b5d08a70c57.png)

```python
# 데이터 (행,열) 확인

iris.data.shape
## (150,4)
```



---



#### ● 순차적 분할

: 순차적으로 train,test 데이터 분할 (7:3)

```python
X_train1, X_test1, y_train1, y_test1 = train_test_split(iris.data,iris.target,test_size=0.3,shuffle=False)
```

-> shuffle = False로 무작위로 섞는 것 없이 순차적 분할을 명시하였다.

-> 시계열 데이터는 순서를 유지해서 샘플랭 하는 것이 필요함으로 시계열데이터 분할 시 자주 사용됨



\- 항상 확인하는 습관을 가지자

```python
X_train1.shape, y_train1.shape,X_test1.shape, y_test1.shape

## ((105,4), (105,), (45, 4),(45,))
```



---



#### ● 랜덤 분할

: 랜덤으로 train,test 데이터 분할 (7:3)

```python
X_train2, X_test2, y_train2, y_test2 = train_test_split(iris.data,iris.target,test_size=0.3)
```

-> shuffle = False가 defalt 값으로, 따로 써넣을 필요 없다.



---



#### ● 층화추출법 분할

```python
X_train3, X_test3, y_train3, y_test3 = train_test_split(iris.data,iris.target,test_size=0.3,stratify=iris.target)
```

-> 층 = target변수의 종류(3종류) 로 층화추출법을 해주었다.





