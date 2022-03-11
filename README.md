# django-practice

## Requirement
```bash
python3 -m venv venv
source venv/bin/activate
(venv) pip3 install -r requirements.txt
```

### start project
```bash
$ django-admin startproject do_it_django_prj .
```

### Run
```bash
$ python manage.py runserver
```

### Apply migration
```bash
$ python manage.py migrate
```

### Create admin user
```bash
$ python manage.py createsuperuser
```

### Create app
```bash
$ python manage.py startapp blog
```

### Apply database model
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### Apply bootstrap
- 부트스트랩에서 css, css.map 파일 가져오기
    - getbootstrap.com 에서 download
    - Compiled CSS and JS
    - bootstrap.min.css
    - bootstrap.min.css.map
- html head 에 추가
- 자바스크립트 코드 추가
    - jsDelivr copy & paste
- 부트스트랩에서 컴포넌트에서 필요한 것들 보고 선택
    - eg) Navbar
    - 예제의 html 코드 사용
- 부트스트랩 공식 홈페이지의 Examples 에서 샘플 확인 후 적용
    - startbootstrap.com 에서도 좋은 템플릿들 있음
        - 상세 페이지에서 다운로드
        - Live preview 로 확인 가능