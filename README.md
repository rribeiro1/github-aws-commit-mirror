# github-aws-commit-mirror

> This project shows how to mirror a Github repository into AWS CodeCommit using a schedule job on CircleCi

<p align="center">
  <img src="resources/logo.png" width="450" title="Github AWS CodeCommit Mirror">
</p>

## 1. Requirements
- Github API Token
- Account on AWS and a user with right permissions to interact with AWS CodeCommit

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

You can fork this project and it on Circle CI, in order to make it work you must configure those environment on Circle CI:

- **AWS_ACCESS_KEY_ID:** Access key from the user on AWS 
- **AWS_SECRET_ACCESS_KEY:** Secret access key from the user on AWS
- **SSH_KEY_ID:** [SSH key ID](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-without-cli.html#setting-up-without-cli-add-key) from the user on AWS
- **AWS_DEFAULT_REGION:** Region on AWS where you are using CodeCommit
- **GITHUB_API_TOKEN:** [Github API Token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)
