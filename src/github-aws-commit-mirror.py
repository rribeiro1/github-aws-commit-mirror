from github import Github
import boto3
import os

GITHUB_API_TOKEN = os.getenv('GITHUB_API_TOKEN')

github_client = Github(GITHUB_API_TOKEN)
codecommit_client = boto3.client('codecommit')


def clone_repo(repo_name):
    os.system('git clone --mirror https://github.com/rribeiro1/{}.git {}'.format(repo_name, repo_name))


def delete_repo_local(repo_name):
    os.system('rm -Rf {}'.format(repo_name))


def is_repo_exists_on_aws(repo_name):
    try:
        codecommit_client.get_repository(repositoryName=repo_name)
        return True
    except Exception:
        return False


def create_repo_code_commit(repo_name):
    codecommit_client.create_repository(
        repositoryName=repo_name,
        repositoryDescription='Backup repository for {}'.format(repo_name),
        tags={
            'name': repo_name
        }
    )


def push_repository_code_commit(repo_name):
    os.system('cd {} && git remote add sync ssh://git-codecommit.eu-central-1.amazonaws.com/v1/repos/{}'.format(repo_name, repo_name))
    os.system('cd {} && git push sync --mirror'.format(repo.name))


for repo in github_client.get_user().get_repos():
    if repo.archived:
        print('Skipping repository {}, it is archived on github'.format(repo.name))
    else:
        if repo.name in ['bible-vue', 'bible-edge']:
            print('Cloning repository {} to local storage'.format(repo.name))
            clone_repo(repo.name)

            # Check if repo exists on AWS
            if is_repo_exists_on_aws(repo.name):
                push_repository_code_commit(repo.name)
            else:
                create_repo_code_commit(repo.name)
                push_repository_code_commit(repo.name)

            print('Deleting repository {} from local storage'.format(repo.name))
            delete_repo_local(repo.name)
