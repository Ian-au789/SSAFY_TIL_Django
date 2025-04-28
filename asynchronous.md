# Asynchronous JS

### 비동기

1. 동기(Synchronous) : 프로그램의 실행 흐름이 순차적으로 진행 (하나의 작업이 완료된 후 다음 작업 실행)

2. 비동기(Asynchronous) : 특정 작업의 종료를 기다리지 않고 다음 작업을 실행 (백드라운드에서 여러 작업 동시에 진행) 

### JavaScript 비동기 

- Thread : 작업을 처리할 때 실제로 작업을 수행하는 주체 

- Single Thread : Thread가 하나 뿐인 케이스 (JavaScript는 Single Thread 언어)

- Runtime : 브라우저 또는 Node.js 등 비동기 처리를 할 수 있도록 도와주는 환경 

1. JavaScript Engine의 Call Stack: 요청이 들어올 때 마다 모든 작업 순차적 처리 

2. Web API : 브라우저에서 제공하는 runtime 완경, 오래 걸리는 작업들을 call stack에서 받아서 별도로 처리

3. Task Queue : Web API에서 처리가 끝난 작업들 저장, Call Stack이 빈다면 전송 (FIFO)

4. Event Loop : 태스크가 들어오면 처리, 태스크가 없으면 슬립 


