"""
Script to mirror git repos
to aws codecommit
"""
import os
import boto3  # pylint: disable=import-error
from github import Github  # pylint: disable=import-error
from github import GithubException  # pylint: disable=import-error

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
GITHUB_API_TOKEN = os.getenv("GH_API_TOKEN")
AWS_SSH_KEY_ID = os.getenv("AWS_SSH_KEY_ID")

github_client = Github(GITHUB_API_TOKEN)

codecommit_client = boto3.client(
    "codecommit",
    region_name="us-east-1",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


class BColors:
    """Define print colors"""
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def clone_repo(repo_name):
    """Clone the repository"""
    print(
        f"{BColors.OKGREEN}--> Cloning repository {repo_name} to local storage {BColors.ENDC}",
        flush=True,
    )
    os.system(
        "git clone --mirror https://github.com/PedigreeTechnologies/{repo_name}.git {repo_name}"
    )


def delete_repo_local(repo_name):
    """Delete local repository"""
    print(
        f"{BColors.OKGREEN}--> Deleting repository {repo_name} from local storage {BColors.ENDC}",
        flush=True,
    )
    os.system("rm -Rf {repo_name}")


def is_repo_exists_on_aws(repo_name):
    """Check if repo exists on aws codecommit"""
    try:
        codecommit_client.get_repository(repositoryName=repo_name)
        return True
    except Exception: # pylint: disable=broad-except
        return False


def create_repo_code_commit(repo_name):
    """Create repo on aws codecommit"""
    print(
        f"{BColors.OKBLUE}--> Creating repository {repo_name} on AWS CodeCommit {BColors.ENDC}",
        flush=True,
    )
    codecommit_client.create_repository(
        repositoryName=repo_name,
        repositoryDescription="Backup repository for {repo_name}",
        tags={"name": repo_name},
    )


def sync_code_commit_repo(repo_name, default_branch):
    """sync comdecommit repo"""
    print(
        f"{BColors.OKGREEN}--> Pushing changes from repository \
            {repo_name} to AWS CodeCommit {BColors.ENDC}",
        flush=True,
    )
    os.system(
        "cd {repo_name} && git remote add sync \
            ssh://{AWS_SSH_KEY_ID}@git-codecommit.us-east-1.amazonaws.com/v1/repos/{repo_name}"
    )
    os.system("cd {repo_name} && git push sync --mirror")
    response = codecommit_client.get_repository(repositoryName=repo_name)
    current_branch_name = response["repositoryMetadata"]["defaultBranch"]
    if current_branch_name != default_branch:
        codecommit_client.update_default_branch(
            repositoryName=repo_name, defaultBranchName=default_branch
        )
        print("Updating Default Branch To: " + branch_name)


for repo in github_client.get_user().get_repos():
    try:
        print(
            f"{BColors.HEADER}> Processing repository: {repo.name} {BColors.ENDC}",
            flush=True,
        )
        repo.get_contents("/")
        branch_name = repo.default_branch
        clone_repo(repo.name)
    except GithubException as e:
        print(e.args[1]["message"], flush=True)  # output: This repository is empty.
        continue

    if is_repo_exists_on_aws(repo.name):
        sync_code_commit_repo(repo.name, branch_name)
    else:
        create_repo_code_commit(repo.name)
        sync_code_commit_repo(repo.name, branch_name)

    delete_repo_local(repo.name)
