# Bastion instance

A bastion is a regular EC2 instance located in one of the public subnets, which allows incoming traffic through SSH. Through this instance, we will be able to SSH into any instance located in the private subnet (assuming they accept incoming traffic from the bastion).

## Create a Bastion Instance
1. Go to **EC2** under **Compute section**.
2. Click on Launch Instance.
3. Look for Ubuntu Server (make sure it says Free tier eligible) and click Select.
4. Select `t2.micro` and then click on Next: Configure Instance Details.
5. On Network, select your VPC.
6. As subnet, you can pick any of the two public ones. For example, `10.0.1.0-us-east-1a`.
8. Click Next: Add Storage.
9. Leave the default settings and click Next: Add Tags.
10. Click Add Tag.
11. Fill Key with `Name` and in Value with `bastion`.
12. Click on Next: Configure Security Group.
13. Write a meaningful name in **Security group name**.
14. Click Review and Launch.
15. Click Launch.
16. Select your key pair and click Launch Instances.
17. Select the Bastion on the instances list and on Actions/Networking select Change Security Groups.
18. Check the default security group of your VPC. Make sure that 2 security groups are checked, the default one and the one you created during the creation of the bastion.

## Accessing private instances through the bastion

Now you have a public instance that can be accessed via SSH, but what you want is to be able to access to your private instances.

To access the instances, you need to SSH with the PEM (key pair) that you had generated when launching the first one.

### Option 1: setup SSH agent forwarding
You can read a guide [here](https://developer.github.com/v3/guides/using-ssh-agent-forwarding/). Even though the examples check access to GitHub, it's analogous to accessing our private instances.

You can setup SSH so it's easier to access protected instances going transparently through the bastion. [Here](https://www.cyberciti.biz/faq/linux-unix-ssh-proxycommand-passing-through-one-host-gateway-server/) you have a nice guide.

### Option 2: copy the PEM file from your machine to the bastion instance
Ideally, you would be using a different PEM file for the bastion and the instances (increased security).

1. Copy the file with `scp ~/.ssh/<your-pem-file>.pem ubuntu@<public-ip-of-the-bastion>:/home/ubuntu/.ssh -i ~/.ssh/<your-pem-file>.pem`.
2. SSH into the bastion.
2. Make sure the file permissions are correct: `chmod 400 <pem-file-name>`.
3. SSH into the instances (from the bastion) with `ssh <private-ip-of-webserver-instance> -i <pem-file-name>`.

---
**Extra mile:** `ssh` to one of the instances in the private subnets and `tracepath` to an external host. Do the same for a instance in the public subnets. What's the difference?

---

**Next:** [finish the deploy](/workshop/vpc-subnets-bastion/08-finishing-up.md).

# Bastion instance

Bastion  dms Public Subnet 중 하나에 있는 일반 EC2 인스턴스로, SSH를 통해 들어오는 트래픽을 허용합니다. 이 Bastion 인스턴스를 통해 Private Subnet 에 있는 모든 인스턴스로 SSH를 수행 할 수 있습니다 (Bastion 에서 들어오는 트래픽을 수락한다고 가정).

## Create a Bastion Instance
1. AWS Management Console 에서 **Compute section** 의 **EC2** 로 이동하세요.
2. Launch Instance 를 Click 하세요.
3. Ubuntu 서버를 찾아 (무료 티어를 사용할 수 있는지 확인하세요) 선택하여 Click 하세요.
4. `t2.micro` 를 선택하고 이후 Next: Configure Instance Details 를 click 하세요.
5. Network 에서, VPC 를 선택하세요.
6. subnet 에서, 2개의 Public 중 1개를 선택하세요. 예를 들어, `10.0.1.0-ap-northeast-1a`.
8. Next: Add Storage Click 하세요.
9. 기본 Settings 을 하고 Next: Add Tags Click 하세요.
10. Add Tag 를 Click 하세요.
11. `Name` 에 Key 를 입력하고 `bastion` 을 입력하거나 원하시는 것을 입력하세요.
12. Next: Configure Security Group Click 하세요.
13. **Security group name** 에 원하시는 것을 입력하세요.
14. Review and Launch 를 Click 하세요.
15. Launch 를 Click 하세요.
16. Key pair 를 선택하고 Launch Instances 를 Click 하세요.
17. EC2 Dashboard 에서 Instances list 를 보고 Bastion 을 선택하고 Actions/Networking Change Security Groups 을 선택하세요.
18. VPC 에서 default security group 을 확인하세요. 2 개의 Security Group 이 선택되었는지 확인하세요. Default Security Group 과 1개의 Security Group 을 작성되었습니다.

## Accessing private instances through the bastion

이제 SSH를 통해 액세스 할 수 있는 Public Instance 가 있지만 원하는 것은 Private Instance 에 액세스 할 수있는 것입니다.

인스턴스에 액세스하려면 첫 번째 인스턴스를 시작할 때 생성 한 PEM (키 쌍)으로 SSH를 수행해야 합니다.

### Option 1: setup SSH agent forwarding
가이드 [here](https://developer.github.com/v3/guides/using-ssh-agent-forwarding/)를 읽을 수 있습니다. 예제가 GitHub에 대한 액세스를 확인하더라도 개인 인스턴스에 액세스하는 것과 유사합니다.

Bastion 을 통해 투명하게 진행되는 보호된 인스턴스에 더 쉽게 액세스 할 수 있도록 SSH를 설정할 수 있습니다. [Here](https://www.cyberciti.biz/faq/linux-unix-ssh-proxycommand-passing-through-one-host-gateway-server/) 에 좋은 가이드가 있습니다.

### Option 2: copy the PEM file from your machine to the bastion instance
이상적으로는 Bastion 과 인스턴스에 대해 다른 PEM 파일을 사용하는 것입니다(보안 강화).

1. `scp ~/.ssh/<your-pem-file>.pem ubuntu@<public-ip-of-the-bastion>:/home/ubuntu/.ssh -i ~/.ssh/<your-pem-file>.pem` 과 같이 Copy 하세요.
2. Bastion 에 SSH 를 사용하게 됩니다.
2. 다음과 같이 Permission 권한을 부여하세요: `chmod 400 <pem-file-name>`.
3. Instances 로 SSH 를 (Bastion 으로 부터) `ssh <private-ip-of-webserver-instance> -i <pem-file-name>` 이와 같이 연결하세요.

---
**Extra mile:** `ssh` 는 Private Subnet 의 인스턴스 중 하나에 연결하고 `tracepath`를 외부 호스트에 전달합니다. Public Subnet 의 인스턴스에 대해서도 동일하게 수행하십시오. 차이점이 뭘까요?

---
**다음:** [finish the deploy](/workshop/vpc-subnets-bastion/08-finishing-up.md).