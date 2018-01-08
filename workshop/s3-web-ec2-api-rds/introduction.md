# Introduction

We are ready to start the deployment of our website.

The first step will be the frontend. Because it’s a static website, we can create an [S3 bucket](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html), put all the code in it and serve it as a static website. Think of an S3 bucket as a folder in the cloud, which can be setup for access from the outside world via a URL (and even help a bit with your application's routes).

To automate the build, we will use [CodeBuild](https://aws.amazon.com/codebuild/), AWS service to build projects on the go.
CodeBuild will pull our repository, build the webpage and copy the build directory to S3. The configuration is specified on `buildspec.frontend.yml` on the root folder of our repo.

In this section we will also create our Postgres database in [AWS RDS](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html).

Finally we will use [CodeDeploy](http://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) to automate the deployment of our API to the EC2 instances. It will pull the repo from our EC2 instances and start gunicorn. You should take a look at the configuration files located in `infrastructure/aws/codedeploy`.

> **Important:** after you are done with this workshop, you will ideally clean up your account, so you are not billed anymore. This means that you need to delete everything you have created.
>
> Many resources in AWS [can be tagged](https://aws.amazon.com/answers/account-management/aws-tagging-strategies/). If something can be tagged, then you should tag it with a **unique name**. Later, you can use the [Tag Editor](https://aws.amazon.com/blogs/aws/resource-groups-and-tagging/) to find your tagged resources to delete, and make sure you don't leave anything behind.

---

**Next:** learn how to [serve a static website from S3](/workshop/s3-web-ec2-api-rds/01-serve-website-from-s3.md).