# Introduction

We are ready to start the deployment of our website.

## Frontend
The first step will be the frontend. Because it’s a static website, we can create an [S3 bucket](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html), put all the code in it and serve it as a static website. Think of an S3 bucket as a folder in the cloud, which can be setup for access from the outside world via a URL (and even help a bit with your application's routes).

To automate the build, we will use [CodeBuild](https://aws.amazon.com/codebuild/), an AWS service to build projects on the go.
CodeBuild will pull our repository, build the webpage and copy the build directory to S3. The configuration is specified on `buildspec.frontend.yml` on [the root folder of our repo](/buildspec.frontend.yml).

Bare in mind that the frontend isn't complete. This means that while you will be able to navigate it, none of the actions you take will have effect on the back end. For example, signing up or in doesn't currently work. However, hitting the API endpoints for signing up or in _does_ work. This is a problem with the frontend alone, so the concepts related to `aws` still apply.

## API
The API will be deployed to EC2 instances. In order to automate the deployment, we will use [CodeDeploy](http://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html). It will pull our repo to the EC2 instances and start our server (gunicorn). The full deploy process is described in the `appspec.yml` file, [here](/appspec.yml).

The API endpoints are described in detail [here](https://github.com/ahmed-belhadj/conduit-node-api/tree/master/api#endpoints).

## Database
Last but not least our database will be hosted using [AWS RDS](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html), as a PostgreSQL instance.

## AWS Console
Get familiar with the AWS Console (the web interface [here](https://console.aws.amazon.com)), it's what you'll mostly use throughout the workshop.

In particular, note that there's a search bar up top. Whenever the workshop instructs you to go somewhere, start by looking it up in that search bar.

Next to the search bar there's a `Services` button, which shows a menu with all of AWS's offerings. Whenever a new service is introduced by the workshop, the instructions will reference a section under this `Services` menu. For example: `Compute/EC2`. 

From this menu you can _favourite_ services, which will make accessing them much faster. You can't favourite services from a search result. As part of your exploration, you could try favouriting the following services:
- EC2 under Compute.
- S3 under Storage.
- Systems Manager under Management & Governance.
- Code Build under Developer Tools.
- RDS under Database.
- IAM under Security, Indentity & Compliance.

## Repository
You will probably have to make some changes in the code, so you should create a new branch you can push for your modifications.

## Getting logs from EC2 instances
We will configure EC2 instances with a security policy that allows `ssh` access to the instances. You can view logs by `ssh`ing to the instance or by using `scp`.

You can view logs of _all_ deployments in the instance's `/opt/codedeploy-agent/deployment-root/deployment-logs/codedeploy-agent-deployments.log`.

You can also view logs of a specific deployment in the instance's `/opt/codedeploy-agent/deployment-root/<deployment-group-ID>/<deployment-ID>/logs/scripts.log`. You will learn how to find these parameters later.

More on logging [here](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-view-logs.html#deployments-view-logs-instance-unix).

## Summary
To sum up, in this section we will create:

- an S3 bucket to host our static frontend.
- a CodeBuild setup to build the frontend and copy the output to the S3 bucket.
- a CodeDeploy setup to deploy our API to the EC2 instances.
- an RDS PostgreSQL instance.

> **Important:** after you are done with this workshop, you will ideally clean up your account, so you are not billed anymore. This means that you need to delete everything you have created.
>
> Many resources in AWS [can be tagged](https://aws.amazon.com/answers/account-management/aws-tagging-strategies/). If something can be tagged, then you should tag it with a **unique name**. Later, you can use the [Tag Editor](https://aws.amazon.com/blogs/aws/resource-groups-and-tagging/) to find your tagged resources to delete, and make sure you don't leave anything behind.
>
> A good tag/value pair to use is `<your_name>-workshop`/`True`. Whatever you chose, be consistent so that it's easy to clean up your account.


---

**Next:** learn how to [serve a static website from S3](/workshop/s3-web-ec2-api-rds/01-serve-website-from-s3.md).
