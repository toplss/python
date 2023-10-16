# python
## 설치 및 시작하기
brew install python3 

# 업데이트
python3 -m pip install --upgrade pip

# 장고 설치하기
pip3 install django

# 장고 설치 확인 하기 및 버전확인
python3 -m django --version


# 프로젝트 생성
django-admin startproject

# 프로젝트 run
[폴더 이동후] python3 manage.py runserver

## mysql 연동 
python3 -m pip install PyMySQL

## mysql 버전 문제시 mysqlclient 설치
pip install mysqlclient

## pip install mysqlclient 설치시  pkg-config 관련 error 발생시
brew install mysql pkg-config
