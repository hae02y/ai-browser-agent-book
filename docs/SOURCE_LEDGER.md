# 자료 검증 기록

확인일: 2026-11-02. 기존 외부 보고서·설문은 2026-10-26에 기록한 자료이며, 제품 설명에는 공식 문서를 우선합니다.

| 자료 | URL | 확인한 내용 |
|---|---|---|
| Browser Use 공식 GitHub | https://github.com/browser-use/browser-use | 브라우저 에이전트 기능과 공개 스타 수치 |
| Browser Harness 공식 GitHub | https://github.com/browser-use/browser-harness | 로그인된 실제 Chrome을 에이전트가 사용하는 구조와 공개 스타 수치 |
| Browser Use 조직 저장소 | https://github.com/browser-use | 관련 프로젝트·벤치마크·릴리스 활동 |
| Stack Overflow AI 2026 | https://survey.stackoverflow.co/2026/ai | 코딩 에이전트 사용률과 AI 사용 행태 |
| HUMAN State of Agentic Traffic | https://www.humansecurity.com/learn/blog/september-2026-state-of-agentic-traffic | 2026년 9월 브라우저 에이전트 트래픽 점유율 |
| DataDome AI Traffic Report | https://datadome.co/threat-research/ai-traffic-report-q3-2026/ | 2026년 9월 에이전트 브라우저 트래픽 증가 신호 |
| Playwright 공식 문서 | https://playwright.dev/docs/intro | 브라우저 자동화의 기본 개념과 도구 |
| Chrome DevTools Protocol | https://chromedevtools.github.io/devtools-protocol/ | 브라우저 제어 계층의 공식 설명 |
| Playwright Locators | https://playwright.dev/docs/locators | 역할·라벨 등으로 화면 요소를 찾는 방법 |
| Playwright Actions | https://playwright.dev/docs/input | 입력·클릭·업로드의 자동화 동작 |
| Playwright Authentication | https://playwright.dev/docs/auth | 인증 상태 재사용과 저장 파일의 주의점 |
| OWASP LLM01 Prompt Injection | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | 외부 웹페이지·문서의 간접 프롬프트 주입 위험 |

## 편집 원칙

GitHub stars와 트래픽은 관심의 신호이지 품질·안전성의 증거가 아니다. 값이 빨리 바뀌는 수치는 본문에서 순위 근거로 쓰지 않는다. 프로젝트 설명과 실제 보안 검토를 분리한다. 기존 00~19장에 쓰인 SVG 20개는 2026-11-02에, 새 데스크톱·모바일 장의 SVG 2개는 2026-11-27에 개념을 설명하려고 자체 제작했다. 모두 제품 화면이나 실험 결과가 아니다.

## 2026-11-27 컴퓨터 사용 에이전트 공식 자료 재확인

기존 2026-11-02 자료는 당시 초안의 근거다. 아래는 이번 개정에서 직접 확인한 제품 자료이며, 제품 기능과 제공 범위는 장별 집필 시 다시 확인한다.

| 구분 | 공식 자료 | 이번 개정에서 확인할 구분 |
| --- | --- | --- |
| OpenAI API computer use | [Computer use](https://developers.openai.com/api/docs/guides/tools-computer-use) | 모델의 행동 제안, 개발자 실행기의 수행, 새 화면을 돌려주는 루프 |
| ChatGPT Work | [Using cloud browser in ChatGPT](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt) | 사용자용 별도 클라우드 브라우저, 사이트 접근·로그인·확인 단계 |
| 과거 ChatGPT agent | [ChatGPT agent 도움말](https://help.openai.com/en/articles/11752874-chatgpt-agent) | 문서 상단에 더는 제공되지 않으며 ChatGPT Work 사용을 안내함. 아래에 남은 과거 사용법 문단을 현재 기능으로 인용하지 않음 |
| Anthropic computer use | [Computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) | 스크린샷·마우스·키보드로 데스크톱 환경을 조작하는 도구와 실행 주체 |
| Anthropic browser use | [Browser use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool) | 웹페이지 전용 도구와 개발자 측 브라우저 실행 환경 |
| Google Gemini | [Computer Use](https://aistudio.google.com/docs/computer-use) | 화면 관찰·행동·실행기 반복과 지원 환경; 모델·지원 범위는 확인일과 함께 서술 |
| Microsoft Foundry | [Browser automation](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/browser-automation) | 관리형 원격 브라우저, 페이지 요소 기반 조작과 사람의 개입 |
| Microsoft Windows 365 | [Computer use sample](https://learn.microsoft.com/en-us/samples/microsoft/agent365-samples/w365-computer-use-sample/) | 클라우드 PC의 화면 기반 조작과 로그인 인계 예시 |
| 웹 에이전트 연구 | [WebArena](https://arxiv.org/abs/2307.13854) | 웹 작업 평가의 구조와 범위 |
| 컴퓨터 사용 연구 | [OSWorld](https://arxiv.org/abs/2404.07972), [OSWorld 2.0](https://arxiv.org/abs/2606.29537), [EgoUseBench](https://arxiv.org/abs/2611.34466) | 화면·운영체제·장기 작업·변하는 사용자 맥락의 평가 범위. 논문 수치는 재실험 결과로 표현하지 않음 |
| 공개 읽기 실습 | [IANA 예약 도메인](https://www.iana.org/domains/reserved), [RFC 2606](https://www.rfc-editor.org/info/rfc2606/) | 문서 예시용 도메인과 원문 대조 기준. 제품 에이전트 실습을 실제 실행한 근거는 아님 |

위 자료를 확인한 것은 해당 제품의 직접 사용이나 이 책의 실습 성공을 뜻하지 않는다. 실제 화면 캡처와 테스트 결과는 별도 기록이 있어야 한다.
