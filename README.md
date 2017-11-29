# AWS Workshop

This workshop aims to introduce the reader to AWS and its infrastructure.
We will use an open source test application implemented in react and django + django-rest-framework. You can find the original repo [here](https://github.com/gothinkster/realworld).
We created a custom repo based on that one with modified settings to fit our future infrastructure.

# Preconditions:

You must have an AWS account. Don’t worry, you won’t go over the free tier limit.
If you want you can [set up a billing alarm](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-alarms.html), just in case.

# Content:

This workshop contains four sections: 
* [Set up users](/workshop/set-up-users.md)
* [Deploy the website on s3 with a database in RDS and API in EC2](/workshop/s3-web-ec2-api-rds/introduction.md)
* [Add a LoadBalancer and an AutoScaling Group](/workshop/elb-auto-scaling-group/introduction.md)
* [Create your own VPC with public and private subnets, modify your AutoScaling Group and LoadBalancer to work with your subnets and add a Bastion to access to your Api instancess thru SSH.](/workshop/vpc-subnets-bastion/introduction.md)

---

**Next:** Assuming you already have a AWS account you can proceed to [Set up users on AWS](/workshop/set-up-users.md) to get started.
