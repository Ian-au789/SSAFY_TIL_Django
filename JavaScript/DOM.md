# Introduction

JavaScript : Web Page의 동적 기능을 구현하기 위한 프로그래밍 언어 

Node : DOM의 기본 구성 단위, DOM 트리의 각 부분

NodeList : DOM 메서드를 사용해 선택한 Node의 목록, 배열과 유사한 구조 

## Variable

1. 반드시 문자, $, 또는 _ 로 시작

2. 대소문자를 구분

3. 예약어 (for, if, function) 사용 불가 

### 식별자(변수명) Naming case

- camelCase : 변수, 객체, 함수에 사용

- PascalCase : 클래스, 생성자에 사용

- SNAKE_CASE : 상수에 사용 


### 변수 선언 키워드

1. let : 블록 스코프를 갖는 지역 변수를 선언 (재할당 가능 / 재선언 불가능 / ES6에서 추가)

2. const : 블록 스코프를 갖는 지역 변수를 선언 (재할당 불가능 / 재선언 불가능 / ES6에서 추가)

- 블록 스코프(block scope) : if, for, 함수 등의 중괄호 {} 내부 

- const를 기본으로 사용, 필요한 경우에만 let 전환 -> 코드의 의도 명확화 & 버그 예방 


## DOM 

: a문서의 요소들을 객체로 제공하여 다른 프로그래밍 언어에서 접근하고 조작할 수 있는 API 

1. 조작 하고자 하는 요소를 탐색 및 선택

2. 선택된 요소의 콘텐츠 또는 속성을 조작 

### 선택 메서드

- document.querySelector(selector) : 요소 1개 선택

- document.querySelecorall(selector) : 요소 여러 개 선택 
 

 ### 조작 메서드 

<클래스 속성> 

- element.clasList.add() : 클래스 값 추가

- element.classList.remove() : 클래스 값 제거

- element.classList.toggle() : 클래스가 존재하면 제거하고 False, 존재하지 않으면 클래스 추가하고 True 반환 

<일반 속성>

- Element.getAttribute() : 해당 요소에 지정된 값을 반환

- Element.setAttribute(name, value) : 지정된 요소의 속성 값 설정, 이미 있다면 기존값 갱신 

- ELement.removeAttribute() : 요소에서 지정된 이름을 가진 속성 제거 

<HTML 콘텐츠>

: variable.textContent = value

<DOM 요소 조작 메서드>

- document.createElement(tagName) : 작성한 tagName의 HTML 요소를 생성하여 반환

- Node.appendChild() : 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입 및 반환 

- Node.removeChild() : DOM에서 자식 Node를 제거 및 반환 

