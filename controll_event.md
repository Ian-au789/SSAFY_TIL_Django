# Event 

: Web Page 상에서 무언가 일어났다는 신호 또는 사건 

Web에서의 모든 동작은 이벤트 발생과 함께 한다. 

### event object

: DOM에서 이벤트가 발생하면 브라우저는 해당 이벤트에 관한 정보를 담은 event object를 자동으로 생성 

- 이벤트 발생 순간의 상황과 관련된 상세 정보 저장 


### event handler

: 특정 이벤트가 발생했을 떄 실행되는 (콜백)함수 

- addEventListener를 통해 DOM요소에 등록 

- DOM요소에서 발생한 event를 처리함 

- addEventListner() : 이벤트 핸들러를 DOM요소에 연결하는 역할

    EventTarget(DOM 요소).addEventListner(type(수신할 이벤트), handler(핸들러))

    : EventTarget에 type(이벤트 유형)가 발생했을 때 등록된 handler(콜백 함수)를 실행한다.

 
### Bubbling

: 한 요소에 이벤트가 발생 시 이 요소 뿐 아니라 부모 요소의 핸들러까지 동작하는 현상 

- event.currentTarget : '현재' 요소, this 와 유사 

- event.target : 이벤트가 발생한 가장 안쪽의 요소(target)를 참조, 실제 이벤트가 시작된 요소 

- 공통 조상에 이벤트 핸들러 하나만 할당하는 식으로 여러 버튼 요소에서 발생하는 이벤트를 한꺼번에 다룰 수 있음 


### 이벤트 취소

: HTML의 각 요소가 기본적으로 가지고 있는 이벤트가 원하는 동작을 하는데 방해가 된다면 기본 동작을 취소

- .preventDefault() : 해당 이벤트에 대한 기본 동작을 실행하지 않도록 지정 