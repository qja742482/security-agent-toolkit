# 🤖 Agent Core (`agent_core`)

자동화된 데이터 처리, 보안 분석 규칙 연동, LLM 프롬프트 및 알림 자동화를 수행하는 코어 에이전트 시스템입니다.

---

## 📁 프로젝트 구조 (Directory Structure)

```text
agent_core/
├── 📄 01_0928_am_exceptions_logging.py      # 예외 처리 및 로깅 파이프라인
├── 📄 01_0929_am_regex_detection_rules.py  # 정규식 기반 탐지 규칙 모듈
├── 📄 01_0930_am_requests_api_client.py    # 외부 API 호출 및 HTTP 클라이언트
├── 📓 02_0928_pm_nested_json.ipynb         # 중첩 JSON 데이터 파싱 및 전처리 실습/검증
├── 📓 02_0929_pm_rules_api.ipynb           # 탐지 규칙 API 연동 테스트
├── 📓 260922_variables_and_lists.ipynb      # 기초 파이썬 파이프라인 모듈 테스트
├── 📓 260923_am_conditions_loops_control.ipynb # 제어문 및 루프 기반 자동화 로직
├── 📓 260923_pm_functions_files_csv.ipynb  # 파일 및 CSV 데이터 핸들링
├── 📓 261002_am_webhook_cli.ipynb          # Webhook 알림 및 CLI 모듈
├── 📓 261002_pm_trigger_scheduler.ipynb    # 스케줄러 및 트리거 연동
├── 📓 261006_am_llm_prompt.ipynb           # LLM 프롬프트 엔지니어링 및 테스트
├── 📓 261006_pm_agent_tools.ipynb          # 에이전트 도구(Tools) 구현 및 검증
├── 📓 261007_am_report_summary.ipynb       # 일간/주간 요약 보고서 전처리
├── 📓 261007_pm_report_generator.ipynb     # 최종 보고서 자동 생성
├── ⚙️ config.json                          # 에이전트 설정 파일
├── 📄 notifier.py                          # 알림(Webhook, 메시지) 전송 모듈
├── 📄 pipeline.py                          # 메인 에이전트 실행 파이프라인
├── 📝 daily_report_20261008.md             # 일간 생성 보고서 예시
├── 📝 day08_retrospective.md               # 개발 회고록
└── 📄 README.md                            # 프로젝트 설명 문서
