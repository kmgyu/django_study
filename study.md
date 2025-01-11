# django study

1. 프로젝트 초기화
    ```
    django-admin startproject config .
    ```
    make config settings on current directory

    ```
    python manage.py runserver
    ```

    start the server

2. app 시작
    ```bash
    django-admin startapp pybo
    ```

비즈니스 로직들을 app 단위로 분리시키는게 목적인가?

생성된 파일이 하는일

migrations : migrations는 파일이 아닌 디렉터리이며 장고가 데이터베이스 테이블을 생성하고 수정하기 위한 파일들을 이곳에서 관리한다.
admin.py : 장고의 관리자 화면을 구성하는 파일이다. 이 곳에 코드를 추가하여 장고 관리자 화면을 제어할수 있다.
apps.py : 앱의 구성 정보를 정의하는 파일이다. (파이보 프로젝트에서 이 파일을 수정할 일은 없다.)
models.py : 데이터베이스 모델을 정의하는 파일이다.
tests.py : 앱을 테스트할 때 사용하는 파일이다.
views.py : 앱의 기능을 구현하는 파일이다. 앞으로 가장 많이 사용할 파일이다.

config/urls.py에서...
- views.index는 무엇인가?
views.py 파일의 index 함수를 의미한다.
- admin.site.urls의 역할은 무엇인가?

views.index로 미루어보아...
expressJS와 Nodejs를 찾아보긴 했는데 관련 내용으로 export/require?이 있지 않을까? 라우팅 관련 내용이니까 유사하다고 느꼈는데 교수님한테 말을 좀 정리해서 물어보장.

아무튼 간에, Response를 하는 메서드들을 property로 가지고 있고 이를 호출하는 형태인 것 같다.
점프투장고 2-01에서는 httpresponse를 보내기 때문에 HTML을 반환한다.
restful하게 보내려면 JSON으로 serialize해야하나...?

pybo.urls를 통해 각 app별 url을 관리하고, 루트에서 url을 관리하는 형태
스프링부트도 루트 컨트롤러를 이렇게 만들어야 하나?