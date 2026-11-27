# 처음 만나는 컴퓨터 사용 AI: 화면을 보고 대신 일하는 에이전트

AI에게 질문하는 시대에서, AI가 실제 브라우저와 컴퓨터 화면을 보고 버튼을 누르고 결과를 확인하는 시대로 넘어가고 있습니다. 이 책은 개발자가 아니어도 컴퓨터 사용 에이전트가 무엇인지, 어떤 원리로 작동하는지, 어디까지 맡겨도 되는지 이해하도록 돕습니다.

## 이 책에서 다루는 것

- 챗봇과 브라우저 에이전트의 차이
- 화면·DOM·접근성 트리·스크린샷을 읽는 방식
- 관찰 → 계획 → 클릭 → 검증의 실행 루프
- Browser Use, Browser Harness, Playwright의 역할
- 검색·자료조사·반복 입력을 안전하게 자동화하는 방법
- 로그인·권한·파일·결제·개인정보의 경계
- 프롬프트 인젝션과 악성 웹페이지
- 실패·재시도·중단·복구·감사 로그
- 비개발자용 첫 실습과 업무별 체크리스트
- 데스크톱 앱과 모바일 화면에서 달라지는 권한·상태·완료 증거

## 자료 확인 기준

2026년 11월 2일. Browser Use·Browser Harness와 Playwright의 공식 자료를 다시 확인했습니다. 공개 관심 지표는 품질·안전성의 증거로 쓰지 않습니다. 외부 트래픽 보고서와 설문은 조사 방법과 표본을 확인할 때만 참고합니다.

## 상태

기존 00~19장 초안을 업무 사례와 확인 절차로 보강하고 장마다 고유 도식을 넣었습니다. 제목의 범위에 맞춰 데스크톱·모바일 장을 더해 00~21장으로 개정 중입니다. 실제 위키독스 책 생성과 공개 발행은 별도 단계이며, 공개 화면 검수 뒤 상태를 갱신합니다.

2026년 11월 27일부터 기존 초안을 공식 제품 문서와 실제 따라 할 수 있는 절차에 맞춰 개정하고 있습니다. [제작 하네스](docs/AGENT_HARNESS.md)에 에이전트별 작업 순서와 완료 기준을, [작업 대기열](docs/WORK_QUEUE.md)에 현재 상태를 기록합니다. 이 개정은 아직 공개 발행을 뜻하지 않습니다.

## 목차

- [00. 이 책을 읽기 전에](pages/00-preface.md)
- [01. AI 브라우저란 무엇인가](pages/01-what-is-ai-browser.md)
- [02. 챗봇·자동화·에이전트의 차이](pages/02-chatbot-automation-agent.md)
- [03. AI는 화면을 어떻게 읽는가](pages/03-perception.md)
- [04. AI는 다음 행동을 어떻게 고르는가](pages/04-action-loop.md)
- [05. 브라우저 하네스와 실행 환경](pages/05-browser-harness.md)
- [06. Browser Use·Playwright·컴퓨터 사용 도구](pages/06-tools.md)
- [07. 검색과 자료조사를 맡기는 방법](pages/07-research.md)
- [08. 폼 입력과 반복 업무 자동화](pages/08-forms.md)
- [09. 로그인·계정·개인정보의 경계](pages/09-identity.md)
- [10. 프롬프트 인젝션과 악성 웹페이지](pages/10-prompt-injection.md)
- [11. 승인·권한·브라우저 세션 보호](pages/11-permissions.md)
- [12. 실패·재시도·중단·복구](pages/12-recovery.md)
- [13. 결과를 검증하고 기록하는 방법](pages/13-verification.md)
- [14. AI 브라우저를 평가하는 방법](pages/14-evaluation.md)
- [15. 비개발자용 첫 실습](pages/15-first-tutorial.md)
- [16. 업무별 자동화 레시피](pages/16-recipes.md)
- [17. 비용·속도·데이터 관리](pages/17-operations.md)
- [18. 실제 도입 체크리스트](pages/18-adoption.md)
- [19. 브라우저 밖의 컴퓨터 화면을 다루는 AI](pages/19-desktop-computer-use.md)
- [20. 모바일 앱 화면을 다루는 AI](pages/20-mobile-computer-use.md)
- [21. AI가 읽는 화면의 미래](pages/21-outlook.md)

## 출처 기록

- [자료 검증 기록](docs/SOURCE_LEDGER.md)
- [작업 상태](docs/STATUS.md)
