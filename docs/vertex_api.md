# Google Cloud Gemini API 키 발급 방법

참고 문서: <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start/api-keys?hl=ko&usertype=standard>

이 문서는 결제 계정이 연결된 표준 Google Cloud 사용자를 기준으로 Gemini Enterprise Agent Platform에서 사용할 Google Cloud API 키를 발급하는 방법을 정리한 것입니다.

> 테스트 단계에서는 API 키를 사용할 수 있지만, Google Cloud 문서는 프로덕션 환경에서는 API 키보다 애플리케이션 기본 사용자 인증 정보(ADC)를 권장합니다.

## 1. 사전 준비

1. Google 계정으로 로그인합니다.
2. [프로젝트 선택기](https://console.cloud.google.com/projectselector2/home/dashboard?hl=ko)에서 기존 Google Cloud 프로젝트를 선택하거나 새 프로젝트를 만듭니다.
3. [결제 사용 설정 여부](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled?hl=ko#confirm_billing_is_enabled_on_a_project)를 확인합니다.
4. [Agent Platform API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com&hl=ko)를 사용 설정합니다.

이 절차에서 만든 리소스를 계속 보관할 계획이 없다면 기존 프로젝트를 선택하기보다 새 프로젝트를 만드는 것이 좋습니다. 작업이 끝난 뒤 프로젝트를 삭제하면 해당 프로젝트에 연결된 리소스도 함께 정리할 수 있습니다.

API를 사용 설정하려면 일반적으로 `Service Usage Admin` 역할(`roles/serviceusage.serviceUsageAdmin`) 또는 `serviceusage.services.enable` 권한이 필요합니다.
프로젝트를 선택하거나 새로 만들 때도 계정에 필요한 프로젝트 관련 권한이 있어야 합니다.

## 2. 서비스 계정 API 키 생성 허용

조직 정책에서 서비스 계정을 통한 API 키 생성을 막고 있다면 먼저 정책을 변경해야 합니다.

1. Google Cloud Console에서 `IAM 및 관리자 > 조직 정책`으로 이동합니다.
2. 정책 목록에서 `iam.managed.disableServiceAccountApiKeyCreation`을 검색합니다.
3. `작업 > 정책 수정`을 클릭합니다.
4. `정책 소스`에서 `상위 정책 재정의`를 선택한 뒤 `규칙 추가`를 클릭합니다.
5. `시행` 값을 `사용 안함`으로 선택합니다.
6. `완료`를 클릭합니다.
7. `정책 설정`을 클릭하고, 확인 대화상자가 나오면 다시 `정책 설정`을 클릭합니다.

이 단계에는 조직 수준의 `조직 정책 관리자` 권한이 필요합니다. 권한이 없거나 조직 정책을 바꿀 수 없다면 API 키 대신 ADC 사용을 검토하세요.

## 3. 서비스 계정 만들기

1. Google Cloud Console에서 `IAM 및 관리자 > 서비스 계정`으로 이동합니다.
2. `서비스 계정 만들기`를 클릭합니다.
3. 서비스 계정을 다음과 같이 입력합니다.

```text
서비스 계정 이름: vertex-ai-runner
서비스 계정 ID: vertexairunner
```

4. `만들고 계속하기`를 클릭합니다.
5. `권한` 단계에서 역할 선택 메뉴를 열고 `Gemini Enterprise Agent Platform Express 사용자 (베타)` 역할을 선택합니다.
6. `계속`을 클릭합니다.
7. `완료`를 클릭합니다.

## 4. API 키 만들기

1. Google Cloud Console에서 `API 및 서비스 > 사용자 인증 정보`로 이동합니다.
2. `사용자 인증 정보 만들기 > API 키`를 클릭합니다.
3. API 키를 다음과 같이 설정합니다.

```text
이름: vertexaiapikey
서비스 계정을 통해 API 호출 인증: 선택
```

4. `서비스 계정 선택`을 클릭합니다.
5. 앞에서 만든 `vertex-ai-runner` 서비스 계정을 선택하고 `선택`을 클릭합니다.
6. `만들기`를 클릭합니다.
7. 생성된 API 키를 임시로 메모장 등에 복사합니다.

## 5. 로컬 환경에 API 키 설정

발급받은 API 키는 프로그램이 읽을 수 있는 위치에 저장해야 합니다. 이 프로젝트에서는 아래 방법 중 하나를 사용하면 됩니다.

### 방법 1. `api_key.txt` 파일 사용

가장 간단한 방법입니다. 프로젝트 루트 폴더에 `api_key.txt` 파일을 만들고, 발급받은 API 키만 한 줄로 넣습니다.

```text
makein_translator/
  api_key.txt         <-- 직접 생성
  main.py
  target/
  output/
```

`api_key.txt` 내용 예시:

```text
발급받은_API_키
```

파일 안에는 API 키 외 아무것도 넣지 않는 것이 좋습니다.

### 방법 2. Windows PowerShell에서 임시 설정

현재 열려 있는 PowerShell 창에서만 API 키를 사용할 때는 다음처럼 설정합니다.

```powershell
$env:GOOGLE_API_KEY="발급받은_API_키"
python main.py
```

PowerShell 창을 닫으면 이 설정은 사라집니다.

### 방법 3. Windows에 계속 저장

매번 API 키를 입력하고 싶지 않다면 `setx`로 저장할 수 있습니다.

```powershell
setx GOOGLE_API_KEY "발급받은_API_키"
```

`setx`로 저장한 값은 지금 열려 있는 PowerShell 창에는 바로 적용되지 않습니다. 새 PowerShell 창을 열고 프로그램을 실행하세요.

```powershell
python main.py
```

### 방법 4. macOS / Linux에서 설정

사용 중인 셸에 맞춰 `~/.bashrc` 또는 `~/.zshrc`에 다음 줄을 추가합니다.

```bash
export GOOGLE_API_KEY="발급받은_API_키"
```

변경사항을 바로 적용하려면 다음 중 하나를 실행합니다.

```bash
source ~/.bashrc
source ~/.zshrc
```

### 프로그램이 API 키를 찾는 순서

프로그램은 API 키를 다음 순서로 찾습니다.

1. `GEMINI_API_KEY` / `GOOGLE_API_KEY` 환경 변수
2. 프로젝트 루트의 `api_key.txt`
3. 실행 중 직접 입력

처음 사용하는 경우에는 `api_key.txt` 방식이 가장 편합니다. 여러 프로젝트에서 같은 키를 공통으로 쓰고 싶다면 환경 변수 방식을 사용하세요.

## ‼️ 주의사항

- API 키를 GitHub 같은 열린 공간에 공개하지 마세요.
- API 키가 노출되면 다른 사람이 프로젝트 할당량을 사용하거나 추가 비용을 발생시킬 수 있습니다.
- 가능하면 API 키 제한사항을 설정해 사용할 수 있는 API나 호출 범위를 제한하세요.
- 모바일, 웹, 클라이언트 앱에 API 키를 직접 넣으면 사용자에게 노출될 수 있습니다.
- 운영 환경에서는 API 키보다 애플리케이션 기본 사용자 인증 정보(ADC)를 사용하는 방식을 우선 검토하세요.
