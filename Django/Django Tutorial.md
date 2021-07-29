

# Django Tutorial



## 장고의 이해

장고는 파이썬으로 작성된 **오픈 소스 웹 애플리케이션 프레임워크**이다. 현재는 장고 소프트웨어 재단에 의해 관리되고 있다. 고도의 데이터베이스 기반 웹사이트를 작성하는 데 있어서 수고를 더는 것이 장고의 주된 목표이다.



- 장고의 처리 흐름

![image](https://user-images.githubusercontent.com/80219821/127499330-43c9585b-a999-4e5d-a008-cbc9275ad919.png)

웹 클라이언트의 요청을 받아 MTV(Model-Template-View) 모델에 따라 처리하는 과정이다.

=> 클라이언트로부터 요청을 받으면 URLconf 모듈을 이용하여 URL을 분석한다.

=> URL 분석 결과를 통해 해당 URL에 매칭되는 뷰들 실행

=> View는 자신의 로직을 실행하고, 데이터베이스 처리가 필요하면 모델을 통해 처리하고 그 결과 	 반환

=> View는 자신의 로직 처리가 끝나면 Template을 사용하여 클라이언트에 전송할 HTML 파일 생성

=> View는 최종 결과로 HTML 파일을 클라이언트에게 보내 응답한다.



---



## 장고 프로젝트 만들기

**충돌을 막기위해 (djangovenv)라는 가상환경을 만들어서 진행**

1. 명령프롬프트 창에서 지정된 폴더로 이동하여 다음 명령을 실행시켜 장고 프로젝트 생성![image](https://user-images.githubusercontent.com/80219821/127500297-c46ca232-5e9a-4705-8dd7-11ca22ff852a.png)





2. 생성된 studyporject 폴더로 이동해서 **python manage.py runserver** 를 입력하고 실행시켜서 장고에 내장도니 서버 가동![image](https://user-images.githubusercontent.com/80219821/127500546-620feb41-352e-4da9-9563-cf6fe1e41e6e.png)



3. 크롬 브라우저에서 http://localhost:8000/ 으로 이동하면 장고 기본 웹 페이지 출력되는 것을 확인 가능하다.

![image](https://user-images.githubusercontent.com/80219821/127500719-bc432fef-dc3d-47b5-a94b-042d55228ad4.png)



---



## 앱 만들기

1. 파이참으로 가서 가상환경으로 프로젝트를 open하고 아래의 Terminal창을 open



2. firstapp 이라는 장고 앱 생성

![image](https://user-images.githubusercontent.com/80219821/127501855-ffeb38d7-a575-4453-be48-1baf75d6403d.png)



3. firstapp 이라고 장고앱을 생성하면 다음과 같은 디렉토리 구조가 생성된다.

![image](https://user-images.githubusercontent.com/80219821/127502137-8ca4825c-4ae5-4193-ab25-1c456be8544b.png)



4. firstapp의 [views.py]와 studyproject의 [settings.py], [urls.py]안의 내용을 수정한다.

```python
#firstapp - views.py
from django.http import HttpResponse
def welcome(request):
    return HttpResponse("<h1>장고 공부를 재미있게 합시다!!</h1>")


#studyproject - urls.py
from django.contrib import admin
from django.urls import path, include
import firstapp.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', firstapp.views.welcome), 
]


#studyproject - settings.py의 일부분 (환경을 한국어와, 한국시간대로 변경)
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

-> views.py는 실행시킬 로직을 함수로 만든다고 생각하면 된다

-> urls.py는 말 그대로 url을 만드는 것

 (http://localhost:8000/welcome/으로 들어가면 firstapp에 있는 views의 welcome 함수 로직을 실행)



5. Terminal에 **python manage.py runserver** 을 입력해서 서버 가동

![image](https://user-images.githubusercontent.com/80219821/127503286-8485d88b-6afa-4366-bf22-bfba58c68866.png)



6. chrome으로 확인

![image](https://user-images.githubusercontent.com/80219821/127503356-f26645c1-341e-44c2-9075-ce6463d4ee27.png)



- 하지만 보통 위의 firstapp처럼 하지않고 아래와 같이 각 앱에 templates 폴더를 만들어서 홈페이지가 어떻게 보일 것인지를 작성한다.

![image](https://user-images.githubusercontent.com/80219821/127504140-72b23930-b5cc-4aa8-8cc7-9a4e68def46a.png)



- 장고로 구현하는 웹 사이트 구성

  ![image](https://user-images.githubusercontent.com/80219821/127504559-8c906cb5-ded5-4bb8-847e-5499ca224489.png)

  