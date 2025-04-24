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

 
