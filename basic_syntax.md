# Basic Syntax

## Data type

원시 자료형 : 스택 메모리에 변수 값이 직접 저장되는 자료형 -> 불변 & 값이 복사 (Number, String, Boolean, null, undefined)

1. Number : 정수 또는 실수형 숫자를 표현하는 자료형

2. String : 텍스트 데이터를 표현하는 자료형 

- + 를 사용해 문자열끼리 결합, 나머지 연산은 불가능 

- Template literals : Backtick(``)을 사용해 내장된 표현식을 허용하는 문자열 작성 방식 (여러 줄에 걸쳐 문자열 정의 및 f-string 기능 구현)

3. null : 프로그래머가 **의도적**으로 '값이 없음'을 나타낼 때 사용 

4. undefined : 시스템이나 JavaScript 엔진이 '값이 할당되지 않음'을 나타낼 때 사용 

5. Boolean : true / false 

참조 자료형 : 객체의 주소가 저장되는 자료형 -> 가변, 주소가 복사 (Object, Array, Function) 


## Operator 

1. 할당 연산자 : =, +=, -= ..

2. 증가 & 감소 연산자 : ++, -- 

3. 비교 연산자 : < , >

4. 비교 연산자 : 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값 반환 (==) -> '1' == 1 을 true로 반환

5. 일치 연산자 : 두 피연산자의 값과 타입이 모두 같은 경우 true 반환 (===) -> 0 === false 를 false로 반환 

6. 논리 연산자 : and (&&) / or (||) / not (!) 


## Conditional Statement

1. if / else if / else : if ( condition ) { expression }

2. 삼항 연산자 : condition ? expression1 : expression2 


## Loop Statement 

1. while (condition) { statement }

2. for ([초기문]; [조건문]; [증감문];) { statement }

3. for...in : 객체의 열거 가능한 속성(property)에 대해 반복 

    for (variable in object) { statement }

4. for...of : 반복 가능한 객체(배열, 문자열 등)에 대해 반복 

    for (variable in iterable) { statement }


## Function

: 참조 자료형에 속하며, 모든 함수는 Function object 

1. 선언식 (function declaration) : 익숙한 방법 

    function name (param, param, ...param){
        statements
        return value
    }

2. 표현식 (function expression) : 람다 함수와 비슷 

    const funcName = function( name = variable ) {
        statement
        return value 
    }

3. 화살표 함수 표현식 : 간결한 표현법 

    const funcName = (variable) => { return 'hello, ${variable}'}

- 함수의 매개변수가 하나 뿐이라면 () 생략 가능 

- 함수 본문의 표현식이 한 줄이라면 {} 와 return 제거 가능 