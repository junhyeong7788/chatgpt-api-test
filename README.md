## 아나콘다 base 자동활성화 끄기

conda config --set auto_activate_base false

## 파이썬 가상환경 (window)

python -m venv 가상환경이름
가상환경이름₩Scripts₩activate

## 파이썬 가상환경 ( macOS )

python -m venv 가상환경이름
가상환경이름₩Scripts₩activate
각 해당 폴더로 이동 한 후 가상환경 생성

## 파이썬 가상환경 라이브러리 txt파일 생성

pip freeze > 파일명.txt

## git pull error

_git pull origin master error_

1. fatal: couldn't find remote ref master
2. fatal: Need to specify how to reconcile divergent branches.  
   -> 해결
3. git config pull.rebase true : rebase 후 pull
4. git config pull.rebase false : revase 없이 pull
5. git config pull.ff only : fast-forward일때만 pull 허용

- rebase : 새 브랜치가 시작된 분기점 커밋을 기준 브랜치의 가장 최근커밋으로 변경하는 작업
- rebase는 git history가 깔끔해질 수 있지만, 부주의하게 사용할 경우 별도의 알림없이 git history를 영구적으로 변경할 수 있기 때문에 ff-only방식을 추천
