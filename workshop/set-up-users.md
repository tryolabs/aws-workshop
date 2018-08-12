# IAM 사용자 설정하기

여러분도 이미 아시겠지만, AWS에는 루트(_root_)라 불리는 특별한 계정(`루트 계정`)이 있습니다.
이 계정은 사용자(users), 역할(roles) 그리고 결제 정보에 대한 초기 설정을 수행하는 데 사용됩니다. 
매일 작업에 사용할 관리자 권한을 가진 사용자를 생성하고,
[루트 계정으로 AWS에 로그인하지 않기](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#create-iam-users)를 권장합니다.
또한 루트 계정은 [멀티 팩터 인증 (MFA)](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#create-iam-users)을 활성화하고,
로그인할 때 여러분의 핸드폰(Android/iOS)에 설치된 [Authy](https://authy.com/) 같은 앱을 "두 번째 요소"로 이용하시길 권장합니다.

다음으로, 루트 계정을 이용하여 AWS 사용자 2개를 설정합니다.

하나는 console (웹 인터페이스)을 이용하여 AWS에 접근하는 데 사용됩니다.
다른 하나는 프로그래밍 방식(programmatically)으로 접근하는 데 사용됩니다:
AWS API, CLI, SDK 그리고 다른 개발 도구들을 위한 액세스 키 ID(**access key ID**), 보안 액세스 키(**secret access key**)를 생성합니다.

모든 계정은 몇 가지 관련 권한(Permission)을 가집니다.
해당 계정이 최소 권한을 가지도록 엄격하게 제한하는 것이 좋습니다.
특히 프로그램 방식 액세스는 더욱더 그러합니다.
권한(Permission)은 [정책(Policy)](http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)을 사용자 계정에 부여함으로써 처리됩니다.
여기에서 여러분은 다양한 AWS 서비스에 대한 접근 수준을 정의할 수 있습니다.

먼저, AWS console 사용자를 생성합니다:

1. 루트 사용자ID(AWS 가입에 사용한 email)로 AWS 관리 콘솔(Management Console)에 로그인.
2. "Security, Identity & Compliance" 섹션에서 **IAM**으로 이동.
3. 메뉴 Users 클릭.
4. 버튼 "Add user" 클릭.
5. Username에 `ConsoleUser`를 입력하고,
   **Select AWS access type** 섹션에 있는 **AWS Management Console access** 옵션을 선택한 후, 
   버튼 "Next" 클릭.
   **Require password reset** 옵션을 선택하여 다음번 로그인할 때 비밀번호를 수정하도록 합니다 (안전한 암호를 선택하십시오!).
6. **Attach existing policies directly** 선택.
7. `AdministratorAccess`를 검색하여 선택한 후, "Next" 클릭.
8. "Create user"를 클릭하여 사용자를 생성한 후, 메시지에 표시된 AWS Management Console 접근 URL 및 비밀번호를 텍스트 에디터에 복사해 둡니다.

이제, 새로운 사용자로 로그인합니다:

1. AWS console에서 로그아웃하고, 복사한 URL 링크를 이용하여 console에 접속합니다.
2. Username과 자동 생성된 비밀번호를 입력합니다.
3. 새로운 비밀번호를 입력합니다.

이다음으로, 프로그래밍 방식으로 액세스할 사용자를 생성합니다:

1. 아래 2~4번을 반복하여 사용자를 설정합니다.
2. Username에 `ProgrammaticUser`를 입력하고, **Select AWS access type** 섹션에서 **Programmatic access** 옵션을 선택.
   "Next" 클릭.
3. **Attach existing policies directly** 선택.
4. `PowerUserAccess`로 검색하여 이를 선택한 후, 버튼 "Next" 클릭. 
   물론 실제 상황에서는 더욱 제한적인 접근 권한을 가지는 정책(Policy)을 설계하고 이를 사용합니다.
5. "Download .csv" 클릭.

내려받은 CSV 파일에서 액세스 키 ID, 보안 액세스 키를 확인할 수 있습니다.
이는 여러분의 컴퓨터에 설치된 [AWS CLI를 설정](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)하는 데 필요합니다.
아직 AWS CLI가 설치되어 있지 않다면, [이곳 링크](http://docs.aws.amazon.com/cli/latest/userguide/installing.html)를 따라 해 보세요.

---
**도전 과제**: 
  1. 프로그래밍 방식 액세스 사용자에 `ViewOnlyAccess` 권한을 부여해 보세요. AWS CLI 를 사용하여 할 수 있다면 더욱 좋겠죠.
  2. 콘솔 액세스 사용자에게 MFA를 적용시켜 보세요. 이를 위해서는 여러분의 스마트폰에 가상 MFA 어플리케이션을 설치하여야만 합니다.

---

**다음:** [S3, RDS 그리고 EC2](/workshop/s3-web-ec2-api-rds/introduction.md).
