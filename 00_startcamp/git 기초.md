# GIT
## 1. Git 이란?
- 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 **분산 버전 관리 프로그램**
- Git ≠ Github : Git은 버전관리를 위한 소프트웨어고, Github은 이 Git으로 원격전송된 프로젝트들이 저장되는 공간을 제공하는 서비스임.
</br>

## 2. GUI와 CUI
- 개념
  - GUI - **그래픽**을 통해 사용자와 컴퓨터가 상호작용하는 방식(마우스 사용)
  - CLI - **명령어**를 통해 사용자와 컴퓨터가 상호작용하는 방식
  
- 차이점
  - GUI는 CLI에 비해 사용하기 쉽지만 단계가 많고 컴퓨터의 성능을 더 많이 소모
  - 수 많은 서버, 개발 시스템이 CLI를 통한 조작 환경을 제공

- CLI (Git Bash)
    - mkdir, ls(list directory contents), cd
    - touch, start, rm
    - cd ../

- [참고] 절대경로와 상대경로
    - 절대경로: 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
    - 상대경로: 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
        - ./: 현재 작성하고 있는 폴더
        - ../: 현재 작업하고 있는 폴더의 부모 폴더

</br>

# GIT 시작하기

## 1. 초기화

- `git init` : `현재 디렉토리`를 `git 이 관리하는 디렉토리로 초기화`한다.

</br>

## 2. git 설정 (최초에만 설정)

```
$ git config --global user.name "이름"
$ git config --global user.email "메일 주소"
```

위 명령어를 통해 사용자의 이름과 메일 주소를 설정해준다.  

```
$ git config --global --list
혹은 $ git config --global -l
```

위 명령어를 통해 설정된 사항을 확인한다.

</br>

## 3. status

- Working Directory 와 Staging Area에 있는 파일들의 현재 상태를 알려주는 명령어
- add 나 commit 전에 한 번씩 확인해주면 좋습니다.

```
$ git status
```

- 상태
1. `Untracked`: Git 이 관리하지 않는 파일 혹은 한 번도 Staging Area 에 올라온 적 없는 파일
2. `Tracked`: Git 이 관리하는 파일
   1. `Unmodified`: 최신 상태
   2. `Modified`: 수정되었지만 아직 Staging Area 에는 반영되지 않은 상태
   3. `Staged`: Staging Area 에 올라간 상태

</br>

## 4. add

- `$ git add`: Working Directory -> Staging Area 로 파일을 이동시키는 명령어

```
# 특정 파일
$ git add <파일명>

# 특정 폴더
$ git add <폴더명>/

# 현재 디렉토리의 모든 파일/폴더
$ git add .
```
</br>

## 5. commit

- `$ git commit`: Staging Area -> Repository 로 파일을 이동시키는 명령어

```
$ git commit -m "커밋 메세지"
```

- `커밋 메세지` 를 반드시 작성해야 한다.
  - 커밋 메세지: 현재 변경 사항의 이유를 기록하므로, 의미있게 작성해야 한다.

</br>

![요약](../img/Image.png)

</br>

## 6. commit 내역 확인

```
$ git log
```

commit 내역 확인 가능
