# AWS Workshop

This workshop aims to introduce the reader to managing infrastructure using [Amazon Web Services](https://aws.amazon.com/) (AWS).

We will learn to deploy real applications. As our demo app, we will use an [open source](https://github.com/gothinkster/realworld) test application called Conduit, which is handy to learn new frameworks because the same app has implementations in multiple frameworks for backend and frontend. In particular, we will use the version built with [React](https://reactjs.org/) and [Django](https://www.djangoproject.com/) + [Django-Rest-Framework](http://www.django-rest-framework.org/) backend.

In this repo, you can find the backend and frontend components, both with modified settings to fit our future infrastructure.

# Preconditions

You must have an AWS account. Don’t worry, you won’t go over the free tier limit.

If you want to, you can [set up a billing alarm](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-alarms.html) to avoid these situations, just in case.

# Content

This workshop contains four sections:

1. [Set up users](/workshop/set-up-users.md).
2. [S3, RDS and EC2](/workshop/s3-web-ec2-api-rds/introduction.md). Here, you will deploy the website on S3, the backend will store the data using RDS and the API will be deployed on EC2.
3. [Load Balancer and Auto Scaling Group](/workshop/elb-auto-scaling-group/introduction.md).
4. [VPC configuration and Bastion instance](/workshop/vpc-subnets-bastion/introduction.md). Here, you will setup your own VPC with public and private subnets, modify your Auto Scaling Group and Load Balancer to work with those and add a Bastion to access to your API instances through SSH.

---

**Next:** assuming you already have an AWS account, you can [get started](/workshop/set-up-users.md).
