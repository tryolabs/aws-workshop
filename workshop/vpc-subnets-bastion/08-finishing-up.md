# Finishing up

Last steps are modifing our CodeDeploy project so it use our new Auto Scaling group, re-run the deploy and rebuild the web so it takes the new parameters.

## Modify the CodeDeploy project
1. Go to CodeDeploy under Developer Tools
2. click your application name
3. select your deployment group and on Actions select Edit
4. On Environment configuration select your Auto Scaling Group on Auto Scaling groups tag
5. Go to Amazon EC2 instances tag and delete all tag groups
6. check the Enable load balancing
7. on Load balancer select your target group on the drop down
8. click Save
9. select your deployment group and on Actions click Deploy new version
10. on Repository type select : My application is stored in github
11. Repository Name: tryolabs/aws-workshop
12. select last commit id
13. then click Deploy


## Re-run CodeBuild
1. Go to CodeBuild under Developer Tools
2. click Start build
3. click Start build


---