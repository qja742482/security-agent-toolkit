# 4과목 Day 5 도커 컴포즈로 서버 두 대 켜기 · 웹 서버 로그 만들기 · 오후 (허현범 · 2026-11-06(금))

> **쓰는 법**
> - 문제를 풀 때마다 그 문제 제목 아래 질문에 답합니다.
> - 질문마다 `쓸 내용:` 에 무엇을 쓰면 되는지 적혀 있습니다. 그대로 `답:` 뒤에 씁니다.
> - 출력이나 코드를 붙여 넣는 질문은 `답:` 아래 빈 코드 상자에 붙여 넣고, 설명은 `답:` 뒤에 씁니다.
> - 「왜」를 묻는 질문은 한 단어로 끝내지 말고, 내 화면에서 본 값이나 배운 내용을 근거로 이유까지 씁니다.
> - 🔍 는 이 교시에서 꼭 알아야 할 핵심 질문입니다. 답을 못 찾았으면 「모름 — 막힌 곳: …」 이라고 씁니다. 🔍 가 없는 질문도 못 적으면 같은 말을 씁니다.

---

## 5교시 · 도커 복습 · 컴포즈로 서버 두 대 한 번에 켜기

### 문제 5-1 · 서버 한 대를 복습하고 컴포즈로 두 대 켜기

- (가) 5교시 순서의 서버 켜기 · 확인 명령(`docker images` 부터 `curl` 까지)과 그 결과를 친 순서대로 붙여 넣고, 서비스 이름 두 개와 각 서비스의 포트를 적어 주세요.
  - 쓸 내용: ① 명령과 결과를 친 순서대로(코드 상자에 붙여 넣기): `docker images` · `docker run` · `docker ps` · `docker stop` · `docker compose up -d` · `docker compose ps` · `curl` 두 개 (`docker pull` 은 받았을 때만, `pwd` · `touch` · `ls` 는 붙이지 않아도 됩니다) ② 서비스 이름 두 개 ③ 각 서비스의 포트
  - 답:
1. 
```
$ docker images nginx:1.28
REPOSITORY          ID             DISK USAGE    CONTENT SIZE    EXTRA
nginx:1.28          146adea4768b         240MB          65.8MB        

$ docker run -d --rm -p 8080:80 --name web-run nginx:1.28
31191a41259b2a0b0306f6d6d47a66564613016d9814f822681f33c0318b0e1b

$ docker stop web-run
web-run

$ docker compose up -d
[+] up 3/3
 ✔ Network anomaly_detection_default  Created                                                                                                                 0.0s
 ✔ Container anomaly_detection-web2-1 Started                                                                                                               0.5s
 ✔ Container anomaly_detection-web1-1 Started                                                                                                               0.7s

$ docker compose ps
NAME                       IMAGE       COMMAND                  SERVICE    CREATED         STATUS         PORTS
anomaly_detection-web1-1   nginx:1.28  "/docker-entrypoint.…"   web1       6 seconds ago   Up 6 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
anomaly_detection-web2-1   nginx:1.28  "/docker-entrypoint.…"   web2       6 seconds ago   Up 6 seconds   0.0.0.0:8081->80/tcp, [::]:8081->80/tcp

$ curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080
200

$ curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8081
200
```
2. web 1, web 2
3. web 1 = 8000 or 8080
   web 2 = 8081

- (나) 🔍 서버 두 대를 `docker run` 으로 켜는 것과 `compose.yaml` 과 `docker compose up -d` 로 켜는 것을 비교해, 컴포즈가 더 나은 점을 두 가지 적어 주세요.
  - 쓸 내용: ① 컴포즈가 더 나은 점 두 가지
  - 답:
  1: 일괄 관리 및 자동화 편의성
  2: 설정의 코드화 및 네트워크 통합

- (다) 🔍 보안 사고가 난 뒤 감사팀이 「사고 당시와 같은 구성으로 서버를 다시 켜 보라」고 요청했습니다. 팀원 한 명은 3주 전에 긴 `docker run` 명령을 직접 쳐서 서버를 켰는데 그 명령을 기억하지 못합니다. 다른 팀은 `compose.yaml` 을 깃허브에 올려 두었습니다. 두 팀이 같은 구성을 다시 켤 수 있는지 비교하고, 파일에 `nginx:1.28` 처럼 버전을 적어 두는 것이 이런 재현에 왜 중요한지 적어 주세요.
  - 쓸 내용: ① 두 팀의 차이 ② 버전을 적어 두는 것이 재현에 중요한 이유
  - 답:
  1. docker run을 사용한 팀은 오랜 시간이 지나 복잡한 명령어 옵션(포트 매핑, 볼륨, 환경변수 등)을 기억하지 못하면 사고 당시의 서버 환경을 정확하게 다시 켜기 어렵습니다. 반면, compose.yaml 파일을 깃허브에 관리한 팀은 명령어를 기억할 필요 없이 docker compose up -d 명령 하나로 사고 당시와 동일한 서버 및 네트워크 구성을 완벽하고 신속하게 재현할 수 있습니다.
  2. 정확한 버전(nginx:1.28)을 명시하여 고정해 두어야 당시의 환경과 동일한 바이너리 및 설정 상태를 온전히 보장받아 객관적이고 정확한 보안 감사와 포렌식 조사를 수행할 수 있습니다.

