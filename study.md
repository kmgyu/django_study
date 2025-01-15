# django study

1. 프로젝트 초기화
    ```bash
    django-admin startproject config .
    ```
    make config settings on current directory

    ```bash
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

3. migrate
migrations 만들기
```bash
python manage.py makemigrations
```
모델이 수정되거나 추가되었을 시 해당 명령어를 실행해야 한다.

migrate 하기
```bash
python manage.py migrate
```
앱의 설정을 적용한다.
DB가 필요한 앱은 migrate가 필요하다.
settings.py의 installed_apps에 있는 앱들이 해당된다.
databases를 이용해 DB 엔진도 설정가능.
DB 관련 세팅인데... 아마 ORM이랑 DB랑 매칭시킬 때 사용하는 것 아닐까?
모르니 찾아봐야 겠다.

```bash
python manage.py sqlmigrate pybo 0001
```
해당 명령어를 통해 0001_initial.py의 쿼리 확인 가능.
쿼리 조회만 되고 실제론 안함.

```bash
python manage.py shell
```
장고 셸 실행 명령어
파이썬/장고 형식으로 시행되서 django 라이브러리 및 앱을 이용가능한 셸인듯...? 더 알아봐야할 것

Model.objects.get(id=???) 쿼리?를 통해 아이템 조회 가능
Model.objects.filter(???) 를 통해 1개 이상 조회 가능.
옵션이 많이 있다는 데 where 문 역할을 하는 듯?

```python
q.subject = 'Django Model Question'
# 저장 시(update)
q.save()
# 삭제 시
q.delete()
```

```python
a = Answer.objects.get(id=1)
a.question # question FK 조회 가능

# question에서 answer 조회.
q.answer_set.all() # PK가 answer의 FK라 다음과 같이 조회가능.
# 연결모델명_set을 통해 조회 가능 (1:N 관계라 _set 붙임.)
```

4. superuser
```bash
python manage.py createsuperuser
```

5. test data
```bash
python manage.py shell
from pybo.models import Question
from django.utils import timezone
for i in range(300):
    q = Question(title='테스트 데이터입니다:[%03d]' % i, content='내용무', create_date=timezone.now(), modify_date=timezone.now())
    q.save()
```
장고 셸을 실행하여 테스트 데이터를 만들어준다.
그냥 스크립트 파일로 만들어도 무방한가? 공부 필요

6. 페이지네이션
paginator
paging을 위한 기능
(갱장하다)
paginator 내부에도 다양한 속성이 존재한다.
iterator를 이용한 클래스같다. iterable 한 클래스인건 맞는데 흠...

7. template filter
게시물 번호 넘버링에 씌였지만, 더 활용할 방법이 있을 것 같다.
app의 templatetags에 [app]_filter.py 형식으로 만들어준다.(만들고 재시작 필요)
