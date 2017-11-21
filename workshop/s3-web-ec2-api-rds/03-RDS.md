# RDS

## Create Postgres in RDS
1. Go to **RDS** under **DataBase** section
2. Click on Get Started Now
3. Click on PostgreSQL logo and then click select
4. Check the option of Dev/Test section and click Next Step
5. on **DB Instance class** select : db.t2.micro
6. on **Multi-AZ Deployment** select: no
7. Enter a name on DB Instance identifier (we will need it later so don’t forget it)
8. Enter a username and password and click Next (again, we will need them later)
9. Select No on **Publicly Accessible**
10. Availability Zone :  us-east-1a
11. Pick a db name and click Launch Instance (again, we will need them later)
12. Click View Your DB Instances

Now our instance is created. We will configure its access, allowing every instance under the security group that was created in the previous section.

1. Click on the name of the **Security Groups** under **Configuration Details** of your RDS instance
2. Go to Inbound and click edit
3. On source you have to put the group-id that you copy on last step of [Create EC2 instance](/workshop/s3-web-ec2-api-rds/02-EC2-instances.md)

Now only our instance will have access to our database.

## Add DB parameters on Parameters Store

As before, we will need some variables stored in the parameter store, including the database name, username, password and endpoint. this variables are used on the [/backend/conduit/settings/ec2.py](/backend/conduit/settings/ec2.py) so django can access the db.

1. Go to **RDS** under **DataBase** section
2. Click on Instances
3. See details of your db and copy the url of the **Endpoint** (until the : ) this is the `DATABASE_HOST`
4. Go to **EC2** under **Compute** section
5. On the left menu select Parameter Store
6. Click Create Parameter
7. Enter  `/prod/api/DATABASE_NAME` as the name and `name of the postgres database` as description
8. Enter the db name, the db name that was picked on step 10 of the previous section on the value attribute
9. Click create parameter and close
10. Now we will need to do the same thing for the username and host
  1. For the username enter `/prod/api/DATABASE_USER` as the name and your database username  and as the value
  2. For the host enter `/prod/api/DATABASE_HOST` as the name and the hostname you copied earlier as the value
11. For `/prod/api/DATABASE_PASSWORD` do the same steps but select as **Type: Secure String** and as KMS Key ID the key : `workshopkey`

Now we have our database parameters set, and the password encrypted. Only our EC2 instances will be able to decrypt it.

---

Next: [Create a CodeDeploy project to deploy your API](/workshop/s3-web-ec2-api-rds/04-code-deploy.md)
