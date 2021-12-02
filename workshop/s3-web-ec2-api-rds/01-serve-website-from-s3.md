# Serve a static website from S3

## Creating the bucket

First we need to create a bucket from where we are going to serve the website.

1. On your AWS Console, go to **S3** under **Storage section**.
2. Click on Create bucket.
3. Enter the name of the bucket.

    Remember, bucket names must be unique across all existing accounts and regions in AWS. You cannot rename a bucket after it is created, so chose the name wisely. Amazon suggests using DNS-compliant bucket names. You should read more about this [here](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html#bucketnamingrules).

    A good bucket name is `<your_name>-workshop`.

4. Pick a region for the S3 bucket.

    You can chose any region you like, but beware that Amazon has [different pricing](https://aws.amazon.com/s3/pricing/) for storage in different regions. In this case (though it won't matter too much) we will pick `US East (N. Virginia)`.
5. Click Create. We will configure the properties later.

## Enable static website hosting
Once created, enable static website hosting for this bucket by
1. Clicking on the name of your bucket.
2. Going to Properties.
3. Scrolling down to **Static website hosting**.
4. Clicking the _Edit_ button.
5. Checking the **Enable** option under **Static website hosting**.
6. Checking the **Host static website** option under **Hosting Type**.
6. Putting `index.html` as index and error documents. 
7. Clicking Save.

Note the URL under **Bucket website endpoint** in the **Static website hosting** section. Later, we will go to the **endpoint url** specified to access our website.

## Enable and configure public access
Enable public access by going to the **Permissions** tab (you might need to scroll back up from where you are) and:
1. Click **Edit** on the **Block public access** section.
2. Uncheck **Block all public access**.
3. Save and confirm.

Now, still in the **Permissions** tab, make every object readable by
1. Clicking **Edit** on the **Bucket Policy** section.
2. Adding the following policy to make every object readable:
    ```
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
    ```
3. Saving.


## Add `WEBSITE_BUCKET_NAME` to the Parameters Store

Every application needs to have some configurations that inherently will vary between different deployments: whether to enable debug or not, the address of the database server, secret keys or access tokens for third party services, etc. Some of these need to be stored securely (ie. keys API tokens). Many people use [environment variables](https://en.wikipedia.org/wiki/Environment_variable) for this, but it is not secure enough.

[AWS Parameters Store](http://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-paramstore.html) is a service designed for just this, and we will use it to store variables of our system. This will enable us to store constants and later use them during other steps of the deployment. We will start by storing the bucket name.

1. Get your bucket's name (the one you created before).

    If you don't remember it, you can find all your buckets if you go to **S3** under **Storage** **section**.
3. In the search bar  up top, search for **Systems Manager** (it's under **Management & Governance**).
4. On the left menu select **Parameter Store**.
5. Click **Create Parameter**.
6. Enter `/prod/codebuild/WEBSITE_BUCKET_NAME` as name and a meaningful description of what the parameter means (ie. "name of the website bucket").
7. Enter `s3://<your-bucket-name>` as value.
8. Click create parameter.

Now we can retrieve the bucket name with `aws ssm get-parameter` like we did [here](/buildspec.frontend.yml). Also, we can use [AWS SSM Agent](http://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) to manage our instances' configuration from the AWS web console.


## Create a policy to get full access to the S3 website bucket

With [AWS Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html), you can specify different permissions regarding every AWS resource you use. For example, you can create a policy for enabling full access to a specific S3 bucket, and that is what we are going to do. We will need this in the future to build the project programmatically and store it on S3.

1. Go to **IAM** under **Security, Identity & Compliance**.
2. Click in Policies.
3. Click in Create Policy.
4. Click **Import managed policy**.
5. Search and select `AmazonS3FullAccess` (this is a premade policy, but you can also build your own).
6. Click the **JSON** tab and change the `Resource` value to `["arn:aws:s3:::<your-bucket-name>", "arn:aws:s3:::<your-bucket-name>/*"]` in the JSON content.
7. Click **Review policy**
8. Choose a name for the policy (eg. S3WebsiteFullAccess) and click in Create Policy.

Now we have a policy that allows full access (list, write, update, delete, etc) to our website bucket. Let’s see how we can use it in the following section.

Don't fret, only a particular _role_ will have this policy attached to it. It's not like _everyone_ will have full access to your S3 bucket (that would be dangerous). More on this later.


## Create a project in CodeBuild to build and deploy the frontend

As we mentioned earlier, [AWS CodeBuild](https://aws.amazon.com/codebuild/) is an AWS service to build projects. In order to instruct CodeBuild on what to do, we have created the `buildspec.frontend.yml`. CodeBuild will first pull the repository, and then run the commands specified on [that file](/buildspec.frontend.yml). If you see, we have specified what is needed for a fresh install of the project, which ends up in a build using `npm build` and `aws s3 sync` for uploading the resulting files to S3.

Follow these steps to get it ready:

1. Go to **CodeBuild** under the **Developer Tools** section.
2. Click on Get Started (or Create Project if you had other projects).
3. Choose a project name and write a description (optional).
4. On the Source section:
    1. Choose **Github** as the source provider.
    2. Select an option for the repository (probably _Public repository_).
    3. Connect Github with AWS if neccesary.
    4. Fill the repository URL or choose one repository from your Github account.
    5. Write your branch's name under **Source version**.
5. On the Environment section:
    1. Choose Ubuntu as the OS and Standard as the Runtime.
    2. Select  `aws/codebuild/standard:5.0` as the Image and latest Image Version.
6. In the Service Role section:
    1. Select New service role.
    1. Choose a name for the Role and name it `aws-workshop-service-rcodebuild-ole`.
7. In the BuildSpec section:
    1. Choose `Use a Buildspec file`.
    2. Set to name to `buildspec.frontend.yml` (our yaml file with the steps to follow).
8. In the Artifacts section select _No artifacts_.
9. Click on Create Build Project.
10. Click on Save.

Now, we have created a CodeBuild application. We won’t be able to run it though, because we don’t have permissions to add files to our S3 bucket. That is why earlier we created a policy and also something called a "role". For everything to work, we need to attach the policy to the role.

## Attach policies to the CodeBuild role

A [Role](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) defines permissions inside AWS. Those permissions come in the form of policies, just like in the case of your AWS user. Things like certain EC2 services (and even instances) which need to execute some actions can run attached to a certain role, and will thus get whatever permissions the role has.

Earlier, we created a policy to allow full access to our S3 bucket and assigned a new role to our CodeBuild application. Now we will attach the policy to the role, effectively giving CodeBuild access to our S3 bucket. Moreover, we will need to attach another policy to give it access to SSM, so that it can query the values of the variables we setup in the Parameter Store.

**Website full access**

1. Go to IAM under Security, Identity & Compliance.
2. Click in Roles.
3. You should see the role created in the CodeBuild project creation, select it.
4. Click Attach Policies.
5. Search for the Policy for full access to the S3 website bucket (`S3WebsiteFullAccess`) and select it.
6. Click Attach Policy.

**SSM read access**

1. Click Attach Policy again.
2. Search for `AmazonSSMReadOnlyAccess` and click on Attach.

---
**Extra mile:** try get the value of `WEBSITE_BUCKET_NAME` from the command line.

---

**Next:** [EC2 instances](/workshop/s3-web-ec2-api-rds/02-EC2-instances.md).
