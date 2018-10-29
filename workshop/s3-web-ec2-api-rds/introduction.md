# 소개

우리는 웹 사이트 배포를 시작할 것입니다.

첫 번째 단계는 프론트 엔드가 될 것입니다. 정적 웹 사이트이기 때문에, 우리는 [S3 bucket](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html) 을 생성 할 수 있고, 그 곳에 모든 코드를 넣을 수 있고, 정적인 웹사이트로서 제공할 수 있습니다. S3 버킷을, 외부에서 URL을 통해 액세스 할 수 있도록 설정할 수 있는(응용 프로그램의 경로를 조금이라도 도울 수 있는) 클라우드의 폴더로 생각하십시오.

빌드를 자동화하기 위해, 우리는 지속적으로 프로젝트를 빌드하기 위한 AWS service 인 [CodeBuild](https://aws.amazon.com/codebuild/) 를 사용할 것입니다.
CodeBuild 는 우리의 레파지토리에서 소스를 가져오고, 웹페이지에 빌드하고, S3에 빌드 디렉토리를 복사할 것입니다. 설정값은 우리의 레파지토리의 root 폴더에 있는 (/buildspec.frontend.yml) `buildspec.frontend.yml` 파일에 명시 되어 있습니다.

우리의 API를 EC2 인스턴스에 자동으로 배포하기 위해, [CodeDeploy](http://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) 를 사용할 것입니다. EC2 인스턴스로 repo를 가져오고 서버를 시작합니다(gunicorn). 전체 배포 프로세스는 `appspec.yml` 파일에 설명되어 있습니다.[here](/appspec.yml)

마지막으로 데이터베이스는 PostgreSQL 인스턴스로 [AWS RDS](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) 를 사용하여 호스팅됩니다.

요약하면, 이 섹션에서 우리는 아래 내용을 생성할 것입니다.:

- 정적 프런트엔드를 호스팅하기 위한 s3 버킷
- 프런트엔드를 배포하기 위한, S3 버킷에 결과물을 복사하기 위한 CodeBuild 설정
- API를 EC2 인스턴스에 배포하기위한 CodeDeploy 설정
- RDS PostgreSQL 인스턴스.

> **중요:** 이 워크숍을 마친 후에는 계정에 사용중인 인스턴스를 중지할 것이므로 더 이상 청구되지 않습니다. 즉, 이번에 신규로 생성한 모든 것을 삭제해야합니다.
>
> AWS의 많은 자원은 [태그를 달 수 있습니다](https://aws.amazon.com/answers/account-management/aws-tagging-strategies/). 만약 태그 할 수 있는 어떤 항목이 있으면, **unique name** 으로 태그를 지정해야 합니다. 나중에, 여러분들은 지울 태그된 리소스를 찾기 위해 [Tag Editor](https://aws.amazon.com/blogs/aws/resource-groups-and-tagging/) 를 사용할 수 있고, 뒤에 어떤것도 남기지 않을 것이라 확신합니다.

---

**다음:** [S3에서 정적 웹 사이트를 제공하는 방법](/workshop/s3-web-ec2-api-rds/01-serve-website-from-s3.md)을 배우십시오.
