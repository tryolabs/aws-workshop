# S3로부터 정적 웹 사이트 제공하기

## 버킷 만들기

우선 웹사이트를 제공할 곳에서 버킷을 만들어야 한다.

1. AWS Console에서 **Storage section** 아래의 **S3**로 이동하여 버킷 생성을 클릭하십시오.
2. 버킷의 이름을 입력하십시오. 
버킷 이름은 AWS의 모든 기존 계정 및 지역에서 고유해야합니다. 
버킷을 만든 후에는 버켓의 이름을 바꿀 수 없으므로 이름을 현명하게 선택하십시오. 
Amazon은 DNS 호환 버킷 이름 사용을 제안합니다. [여기](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html#bucketnamingrules)에서 이에 대한 추가적인 정보를 찾으실 수 있습니다.
3. S3 버킷의 리전을 선택하세요. 여러분이 원하는 어떤 리전이든 선택할 수 있습니다. 그러나 AWS는 [리전별로 가격이 다릅니다](https://aws.amazon.com/s3/pricing/). 이번 실습에서 우리는`미국 동부(버지니아 북부)`를 선택할 것입니다.
4. Create를 클릭하세요. 우리는 나중에 속성을 수정할 것입니다.
5. 일단 만들어지면, 버킷 이름을 클릭하고 속성(Properties)탭을 클릭하여 이동 한 다음 **정적 웹 사이트 호스팅(Static website hosting)을 클릭**한 후에 **이 버킷을 사용하여 웹 사이트를 호스팅(Use this bucket to host a website)** 를 선택 하십시오.
6. Index document와 Error document란 에는`index.html`을 넣습니다. 이후에 우리는 **웹 사이트**에 접속하기 위해 상단에 표시된 **Endpoint URL**를 사용할 것 입니다. 텍스트 에디터를 열어 Endpoint의 주소를 적어 놓으시기 바랍니다.
> 입력란에 index.html이 미리 표시 되어 있어 마치 사전에 입력되어 있는것처럼 보이지만 반드시 손으로 입력해 주셔야만 **Save**버튼이 활성화 됩니다.
7. Save 버튼을 클릭하세요.
8. **권한(Permissions)** 탭에서 **버킷 정책(Bucket Policy)** 버튼을 클릭하고, 모든 객체를 읽을 수있게 만들기 위해 다음 정책을 추가하십시오:
  ```
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Sid": "AddPerm",
              "Effect": "Allow",
              "Principal": "*",
              "Action": "s3:GetObject",
              "Resource": "arn:aws:s3:::<여러분의 버킷이름>/*"
          }
      ]
  }
  ```
> 위 예제에서 여러분의 버킷 이름을 입력할때 꺽쇠<>는 필요 없습니다.

9. 저장 버튼을 누르세요.
> 버킷 내용이 공개되었다는 경고메세지가 나오지만 이번 실습에서는 신경쓰지 않아도 됩니다.

## 매개 변수 저장소에`WEBSITE_BUCKET_NAME`을 추가하십시오.

모든 어플리케이션에는 각각의 배포 때마다 고유한 설정이 있어야합니다: 디버그 사용할지 여부, 데이터베이스 서버의 주소, Third Party 에 대한 서비스를 사용을 위한 비밀 키 또는 액세스 토큰 등등. 이들 중 일부는 안전하게 저장해야합니다 (ex. keys API tokens). 많은 사람들이 이를 위해 [환경 변수](https://en.wikipedia.org/wiki/Environment_variable) 를 사용하지만 안전하다 라고 말할 순 없습니다.

[AWS Parameters Store](http://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-paramstore.html) 는 이를 위해 고안된 서비스로 우리 시스템의 변수를 저장하는 데 사용합니다. 이렇게하면 우리에게 상수를 저장하고, 나중에 다른 배포 단계동안에도 사용할 수 있습니다. 우리는 버킷 이름을 저장하여 시작합니다.

1. **Storage** **section** 에서 **S3** 로 이동하십시오. 
2. 버킷의 세부 정보를 보고 만들었던 버킷의 이름을 복사하십시오.
3. **Compute section**.에서 **EC2** 로 이동하십시오.
4. 왼쪽 탐색 메뉴 하단 에서 **Parameter Store** 를 선택하십시오.
5. **Create Parameter** 를 클릭하십시오.
6. **Name**에 `/prod/codebuild/WEBSITE_BUCKET_NAME`을 입력하고 **Description**란에는 파라미터가 의미하는 바에 대한 설명 (예. "웹사이트용 버킷 이름")을 입력하십시오. **Type**란은 **String**이 선택된 그대로 두시면 됩니다.
7. **Value**에는 `s3://<your-bucket-name>`을 입력하십시오(꺽쇠<>는 입력할 필요가 없습니다).
8. Create Parameter 를 클릭하십시오.

이제 우리가 [여기에](/buildspec.frontend.yml) 셋팅 한 것처럼 'aws ssm get-parameter'로 버킷 이름을 검색 할 수 있습니다. 또한 [AWS SSM Agent](http://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) 를 사용하여 AWS 웹 콘솔에서 인스턴스 구성을 관리 할 수 있습니다.


## S3 웹 사이트 버킷에 대한 full access 권한을 얻는 정책을 만듭니다.

[AWS Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) 내에서, 너가 사용하는 모든 AWS 리소스에 대해 다른 권한을 지정할 수 있습니다. 예를 들어, 특정 S3 버킷에 대한 전체 액세스를 가능하게하는 정책을 만들 수 있습니다. 이것이 바로 우리가 할 일입니다. 앞으로 우리는 프로젝트를 프로그래밍적으로 빌드하고 그것을 S3에 저장해야합니다.

1. **Security, Identity & Compliance** 에서 **IAM** 으로 이동하십시오.
2. Policies 을 클릭하십시오.
3. Create Policy 를 클릭하십시오.
4. **Import managed policy** 를 클릭하십시오.
5. 'AmazonS3FullAccess'를 검색하고 선택하십시오 (사전 정책이지만 당신이 직접 build 할 수도 있습니다).
6. **JSON** 탭을 클릭하여 JSON본문에서 `Resource`의 `"*"`부분을 `["arn:aws:s3:::<여러분의 버킷이름>", "arn:aws:s3:::<여러분의 버킷이름>/*"]`으로 대체 합니다. 
> 위 예제에서 여러분의 버킷 이름을 입력할때 꺽쇠<>는 필요 없습니다.
7. **Review policy** 를 클릭하십시오.
8. 정책 이름(예 : S3WebsiteFullAccess)을 선택하고 Create Policy 을 클릭하십시오.

이제 우리는 웹 사이트 버킷에 대한 전체 액세스 (목록 작성, 업데이트, 삭제 등)를 허용하는 정책을 가지고 있습니다. 다음 섹션에서 어떻게 사용할 수 있는지 보도록하겠습니다.

## CodeBuild 안에서 프런트앤드에 빌드 및 배포하기 위해 프로젝트를 생성하십시오.

앞서 언급했듯이 [AWS CodeBuild](https://aws.amazon.com/codebuild/)는 프로젝트를 빌드하는 AWS 서비스입니다. CodeBuild에게 무엇을 할 것인지를 지시하기 위해 우리는`buildspec.frontend.yml` 파일을 만들었습니다. CodeBuild는 먼저 repository를 pull 한 다음 [해당 파일](/buildspec.frontend.yml)에 지정된 명령을 실행합니다. 아시다시피, 우리는 프로젝트를 새로 설치하는 데 필요한 것을 지정했습니다. 생성 된 파일은 S3에 결과 파일을 업로드하기 위해 `npm build` 와 `aws s3 sync` 를 사용하여 빌드를 완료 합니다.

준비하기 위해 다음 단계를 진행하세요:

1. **Developer Tools** 섹션 아래 있는 **CodeBuild** 로 이동하십시오.
2. Get Started 를 클릭하세요 (이미 다른 프로젝트가 있다면 Create Project 를 클릭하십시오).
3. 프로젝트 이름(Project Name)에 `Hands-on-project` 입력하고 설명(Description)을 작성하십시오(선택).
4. Source 섹션에서:
    1. 소스 제공자(Source provider)로서 **Github** 를 선택하십시오.
    2. repository 옵션을 선택하십시오.
    3. 필요한 경우 AWS와 Github을 연결하십시오.
    4. repository URL을 채우거나 Github 계정에서 하나의 repository를 선택하십시오.
5. Environment 섹션에서:
    1. OS는 `Ubuntu`를 선택하고 런타임은 `Node.js`를 선택하십시오.
    2. 버전은 `aws/codebuild/nodejs:8.11.0`을 선택하십시오.
    3. BuildSpec 이름을`buildspec.frontend.yml` (따라야할 스탭을 가지고 있는 yaml 파일)로 변경하십시오.
6. 이슈 섹션에서 _No artifacts_을 선택하십시오.
7. Service Role 섹션에서:
    1. 당신의 계정에서 Create a service role 를 선택하십시오.
    2. role의 이름을 선택하고 이름을 `codebuild-aws-workshop-service-role` 로 지정하십시오.
8. Continue를 클릭하십시오.
9. Save를 클릭하십시오.

이제 CodeBuild Application을 만들었습니다. 우리는 S3 버킷에 파일을 추가 할 수있는 권한이 없기 때문에 실행할 수 없습니다. 그래서 우리는 "role" 이라는 정책을 초기에 만들어 냈습니다. 모든 것이 제대로 작동하려면 우리는 정책을 역할에 첨부해야 합니다.

## CodeBuild role에 정책 첨부

[role](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) 은 AWS 내부에서 사용 권한을 정의합니다. 이러한 권한은 AWS 사용자와 마찬가지로 정책 형태로 제공됩니다. 특정 작업을 실행해야하는 특정 EC2 서비스 (심지어 인스턴스)와 같은 것들은 특정 역할에 연결되어 실행될 수 있으므로 역할에 부여 된 권한을 얻습니다.

이전에 우리는 S3 버킷에 대한 전체 액세스를 허용하고 CodeBuild 응용 프로그램에 새로운 역할을 할당하는 정책을 만들었습니다. 이제 정책에 역할을 첨부하여 CodeBuild에 S3 버킷에 대한 액세스 권한을 부여합니다. 또한 Parameter Store 에서 설정 한 변수의 값을 쿼리 하기 위하여 SSM에 대한 액세스 권한을 부여하기 위해 다른 정책을 첨부해야합니다.

**Website full access**

1. Security, Identity & Compliance 아래 IAM으로 이동하십시오. 
2. Roles 를 클릭하십시오.
3. CodeBuild 프로젝트 생성시 생성 된 역할을 볼 수 있어야합니다.
4. Attach Policy를 클릭하십시오.
5. S3 웹 사이트 버킷에 대한 전체 액세스 정책을 검색하여 선택하고 정책 첨부를 클릭하십시오.

**SSM read access**

1. Attach Policy 를 다시 클릭하십시오.
2. `AmazonSSMReadOnlyAccess`를 검색하고 Attach를 클릭하십시오.

---
**도전 과제:** CLI를 사용하여 `WEBSITE_BUCKET_NAME`의 값을 얻으십시오.

---

**다음:** [EC2 인스턴스](/workshop/s3-web-ec2-api-rds/02-EC2-instances.md).
