# github-aws-codecommit-mirror

[![python](https://upload.wikimedia.org/wikipedia/commons/a/a5/Blue_Python_3.8_Shield_Badge.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![AWS CodeCommit Mirror](https://github.com/PedigreeTechnologies/github-aws-commit-mirror/workflows/AWS%20CodeCommit%20Mirror/badge.svg?branch=master)

You can use this project to automate the replication of a source repository in Github to a repository in AWS CodeCommit, and it can be useful for:

- One-off task to migrate all active repositories to AWS CodeCommit
- Continuous backup process to mirror Github repos to AWS CodeCommit

It was inspired on [this AWS article](https://aws.amazon.com/pt/blogs/devops/replicating-and-automating-sync-ups-for-a-repository-with-aws-codecommit/)
however, instead of Jenkins and EC2 we are using Github Actions to create a Cronjob and executing a Python Script which fetches all repositories from an account
and for each repository, it creates the same repository in CodeCommit (if it does not exist) and mirrors the repository.

## 1. Requirements
- Github API Token
- An account on AWS and a user with right permissions to interact with AWS CodeCommit

## 2. Setup

### 2.1 Setup AWS account

1. Create a group on AWS e.g `Devops`
2. Create a user on AWS  e.g `codecommit_user` and add to the group `Devops`
3. Create a policy e.g `AwsCodeCommitMirroring` and attach this policy to the group `Devops`

This is the minimum permission required to make it work
``` json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "codecommit:TagResource",
                "codecommit:GetRepository",
                "codecommit:CreateRepository",
                "codecommit:GitPush",
                "codecommit:UpdateDefaultBranch"
            ],
            "Resource": "*"
        }
    ]
}
```

### 2.2 Setup Enviroment Variables

1. Fork this project
2. Configure the environment variables as described below:

- `AWS_ACCESS_KEY_ID` Access key from the user on AWS
- `AWS_SECRET_ACCESS_KEY` Secret access key from the user on AWS
- `AWS_SSH_KEY_ID` [AWS SSH key ID](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-without-cli.html#setting-up-without-cli-add-key) from the user on AWS
- `AWS_DEFAULT_REGION` Region on AWS where you are using CodeCommit
- `GH_API_TOKEN` [Github API Token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)

### 2.3 Setup Job scheduler

At the top of the `main.yml` file you can configure some as aspects of the job, such as the scheduler as well as the target branch to run the pipeline.

Use the `cron` parameter to configure the schedule, [Crontab Guru](https://crontab.guru/) can help on this task.

```yaml
'on':
  pull_request:
  push:
    branches:
      - master
  schedule:
    #5:30 AM Sunday
    - cron: "30 5 * * 0"
```

### 2.4 Output

```
...
> Processing repository: spring-tdd-experiments
--> Cloning repository spring-tdd-experiments to local storage
Cloning into bare repository 'spring-tdd-experiments'...
remote: Enumerating objects: 51, done.
Receiving objects: 100% (51/51), 9.90 KiB | 9.90 MiB/s, done.
Resolving deltas: 100% (4/4), done.
remote: Total 51 (delta 0), reused 0 (delta 0), pack-reused 51
--> Pushing changes from repository spring-tdd-experiments to AWS CodeCommit
Everything up-to-date
--> Deleting repository spring-tdd-experiments from local storage
...
```

### 3. References

- [Using IAM with CodeCommit: Git Credentials, SSH Keys, and AWS Access Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_ssh-keys.html)
- [Add CodeCommit to Your SSH Configuration](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-without-cli.html#setting-up-without-cli-configure-client)
- [Troubleshooting SSH Connections to AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/troubleshooting-ssh.html)
- [Using Identity-Based Policies (IAM Policies) for CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html)