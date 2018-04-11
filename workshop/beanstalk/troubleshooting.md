# Troubleshooting

These are some places where you can look for info if something doesn't work as expected.

- The deploy log is stored on each instances `/var/log/eb-activity.log` file.
- Beanstalk use Apache to run the Django app so the error logs for Apache are under `/var/log/httpd` folder.
- Your code is deployed to `/opt/python/current/` wich is a symblink to the last bundle deployed. All the past versions are in `/opt/python/bundle`.
- The virtual env for your app is in `/opt/python/run/venv`.
- Amazon Linux use `yum` to install packages. If you need some tool not installed by default, which is very likely to happen, [install it yourself](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-software.html).

If you can't login to your instances the logs can be retrieved from Beanstalk.

1. Go to **Elastic Beanstalk** under **Compute**.
2. Select your environment.
3. Click **Logs** in the left pane.
4. Click **Request Logs** and then **Full Logs**. This will zip all the `/var/log` and `/var/opt/log` content and give you a link in the **Logs** table to download it.

If nothing of this helps you, [open an issue](https://github.com/tryolabs/aws-workshop/issues/new) and we will try to help you.