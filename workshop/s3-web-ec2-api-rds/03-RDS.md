# RDS

## RDS에서 PostgreSQL 인스턴스 만들기
1. **Database** 섹션 아래에 있는 **RDS** 로 이동하십시오.
2. **Launch a DB Instance**를 클릭하십시오.
3. PostgreSQL 로고를 클릭하십시오, _"RDS 무료 사용 등급에 해당하는 옵션 만 활성화"_ 체크 박스를 선택하고 Next을 클릭하십시오.
4. _DB Instance identifier_ 에 이름을 입력하십시오.(나중에 필요하므로 잊지 마십시오).
5. 사용자 이름과 비밀번호를 입력하고 Next를 클릭합니다 (다시 말하지만 나중에 필요합니다).
6. **Publicly Accessible** 에 대해 No 를 선택하십시오.
7. 이용가능한 Zone: `us-east-1a`.
8. **VPC security groups** 에서 _Select existing VPC security groups_ 를 선택하고, [EC2 인스턴스 시작](/workshop/s3-web-ec2-api-rds/02-EC2-instances.md#launch-your-first-ec2-instance)할 때 너가 생성한 보안 그룹을 선택하십시오.
9. DB 이름을 선택하고 인스턴스 실행을 클릭합니다 (다시 말하면 나중에 데이터베이스 이름이 필요합니다).
10. 너의 DB 인스턴스 뷰를 클릭하십시오.

이제 우리의 인스턴스가 생성됩니다. 이전 섹션에서 작성한 보안 그룹의 모든 인스턴스를 연결할 수 있도록 액세스를 구성합니다.

## Parameters Store 에서 DB 파라미터 추가

이전과 마찬가지로 데이터베이스 이름, 사용자 이름, 암호 및 끝점을 포함하여 매개 변수 저장소에 저장된 일부 변수가 필요합니다. 이 변수는 [이 파일](/backend/conduit/settings/ec2.py)에서 참조되므로 Django는 데이터베이스에 액세스 할 수 있습니다.

1. **Database** 섹션에 있는 **RDS** 로 이동하십시오.
2. 인스턴스를 클릭하십시오.
3. 데이터베이스의 세부 정보를 확인하고 **Endpoint**를 복사하십시오. 이것은`DATABASE_HOST`의 값이 될 것입니다.
4. **Compute** 섹션 아래 있는 **EC2** 로 이동하십시오..
5. 왼쪽메뉴에서 Parameter Store를 선택하십시오.
6. Create Parameter를 클릭하십시오.
7. `/prod/api/DATABASE_NAME` 의 이름을 입력하고, "PostgreSQL 데이터베이스의 이름"과 같은 의미있는 설명을 입력하십시오.
8. 이전에 선택한 DB 이름을 value 속성에 입력하십시오..
9. create parameter and close를 클릭하십시오.
10. 이제 유저이름과 호스트에 대해 동일한 작업을 수행해야합니다.
  1. 유저이름으로 `/prod/api/DATABASE_USER` 를 이름과 데이터베이스 사용자 이름으로 입력하고 value로 입력하십시오.
  2. 호스트의 경우 이전에 값으로 복사 한 이름과 호스트 이름으로 `/prod/api/DATABASE_HOST` 를 입력하십시오.
11. `/prod/api/DATABASE_PASSWORD` 에 대해서도 같은 과정을 반복하되 **Type: Secure String** 로 선택하고 KMS Key ID로 키 `workshopkey` 를 선택하십시오.

이제 데이터베이스 매개 변수를 설정하고 암호를 암호화했습니다. EC2 인스턴스만 해독 할 수 있습니다.

---
**도전과제:**

- Postgres 인스턴스에 'ping'할 수 있습니까?
- 실행중인 EC2 인스턴스를 통해 DB에 연결하십시오.

---

**다음:** [CodeDeploy project to deploy your API](/workshop/s3-web-ec2-api-rds/04-code-deploy.md) 만들기.
