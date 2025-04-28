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


## Ajax

: Asynchronous JavaScript and XML 

- 하나의 특정한 기술을 의미하는 것이 아닌, 비동기적인 웹 개발에 사용하는 기술들의 집합 

- XMLHttpRequest 기술을 사용해 복잡하고 동적인 웹 페이지를 구성하는 프로그래밍 방식

- 브라우저와 서버 간의 데이터를 비동기적으로 교환하는 기술

- 새로고침을 하지 않고도 동적으로 데이터를 불러와 화면 일부만 갱신 가능

- XML은 데이터 타입이지만 모든 종류 데이터를 다룸 (요즘에는 JSON을 더 많이 사용)


## Axios

: 브라우저와 Node.js에서 사용할 수 있는 Promise 기반의 HTTP 클라이언트 라이브러리 


- 클라이언트 및 서버 사이에 HTTP 요청을 만들고 응답을 처리하는 데 사용되는 JS 라이브러리

- 브라우저를 위한 XHR 객체 생성

- 간편한 API를 제공하며, Promise API 기반의 비동기 요청 처리

- XHR 객체 생성 및 요청 -> 응답 데이터 생성 -> JSON 데이터 응답 -> Promise 객체 데이터를 활용해 DOM 조작 


## Promise

: 비동기 처리는 작업 완료 순서에 따라 처리되는 방식으로 UX를 개선하지만 개발자 입장에서 코드 실행 순서가 불명확하다는 단점 

1. 비동기 콜백 : 비동기 작업이 완료된 후 실행될 함수를 미리 정의 -> 콜백 지옥에 빠질 수 있음 

2. Promise : 비동기 작업의 최종 완료 또는 실패를 나타내는 객체 -> 콜백 지옥 문제 해결 

- 자바스크립트 비동기 작업 성공 또는 실패 결과 나타냄

- 작업이 끝나면 실행시켜준다는 약속 

예시) 

    const getCats = function () {
        axios({
            method: 'get',
            url: apiURL
        })
            .then((response) => {
            const imgUrl = response.data[0].url
            return imgUrl
            })
            .then((imgData) => {
            const imgElem = document.createElement('img')
            imgElem.setAttribute('src', imgData)
            document.body.appendChild(imgElem)
            })
            .catch((error) => {
            console.log(error)
            console.log('실패했다옹')
            })
        console.log('야옹야옹')
        }