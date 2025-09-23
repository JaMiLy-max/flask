<details>
<summary>
### **Marshmallow 스키마란?**
</summary>
- 파이썬에서 사용되는 ORM/ODM(Object-Relational Mapper/Object-Document Mapper)과 함께 사용되는 라이브러리
- Marshmallow 스키마는 데이터의 구조와 타입을 정의합니다.
    - 예를 들어, 특정 API 요청이나 응답에서 예상되는 데이터 형식을 스키마로 정의할 수 있으며, 이를 통해 데이터 유효성 검사, 직렬화 및 역직렬화를 자동화할 수 있습니다.
- 복잡한 데이터 타입을 파이썬 데이터 타입으로 변환(직렬화)하고, 파이썬 데이터를 JSON과 같은 형식으로 변환(역직렬화)하는 데 사용(데이터 검증, 데이터 직렬화/역직렬화 등이 쉽게 가능해짐)
</details>

<details>
<summary>
### **Blueprint**
</summary>
애플리케이션의 특정 기능 별로 라우팅, 뷰 함수, 템플릿, 정적 파일 등의 관리가 가능
- **모듈화**: 블루프린트를 사용하면 애플리케이션의 서로 다른 부분을 별도의 모듈로 나누어 관리할 수 있습니다. 이는 코드의 재사용성을 높이고, 유지보수를 용이하게 합니다.
- **라우팅 관리**: 블루프린트는 자체 URL 규칙을 가지고 있으며, 이를 통해 애플리케이션의 라우팅을 체계적으로 관리할 수 있습니다.
- **기능별 분리**: 블루프린트를 사용하면 특정 기능에 대한 라우팅, 뷰 함수, 에러 핸들러, 템플릿 등을 그룹화할 수 있습니다.
</details>

* 목표 : RESTFull API를 작성 방법에 대해 익히고, 책 관리 API를 완성해서 제출하기
- 주제 : 책 관리 API 만들기
- 복습할 개념 :
    - [ ]  get, post, put, delete
    - [ ]  schemas 정의
    - [ ]  Python( class, function )

### 개요
    책 정보를 관리하는 간단한 RESTful API를 만들어야 합니다. 이 API는 책의 목록을 보여주고, 새로운 책을 추가하며, 특정 책의 정보를 업데이트하고 삭제할 수 있어야 합니다.

### 요구 사항

1. **애플리케이션 설정** (**`app.py`**)
    - Flask 애플리케이션을 생성하고, Flask-Smorest API를 설정합니다.
2. **책 스키마 정의** (**`schemas.py`**)
    - Marshmallow를 사용하여 책 정보를 위한 스키마를 정의합니다. 책은 최소한 'title'(제목)과 'author'(저자) 필드를 가져야 합니다.
3. **API 엔드포인트 구현** (**`api.py`**)
    - 책 목록을 보여주는 GET 엔드포인트를 만듭니다.
    - 새 책을 추가하는 POST 엔드포인트를 만듭니다.
    - 특정 책의 정보를 업데이트하는 PUT 엔드포인트를 만듭니다.
    - 특정 책을 삭제하는 DELETE 엔드포인트를 만듭니다.
4. **데이터 저장소**
    - 책의 데이터는 메모리 내의 간단한 리스트로 관리합니다.

### 개발 요구사항

1. Flask와 Flask-Smorest를 사용하여 위의 요구 사항을 만족하는 API를 구현합니다.
2. 각 파일(**`app.py`**, **`schemas.py`**, **`api.py`**)에 필요한 코드를 작성합니다.
3. 책 정보를 관리하는 로직을 구현하고, 적절한 HTTP 응답을 반환하도록 합니다.
4. Marshmallow 스키마를 사용하여 입력 데이터를 검증합니다.

### **파일별 설명**
- **`app.py`**: Flask 애플리케이션과 Flask-Smorest API의 기본 설정을 포함합니다. Swagger UI 경로도 설정됩니다.
- **`schemas.py`**: 책 정보를 위한 스키마를 정의합니다. 여기서는 책의 제목과 저자가 필요하며, 책의 고유 ID는 자동으로 설정됩니다.
- **`api.py`**: 책 목록을 관리하는 API 엔드포인트를 구현합니다. **`GET`**, **`POST`**, **`PUT`**, **`DELETE`** 메소드를 사용하여 책 목록을 조회, 추가, 수정, 삭제할 수 있습니다.


### 결과화면
[swagger](https://github.com/JaMiLy-max/flask/blob/main/day2/%EC%A0%9C%EC%B6%9C/My%20API.pdf)

[postMan](https://github.com/JaMiLy-max/flask/blob/main/day2/%EC%A0%9C%EC%B6%9C/postMan.pdf)
