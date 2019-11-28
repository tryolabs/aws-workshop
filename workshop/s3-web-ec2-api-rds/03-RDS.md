# RDS

## Create a PostgreSQL instance in RDS
1. Go to **RDS** under **Database** section.
2. Click on **Create Database**.
3. Click on PostgreSQL logo, and under **Templates** section tick the _"Free Tier"_ checkbox.
4. Enter a name on _DB Instance identifier_ (we will need it later, so don’t forget it).
5. Enter a username and password and click Next (again, we will need these later).
6. Under **Connectivity** section verify that **Publicly Accessible** is set to No.
7. On **VPC security groups** choose _Select existing VPC security groups_ and select the security group you created when [launching the EC2 instance](/workshop/s3-web-ec2-api-rds/02-EC2-instances.md#launch-your-first-ec2-instance).
8. Pick a db name under **Additional Configuration** and click create Database (again, we will need the database name later).

Now our instance is created. We configured its access, allowing every instance under the security group that was created in the previous section to connect.

## Add DB parameters on Parameters Store

As before, we will need some variables stored in the parameter store, including the database name, username, password and endpoint. These variables are referenced in [this file](/backend/conduit/settings/ec2.py), so Django can access the database.

1. Go to **RDS** under **Database** section.
2. Click on Instances.
3. Wait for instance to create. Then see details of your db and copy the **Endpoint**. This will be the value for `DATABASE_HOST`.
4. Go to AWS console **Systems Manager** under **Management & Governance**.
5. On the left menu select **Parameter Store**.
6. Click Create Parameter.
7. Enter  `/prod/api/DATABASE_NAME` as the name and a meaningful description like "Name of the PostgreSQL database".
8. Enter the DB name you selected before on the value attribute.
9. Click create parameter and close.
10. Now we will need to do the same thing for the username and host
  1. For the username enter `/prod/api/DATABASE_USER` as the name and your database username and as the value
  2. For the host enter `/prod/api/DATABASE_HOST` as the name and the hostname you copied earlier as the value
11. For `/prod/api/DATABASE_PASSWORD` do the same steps but select as **Type: Secure String** and as KMS Key ID the key `workshopkey`.

Now we have our database parameters set, and the password encrypted. Only our EC2 instances will be able to decrypt it.

---
**Extra mile:**

- Can you `ping` the Postgres instance?
- Try to connect to the DB through your running EC2 instance.

---

**Next:** create a [CodeDeploy project to deploy your API](/workshop/s3-web-ec2-api-rds/04-code-deploy.md).
