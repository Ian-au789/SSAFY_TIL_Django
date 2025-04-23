# Basic Syntax 2

### Object

: 키로 구분된 데이터 집합을 저장하는 자료형 

- 중괄호 {} 내부에 작성

- 중괄호 안에는 key : value 쌍으로 구성된 속성을 여러 개 작성 가능

- key는 문자형만, value는 모든 자료형 사용 가능

- . 또는 대괄호[] 로 객체 요소 접근
  
예시)

    const user = {
      name: 'Alice',
      'key with space': true,
      greeting: function () {
        return 'hello'
      }
    }

    // 조회
    console.log(user.name) // Alice
    console.log(user['key with space']) // true


### Method

: 객체 속성에 정의된 함수 (행동), object.method 방식으로 호출

- this : 함수나 메서드를 호출한 객체를 가리키는 키워드, 함수 내에서 객체의 속성 및 메서드에 접근 

- 단순 호출 : 전역 객체

- 메서드 호출 : 메서드를 호출한 객체 

- 화살표 함수는 자신만의 this를 가지지 않기 때문에 외부 함수에서의 this 값을 가져옴 


### 추가 객체 문법

1. 단축 속성 : 키 이름과 값으로 쓰이는 변수의 이름이 같다면 key:value가 아닌 value 만 저장 가능

2. 단축 메서드 : 메서드 선언 시 function 키워드 생략 가능

3. 계산된 속성 : 키가 대괄호[]로 둘러싸여 있는 속성 -> 고정된 값이 아닌 변수 값 사용 가능 

4. 구조 분해 할당 : 배열 또는 객체를 분해하여 객체 속성을 변수에 쉽게 할당 

5. 전개 구문 : 객체 내부에서 객체 전개 -> 얕은 복사 

6. Object.keys(object) / Object.values(object)

7. Optional chaining (?.) : 속성이 없는 중첩 객체를 에러 없이 접근 


## JSON

: Key-Value 형태로 이루어진 자료 표기법 (JavaScript Object Notation)

- 형식이 있는 **문자열**

- JavaScript에서 JSON을 사용하기 위해서 Object 자료형으로 변경 


## Array 

: 순서가 있는 데이터 집합을 저장하는 자료 구조

- push / pop : 배열 끝 요소를 추가 / 제거

- unshift / shift : 배열 앞 요소를 추가 / 제거 

### Array Helper Methods

: 배열 조작을 보다 쉽게 수행할 수 있는 특별한 메서드 모음 

- 배열의 각 요소를 순회하며 각 요소에 대해 콜백함수 호출 

- 메서드 호출 시 인자로 콜백함수를 받는 것이 특징 


### Callback function

: 다른 함수에 인자로 전달되는 함수, 외부 함수 내에서 호출되어 일종의 루틴이나 특정 작업을 진행

1. forEach : 배열 내 모든 요소 각각에 대해 콜백함수를 호출 (반환값 없음)

arr.forEach(callback(item[, index[, array]]))

2. map : 배열 내 모든 요소 각각에 대해 콜백함수 호출 결과를 모아 새로운 배열을 반환 

arr.map(callback(item[, index[, array]]))


