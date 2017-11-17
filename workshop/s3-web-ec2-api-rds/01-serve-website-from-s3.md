# Serve a static website from S3

## Creating the bucket

First we need to create a bucket from where we are going to serve the website.

1. On your AWS Console, go to **S3** under **Storage section** and click on Create bucket
2. Enter the name of the bucket and click next. Remember, bucket names must be unique across all existing regions in AWS.
3. Click Create. We will configure the properties later.
4. Once created, click on the name of your bucket
5. Go to properties, click **Static website hosting** check the option **Use this bucket to host a website**
6. As index and error document put: `index.html`
7. Later, we will go to the **endpoint url** specified at the top to access our website
8. Click Save
9. Go to **Permissions**, **Bucket Policy,** and add the following policy to make every object readable:
      {
          "Version": "2012-10-17",
          "Statement": [
              {
                  "Sid": "AddPerm",
                  "Effect": "Allow",
                  "Principal": "*",
                  "Action": "s3:GetObject",
                  "Resource": "arn:aws:s3:::<your-bucket-name>/*"
              }
          ]
      }
10. Click Save


## Add WEBSITE_BUCKET_NAME to the Parameters Store

From now on we will use [AWS Parameters Store](http://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-paramstore.html) to keep variables of our system. This will enable us to store constants and later use them during other steps of the deployment. This time we will store the bucket name


1. Go to **S3** under **Storage** **section**
2. See details of the bucket you just created and copy its name
3. Go to **EC2** under **Compute section**
4. On the left menu select **Parameter Store**
5. Click Get started now
6. Enter  `/prod/codebuild/WEBSITE_BUCKET_NAME` as name and `name of the website bucket` as description
7. Enter  `s3://<``your-``bucket-name>` as value
8. Click create parameter

Now if we want to get the bucket name programmatically we can use [AWS SSM Agent](http://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html). We will come back at it later.


## Create a policy to get full access to the S3 website bucket

With [AWS Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)  you can specify different actions regarding every AWS resource you use. For example, you an create a policy for enabling full access a specific S3 bucket, and that is what we are going to do. We will need this in the future to build the project programmatically and store it on S3.


1. Go to **IAM** under **Security, Identity & Compliance**
2. Click in Policies.
3. Click in Create Policy.
4. Select Copy an AWS Managed Policy**.**
5. Search and select AmazonS3FullAccess (this is a premade policy to allow full access to every S3 bucket)
6. Choose a name for the policy (eg. S3WebsiteFullAccess)
7. Change the `Resource` value to `["arn:aws:s3:::<``your``-bucket-name>", "arn:aws:s3:::<``your``-bucket-name>/*"]`
8. Click in Create Policy

Now we have a policy that allows full access (write, update, delete, etc) to our website bucket. 
Let’s see how we can use it in the following section.


## Create a project in CodeBuild to build and deploy the frontend

As we mentioned earlier, [AWS CodeBuild](https://aws.amazon.com/codebuild/) is a fast service to build projects. Take a look at `buildspec.frontend.yml`. In there we specify what we want CodeBuild to do. CodeBuild first pulls our repoFirst and then runs our commands, wich are building the project using `npm` and uploading it to S3.

Follow these steps to get it ready.

1. Go to **CodeBuild** under the **Developer Tools** section
2. Click on Get Started (or Create Project if you had other projects)
3. Choose a project name and write an description (optional)
4. On the Source section:
  1. Choose **Github** as the source provider
  2. Select an option for the repository
  3. Connect Github with AWS if neccesary
  4. Fill the repository URL or choose one repository from your Github account
5. On the Environment section:
  1. Choose Ubuntu as the OS and Node.js as the Runtime
  2. Select  `aws/codebuild/nodejs:7.0.0` as the Version.
  3. Change the BuildSpec name to `buildspec.frontend.yml`. Our yaml file with the steps to follow
6. In the Artifacts section select No artifacts
7. In the Service Role section:
  1. Select Create a service role in your account
  2. Choose a name for the Role and name it `codebuild-aws-workshop-service-role`
8. Click on Continue
9. Click on Save

Now we have created a CodeBuild application. We won’t be able to run it though, because we don’t have permissions to add files to our S3 bucket. That is why we created the policy and the CodeBuild role. Let’s attach the policy to the role next

## Attach policies to the CodeBuild role created

A [Role](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) defines permissions inside AWS. Those permissions come in the form of policies.
Earlier we created a policy to allow access to our S3 bucket and a role assigned to our CodeBuild application. Now we will attach that policy to the role, giving CodeBuild access to our S3 bucket. We will need to attach another policy to give it access to SSM, that way we can ask for the variables we set in the Parameter Store.
**Website full access**

1. Go to IAM under Security, Identity & Compliance
2. Click in Roles
3. You should see the role created in the CodeBuild project creation, select it.
4. Click Attach Policy
5. Search for the Policy for full access to the S3 website bucket, select it and then click Attach Policy.

**SSM read access**

1. Click Attach Policy again
2. Search for `AmazonSSMReadOnlyAccess` and click on Attach

---

Next: [EC2 instances](/workshop/s3-web-ec2-api-rds/02-EC2-instances.md)