- (라) 🔍 팀원 세 명이 같은 `compose.yaml` 로 서버를 켰는데 한 명의 PC 에서만 `8081` 번 포트를 다른 프로그램이 쓰고 있어서 `web2` 가 켜지지 않았습니다. 이 사람이 파일의 어느 줄을 어떻게 바꾸면 되는지 적고, 바꿔도 서버 안에서는 여전히 `80` 번 포트로 동작하는 이유를 적어 주세요. 이 사람이 `curl` 로 확인할 때 달라지는 점도 적어 주세요.
  - 쓸 내용: ① 바꿀 줄과 바꾼 모양 ② 서버 안은 그대로 80 인 이유 ③ curl 주소의 달라지는 점
  - 답: 
  1. compose.yaml 파일 내 web2 서비스의 ports: 설정 부분에서 충돌이 발생하는 8081 포트를 사용 가능한 다른 빈 포트(예: 8082)로 변경합니다.

  바꾼 모양: - "8082:80" (또는 8082:80/tcp)
  2. 컨테이너 내부에서 실행 중인 Nginx 웹 서버 자체는 고유한 내부 네트워크 포트인 80번으로 요청을 처리하도록 빌드되어 있기 때문
  3. 기존의 http://localhost:8081 주소 대신, 변경한 호스트 포트 번호에 맞춰 http://localhost:8082로 주소를 바꾸어 curl 요청을 보내야 합니다.

## 6교시 · 서버마다 접속 범위 정하기 · 설정 바꿔 적용하기

### 문제 6-1 · 서버마다 접속 범위를 정해 컴포즈 파일로 적용하기

- (가) 1번과 5번의 `docker compose ps` 출력을 붙여 넣고, 접속 범위가 바뀐 기존 서비스와 새로 추가된 서비스를 따로 적어 주세요.
  - 쓸 내용: ① 1번 출력(코드 상자에 붙여 넣기) ② 5번 출력(코드 상자에 붙여 넣기) ③ 접속 범위가 바뀐 기존 서비스 ④ 새로 추가된 서비스
  - 답:
1. 
```
docker compose ps
mkdir logs
touch compose.secure.yaml
docker compose -f compose.secure.yaml up -d
docker compose -f compose.secure.yaml ps
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8081
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8082
cat logs/access.log
grep " 404 " logs/access.log | wc -l
grep " 404 " logs/access.log > logs/web_404.log
docker compose -f compose.secure.yaml down
ls logs

```
2. docker compose -f compose.secure.yaml ps)
3. web1, web2 (기존에는 외부 모든 네트워크(0.0.0.0)에서 접근 가능했으나, 보안 설정 후 로컬(127.0.0.1)에서만 접근할 수 있도록 접속 범위가 제한됨)
4. 없음

- (나) 🔍 `"8081:80"` 과 `"127.0.0.1:8081:80"` 은 누가 접속할 수 있는지가 어떻게 다른가요? 관리 화면이나 데이터베이스 서버를 이렇게 설정하는 이유도 적어 주세요.
  - 쓸 내용: ① 두 포트 줄에서 누가 접속할 수 있는지의 차이 ② 관리 화면 · 데이터베이스를 이렇게 설정하는 이유
  - 답:
  1. 내 컴퓨터(로컬)뿐만 아니라 외부 네트워크나 다른 사용자(공유기 대역 등)도 접근할 수 있습니다.
  2. 공격 표면적(Attack Surface)을 최소화하기 위함입니다.

- (다) 🔍 `up -d` 의 출력에서 `web1` 은 `Running`, `web2` 는 `Recreated`, `web3` 은 `Created` 였습니다. 서버마다 출력이 다른 이유와, 운영 중인 서비스의 설정을 바꿀 때 이것이 왜 도움이 되는지 적어 주세요.
  - 쓸 내용: ① 서버마다 출력이 다른 이유 ② 서버를 끊지 않고 바꿀 수 있는 것의 쓸모
  - 답:
  1. Running (web1): compose.yaml 파일에서 설정이나 이미지가 변경되지 않아 기존 컨테이너가 아무런 수정 없이 그대로 유지 및 실행 중이기 때문입니다.

Recreated (web2): 포트 번호 등 compose.yaml의 설정 내용이 수정되었기 때문에, 기존 컨테이너를 중지하고 바뀐 설정으로 새롭게 교체(재생성)되었기 때문입니다.

Created (web3): 설정 파일에 새롭게 추가된 서비스로, 이번 실행 과정에서 컨테이너 객체가 처음으로 생성되었기 때문입니다.
  2. 전체 시스템이나 다른 정상적인 서비스(web1 등)를 통째로 중단(Downtime)시킬 필요 없이, 설정이 변경된 특정 서비스(web2)나 새로 추가된 서비스만 골라서 실시간으로 안전하게 반영할 수 있습니다. 이를 통해 서비스의 연속성을 보장하고 운영 중인 시스템의 안정성을 크게 높일 수 있습니다.

### 마무리 · 오늘 만든 것을 깃허브에 올리기

- (가) `git status` 를 쳤을 때 `.env` 나 `.venv` 가 보였는지, 보였다면 어떻게 했는지 적어 주세요.
  - 쓸 내용: ① `.env` · `.venv` 가 보였는지 ② 보였다면 한 조치
  - 답:
  1. 안보였다
