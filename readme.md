# Makein Translator

`패배 히로인이 너무 많아!` 일어판 원서를 한글로 번역하는 데 맞춰 용어집을 포함한 DOCX 번역기입니다. 이 프로젝트는 아래 원본 글의 내용을 다듬은 프로젝트입니다.

원본 링크: <https://gall.dcinside.com/mgallery/board/view/?id=failheroine&no=24868&search_head=40&page=1>

## 주요 기능

- DOCX 문서의 텍스트 번역
- 문서 안 이미지에 포함된 글자 번역 옵션
- 마지막 광고 이미지 번역 제외 옵션
- `glossary.csv`를 이용한 용어집 적용
- 번역 진행률 표시



## 폴더 구조

```text
makein_translator/
├─ main.py              # 실행 파일
├─ requirements.txt     # 필요한 파이썬 패키지 목록
├─ glossary.csv         # 번역 용어집
├─ docs/                # API 키 발급 등 추가 문서
├─ target/              # 번역할 DOCX 파일을 넣는 폴더
├─ output/              # 번역 결과가 저장되는 폴더
└─ modules/             # 내부 코드
```

## 목차

- [책 파일 얻는 방법](#책-파일-얻는-방법)
- [처음 실행하는 방법](#처음-실행하는-방법)
- [용어집 수정 방법](#용어집-수정-방법)
- [macOS / Linux에서 실행](#macos--linux에서-실행)
- [❓ 자주 생기는 문제](#-자주-생기는-문제)
- [⚠️ 주의사항](#️-주의사항)

## 책 파일 얻는 방법

번역할 전자책을 준비하는 방법은 아래 글을 참고하세요. 이 프로그램에서 최종적으로 번역하는 파일은 DRM이 해제된 `.docx` 형식이어야 합니다.

- Google Play Books에서 전자책 구매하기: <https://gall.dcinside.com/mgallery/board/view/?id=failheroine&no=5116>
- Rakuten Kobo에서 전자책 구매하기: <https://gall.dcinside.com/mgallery/board/view/?id=failheroine&no=24883>

## 처음 실행하는 방법

아래 설명은 Windows PowerShell 기준입니다.

### 1. Python 설치

Python이 설치되어 있지 않다면 먼저 설치합니다.

1. <https://www.python.org/downloads/> 에 접속합니다.
2. Python **3.11 이상 버전**을 다운로드합니다.
3. 설치할 때 **Add python.exe to PATH** 체크박스를 꼭 선택합니다.
4. 설치가 끝나면 PowerShell을 새로 열고 아래 명령어로 확인합니다.

```powershell
python --version
```

버전이 보이면 준비 완료입니다.

### 2. 프로젝트 폴더 다운 및 이동

GitHub를 처음 써본다면 ZIP 파일로 받는 방법이 가장 쉽습니다.

1. 초록색 **Code** 버튼을 누릅니다.
2. **Download ZIP**을 누릅니다.
3. 다운로드된 ZIP 파일의 압축을 풉니다.
4. 압축을 푼 폴더를 찾습니다. 보통 `Makein_Translator-main` 같은 이름으로 만들어집니다.

PowerShell에서 압축을 푼 폴더로 이동합니다.

예를 들어 `다운로드` 폴더에 압축을 풀었다면 아래 코드를 복사해 그대로 적으세요.

```powershell
cd $HOME\Downloads\Makein_Translator-main
```

직접 원하는 위치에 옮겨두었다면 그 폴더 경로로 이동하면 됩니다.

```powershell
cd C:\my_projects\Makein_Translator
```

### 3. 가상환경 준비

가상환경은 꼭 설정하지 않아도 됩니다. Python이 설치되어 있다면 이 과정을 건너뛰고 4번부터 실행해도 문제없습니다.

```powershell
pip install -r requirements.txt
python main.py
```

다만 가상환경을 사용하면 이 프로젝트에 필요한 패키지를 다른 Python 프로젝트와 섞이지 않게 따로 관리할 수 있습니다. 나중에 패키지 버전이 꼬이는 문제를 줄일 수 있으므로, 계속 사용할 프로젝트라면 가상환경 사용을 권장합니다.

간단히 한 번 실행해볼 목적이라면 가상환경 없이 진행해도 되고, 안정적으로 관리하고 싶다면 아래 단계를 따라 가상환경을 만들면 됩니다.

#### 3-1. 가상환경 만들기

```powershell
python -m venv .venv
```

#### 3-2. 가상환경 켜기

```powershell
.\.venv\Scripts\Activate.ps1
```

만약 실행 정책 오류가 나오면 PowerShell을 관리자 권한이 아닌 일반 권한으로 열고 아래 명령어를 한 번 실행한 뒤, 다시 가상환경을 켭니다.

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### 4. 필요한 패키지 설치

```powershell
pip install -r requirements.txt
```

### 5. API 키 준비

이 프로그램은 API 키를 아래 순서로 찾습니다.

1. `GEMINI_API_KEY` / `GOOGLE_API_KEY` 환경변수
2. 프로젝트 루트의 `api_key.txt`
3. 실행 중 직접 입력

매번 입력하기 싫다면 `api_key.txt` 파일을 만드는 방법을 추천합니다.

API 키가 아직 없다면 다음 문서를 참고하세요.

- [API 키 발급 방법](docs/vertex_api.md)

### 6. 번역할 파일 넣기

번역할 `.docx` 파일을 `target` 폴더 안에 넣습니다.

예시:

```text
target/
└─ sample.docx
```

현재 프로그램은 `target` 폴더 안의 첫 번째 파일을 번역합니다. 여러 파일을 한 번에 넣기보다는 하나씩 넣고 실행하는 것을 권장합니다.

### 7. 실행

```powershell
python main.py
```

실행하면 화면에 나오는 질문을 선택합니다.

- 추론 수준: 높을수록 더 꼼꼼할 수 있지만 시간이 오래 걸립니다. 최소도 충분히 읽을만 합니다.
- 이미지 번역: 문서 안 이미지의 글자까지 번역할지 선택합니다.
- 광고 이미지 번역: 문서 마지막에 붙은 광고성 이미지를 번역할지 선택합니다.

잘 모르겠다면 기본값 그대로 Enter를 눌러 진행해도 됩니다.

### 8. 결과 확인

번역이 끝나면 결과 파일이 `output` 폴더에 저장됩니다.

```text
output/
└─ [translated] sample.docx
```

번역 결과 예시가 궁금하다면 [텍스트 번역 결과](docs/result_txt.png), [이미지 번역 결과](docs/result_image.png) 파일을 참고하세요. 

위 예시에는 패배 히로인이 너무 많아! 8권의 내용 일부가 포함되어있습니다.

## 용어집 수정 방법

`glossary.csv` 파일을 수정하면 특정 단어를 원하는 표현으로 번역하도록 요청할 수 있습니다. 기본 제공 파일은 `패배 히로인이 너무 많아! 일어판` 번역에 특화되어 있습니다.

형식은 아래처럼 `일어,한글` 형태입니다.

```csv
ja,ko
負けヒロインが多すぎる！,패배 히로인이 너무 많아!
負けヒロインが,패배 히로인이
多すぎる！,너무 많아!
```

첫 줄인 `ja,ko` 줄은 제목 줄이므로 지우지 마십시오.

## macOS / Linux에서 실행

```bash
cd /path/to/makein_translator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export GOOGLE_API_KEY="여기에_API_키_입력"
python main.py
```

## ❓ 자주 생기는 문제

### `python` 명령어를 찾을 수 없다고 나와요

Python이 설치되어 있지 않거나 PATH 설정이 빠진 상태입니다. Python을 다시 설치하면서 **Add python.exe to PATH**를 체크했는지 확인하세요.

### 필요한 모듈이 없다고 나와요

가상환경을 켠 뒤 아래 명령어를 다시 실행하세요.

```powershell
pip install -r requirements.txt
```

### API 키 오류가 나와요

`GOOGLE_API_KEY`, `GEMINI_API_KEY`, `GOOGLE_CLOUD_API_KEY`, `api_key.txt` 중 하나에 올바른 API 키가 들어 있는지 확인하세요. `setx`로 설정했다면 PowerShell을 새로 열어야 적용됩니다.

### 번역할 파일이 없다고 나와요

`target` 폴더 안에 `.docx` 파일을 넣었는지 확인하세요.

## ⚠️ 주의사항

- API 사용량에 따라 Google/Gemini API 비용이 발생할 수 있습니다.
- 큰 문서나 이미지 번역은 시간이 오래 걸릴 수 있습니다.
- 이미지 번역을 켜면 텍스트만 번역할 때보다 훨씬 오래 걸릴 수 있습니다.
- 추론 수준을 높이면 번역 시간이 크게 늘어날 수 있으므로, 처음에는 최소 또는 기본값으로 테스트해 보세요.
- 원본 파일은 `target` 폴더에 그대로 두고, 번역본은 `output` 폴더에서 확인하세요.
- 번역할 문서는 본인이 합법적으로 사용할 권리가 있는 파일만 사용하세요.
- macOS / Linux에서의 동작은 직접 확인하지 못하였습니다. 작동이 안 될 경우 AI 등에게 물어보세요.
