# day05 경보 판단

## 이상한 줄
- 줄 번호(여러 개면 모두): 2, 3
- 이유: 출발이 IP주소이므로 인터넷의 PC인데, 도착이 DB이다. 구성도에는 인터넷에서 INSIDE로 가는 길이 없는데도 허용되었다

## 고친 구성도
```
INTERNET ──── FW ──┬── DMZ    ( WEB )  : WEB (443 open)
                   └── INSIDE ( DB )   : DB (3306 only from WEB)

```
