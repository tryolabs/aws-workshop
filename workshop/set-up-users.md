# Set up users on AWS

> **TryoTip:** if you are using the **Tryolabs Playground AWS account**, this section does not apply. Please, read it anyway, so you have some context on what you would do with a bare new AWS account.

As you might already now there is a special account in AWS called _root_. This is the account used to do the initial setup for users, roles and billing information. Is recommended to create a user with administrator priviledges for the every day use and [not use the root account](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#create-iam-users) to login to AWS. Additionally, you should make sure you enable [Multi Factor Authentication (MFA)](http://docs.aws.amazon.com/console/iam/security-status-activate-mfa) on your root account, and use an app like [Authy](https://authy.com/) as a second factor on your phone (Android/iOS).

Next, we are going to use our root account to setup 2 AWS users.

One will be used to access AWS via the console (web interface, so this will be your own user). The other will be used for accessing our account *programmatically*: we will create an **access key ID** and **secret access key** for the AWS API, CLI, SDK, and other development tools.

Every account has some associated permissions. It is a good practice to have those strictly limited to the bare minimum necessary, especially for programmatic access. Permissions are handled by attaching [policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) to the user accounts. There, you can customize the access levels to various AWS services.

First we are going to create the user for the AWS console:

1. Login to your AWS account with the root user.
2. Go to **IAM** under Security, Identity & Compliance section.
3. Click on Users.
4. Click Add user button.
5. Enter a username and check the option: **AWS Management Console access** under the **Select AWS access type** section and then click next. You should also mark the option so that the user is forced to change his password on next login (pick a secure password!).
6. Select **Attach existing policies directly**.
7. Search for: `AdministratorAccess`, check it and click next.
8. Click on Create user. Copy the url and password that appear in the Success message.

Now, lets login with our new user:

1. Log out from AWS and go to the link you copied earlier.
2. Enter the username and password that was auto-generated.
3. Enter your new password.

After this, we can create the user to access AWS programmatically:

1. Repeat steps from 2 to 4 to setup a user.
2. Enter a username and check the option **Programmatic access** under the **Select AWS access type** section. Click next.
3. Select **Attach existing policies directly**.
4. Search for: `AdministratorAccess`, check it and click next. Of course, in a real use case, you would design or use a policy with more restricted access.
5. Click on Download CSV.

In the downloaded file, you can find the access key id and the secret access key. You’ll need them to [configure your AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in your computer. If you don’t have AWS CLI installed yet, you can do it following [these steps](http://docs.aws.amazon.com/cli/latest/userguide/installing.html).

---
**Extra mile**: set the `ViewOnlyAccess` permissions to the user with programmatic access. Double points if you do it with the CLI.

---

**Next:** [S3, RDS and EC2](/workshop/s3-web-ec2-api-rds/introduction.md).
