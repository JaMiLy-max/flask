- 목표 : Flask의 기본 구조와 Route 그리고 Jinja 템플릿의 활용 방법을 익히기
- 주제 : Flask와 Jinja 템플릿으로 사용자 데이터 웹 페이지에 출력
- 복습한 개념
    - [ ]  __name__
    - [ ]  @app.route()
    - [ ]  변수 출력 : {{ … }}
    - [ ]  제어 구조 : {% … %}
    - [ ]  {% if user %} / {% else %} / {% endif %}
    - [ ]  {% for item in item_list %} / {% endfor %}
 
- 사용자 데이터 정의
  ```python
  users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"}
  ]
  ```

- **Jinja 템플릿 작성**: **`templates`** 폴더 안에 **`index.html`** 파일을 만들고, Jinja 템플릿을 사용하여 사용자 목록을 HTML로 렌더링.
- **웹 페이지 디자인**: **`index.html`**에서 각 사용자의 이름(**`name`**)과 사용자 이름(**`username`**)을 목록 형태로 표시.
- **애플리케이션 실행 및 테스트**: Flask 애플리케이션을 실행하고, 브라우저에서 **`http://localhost:5000/`** 주소로 접속하여 결과를 확인.
- 결과확인
  
  <img width="600" alt="preview" src="https://github.com/user-attachments/assets/0cd9e7c6-cf3f-48cb-a973-dea7f365fb44" />
