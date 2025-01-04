# 일기쓰기
- 제목(line editor)
- 날짜(date picker)
- 날씨(맑음, 흐림, 비옴)
- 한일(여러줄 입력가능)

# 오늘의 업무 입력 폼
- 날짜
- 거래처
- 미수금
- 완료한 일
- 하단에는 저장 수정 삭제 버튼이 있다.

# 프로그램 워크플로우
workflow:
  - step: "사용자 로그인"
    description: "사용자가 이메일과 비밀번호로 로그인합니다."
    input: 
      - "이메일"
      - "비밀번호"
    output: 
      - "사용자 인증 토큰"
    error_handling:
      - "잘못된 이메일 또는 비밀번호"
      - "계정 잠금"
    roles:
      - "사용자"
      - "인증 시스템"

  - step: "대시보드 로드"
    description: "로그인 성공 후 사용자 맞춤형 대시보드가 표시됩니다."
    input:
      - "사용자 인증 토큰"
    output:
      - "대시보드 UI"
    error_handling:
      - "세션 만료"
    roles:
      - "사용자"
      - "프론트엔드"

  - step: "데이터 요청"
    description: "사용자는 필요한 데이터를 서버에 요청합니다."
    input:
      - "API 요청"
    output:
      - "JSON 형식의 데이터"
    error_handling:
      - "API 호출 오류"
      - "권한 없음"
    roles:
      - "사용자"
      - "API 서버"

  - step: "데이터 저장"
    description: "사용자가 변경한 데이터를 서버에 저장합니다."
    input:
      - "사용자 입력 데이터"
    output:
      - "저장 성공 메시지"
    error_handling:
      - "데이터베이스 저장 실패"
    roles:
      - "사용자"
      - "데이터베이스 서버"

  - step: "로그아웃"
    description: "사용자는 안전하게 로그아웃합니다."
    input: 
      - "사용자 요청"
    output:
      - "세션 종료"
    error_handling:
      - "세션 종료 오류"
    roles:
      - "사용자"
      - "인증 시스템"