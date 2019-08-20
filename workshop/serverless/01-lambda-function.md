# Install and configure Serverless


**What is Serverless?** \
Who could be better explaining this than Serverless:\
*"Just like wireless internet has wires somewhere, serverless architectures still have servers somewhere. What ‘serverless’ really means is that, as a developer you don’t have to think about those servers. You just focus on code.
This was initially embodied in function-as-a-service infrastructure, like AWS Lambda, that had Serverless properties like: function as the unit of deployment, 100% auto-scaling, and pay-per-execution pricing models. More recently many other types of ‘serverless infrastructure’ have emerged such as zero configuration databases, APIs for handling user management, and highly abstracted container orchestration engines. At the end of the day, Serverless is any developer tooling which the developer does not need to worry at all about the underlying infrastructure."* \
You can read mor about this [here](https://serverless.com).

[ciemsa@pciaux01desav ~]$ serverless

Serverless: No project detected. Do you want to create a new one? Yes
Serverless: What do you want to make? AWS Node.js
Serverless: What do you want to call this project? test

Project successfully created in 'test' folder.

No AWS credentials were found on your computer, you need these to host your application.

Serverless: Do you want to set them up now? Yes
Serverless: Do you have an AWS account? Yes
Serverless: Press Enter to continue after creating an AWS user with access keys 
Serverless: AWS Access Key Id: AKIAV3C2NQ4XIHIOOKOH
Serverless: AWS Secret Access Key: jun/EL1/AFe+vIQSQV/8FhWvAsE8awE6EQcnP6iq

AWS credentials saved on your machine at ~/.aws/credentials. Go there to change them at any time.

You can monitor, troubleshoot, and test your new service with a free Serverless account.

Serverless: Would you like to enable this? No
You can run the “serverless” command again if you change your mind later.

## Install Serverless
During the installation process you will be asked for your `AWS Access Key Id` and `AWS Secret Access Key` you got when you created the programatic user. Take it at hand.

1. Follow the insstallation isntructions only [here](https://serverless.com/framework/docs/providers/aws/guide/quick-start/)
2. If you didn't clone this repo yet, do it. If you alredy done go to `./infraestructure/aws/lambda` and take a look at the serverless yaml file [here](/infrastructure/aws/lambda/serverless.yml).
There you could see the definition of your serverless service. Under the `functions` section you have the lambda function handler, this is the entry execution point of your microservice. It also defines an HTTP method and path to trigger the lambda function.
At the top of the file there are some general parameters and there is two IAM policies to allow access to parameters and encription keys needed by the lambda function to configure the database access.
3. Take a look to the lambda function source [ambda_function.py](/infrastructure/aws/lambda/lambda_function.py). Check or update your paremeters name if it is necessary.

Now you are ready to deploy your serverless. Let's go!

1. Under the directory `./infrastructure/aws/lambda/` \
run: \
`serverless deploy -v`
This will start to make a detailed set of instructions and will automatically create all that you need to hava a working lambda function in your AWS account. At the end, if all works well, you will have the URL to access to your serveice.
2. Now you could test your endpoint sending a GET request to you API endpoint passing some string to the `query` request parameter and wait for a response with all the articles who has this string in their title.
3. In the AWS console, go to **Lambda** under **Computing**
4. Go to **Functions** at the left.
5. Look for you brand new lambda function (serverless-aws-workshop-dev-lambda_handler) and click on it.
6. In the **Designer** section you will have a diagram with your lambda function and at the left the triggers (in this case API Gateway) and at the right the AWS services the function need access to.
Clicking on wichever of this you will have more details below. Take some time exploring this.
7. Finally you could test your lambda function from the console with the butoon `test` at the top right.

Maybe you haven't access to your RDS because previously in the workshop you created a VPC where you put the DB. Your lambda function are outside the VPC and your DB haven't public access (from outside of your VPC). One solution could be having your lambda inside your VPC but this has some drawbacks related to the long warming time required by the lambda function to be ready to run on each call. For this workshop we will put our RDS in the default VPC and subnets accessible from outside and then will give public access to de DB. Be careful and don't do that in a production environment! There is other ways to workaround this.

### Give public access to your RDS.

1. Go to **RDS** under **Database** and then to **Databases** on the left.
2. Select your database and click on **Modify**.
3. Under **Network and Settings** select `default` Subnet group.
4. Select a security group with allowed TCP traffic from 0.0.0.0/0 to TCP Port 5432. If you havent this security group created you can create one in `VPC security groups` under **EC2** section addint a Inbound rule with type `PostgresSQL`.
5. Then select `Yes` on Public accessibility.
6. Click on **Continue**
7. Select `Apply Immediately` and click **Modify DB Instance**

At this point you could make GET request to your new serverless API endpoint using the URL associated during the deployment and configured in AWS API Gateway. 

---
**Next:** [Connect your load balancer to your lambda](/workshop/serverless/02-api-integration.md).
