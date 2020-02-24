# github-aws-codecommit-mirror

[![CircleCI](https://circleci.com/gh/rribeiro1/github-aws-commit-mirror.svg?style=svg)](https://circleci.com/gh/rribeiro1/github-aws-commit-mirror)
[![python](https://upload.wikimedia.org/wikipedia/commons/a/a5/Blue_Python_3.8_Shield_Badge.svg)]((https://www.python.org/))

You can use this project to automate the replication of a source repository in Github to a repository in AWS CodeCommit, 
it was inspired on [this AWS article](https://aws.amazon.com/pt/blogs/devops/replicating-and-automating-sync-ups-for-a-repository-with-aws-codecommit/) 
however, instead of Jenkins and EC2 I am using Circle CI to create a Cronjob and executing a Python Script which fetches active repositories from an account (discard archived ones) 
and for each repository, it creates the same repository in CodeCommit (if it does not exist) and mirror the repository.

<p align="center">
  <img src="resources/logo.png" width="450" title="Github AWS CodeCommit Mirror">
</p>

## 1. Requirements
- Github API Token
- An account on AWS and a user with right permissions to interact with AWS CodeCommit

## 2. Setup

### 2.1 Setup AWS account

1. Create a group on AWS e.g `Devops`
2. Create a user on AWS to use on CircleCI e.g `circle-ci` and add to the group `Devops`
3. Create a policy e.g `AwsCodeCommitMirroring` and attach this policy to the group `Devops`

This is the minimum permission required to make it work
``` json 
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "codecommit:TagResource",
                "codecommit:GetRepository",
                "codecommit:GitPush",
                "codecommit:CreateRepository"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

### 2.2 Setup Circle CI

You can fork this project and it on Circle CI, to make it work you must configure those environment variables on Circle CI:

- `AWS_ACCESS_KEY_ID` Access key from the user on AWS 
- `AWS_SECRET_ACCESS_KEY` Secret access key from the user on AWS
- `SSH_KEY_ID` [SSH key ID](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-without-cli.html#setting-up-without-cli-add-key) from the user on AWS
- `AWS_DEFAULT_REGION` Region on AWS where you are using CodeCommit
- `GITHUB_API_TOKEN` [Github API Token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)

### 2.3 Setup Job scheduler

In the folder `.circle` you can find the Circle CI pipeline and there you can configure some as aspects of the job, such as the scheduler as well as the target branch to run the pipeline.

Use the `cron` parameter to configure the schedule, [Crontab Guru](https://crontab.guru/) can help on this task. 

```yaml
workflows:
  version: 2
  nightly:
    jobs:
      - build
    triggers:
      - schedule:
          cron: “0 0 * * *” # Trigger every night at 00:00
          filters:
            branches:
              only:
                - master
```

### 3. References

- [Using IAM with CodeCommit: Git Credentials, SSH Keys, and AWS Access Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_ssh-keys.html)
- [Add CodeCommit to Your SSH Configuration](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-without-cli.html#setting-up-without-cli-configure-client)
- [Troubleshooting SSH Connections to AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/troubleshooting-ssh.html)
- [Using Identity-Based Policies (IAM Policies) for CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html)