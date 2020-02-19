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


for repo in github_client.get_user().get_repos():
    if repo.archived:
        print('Skipping repository {}, it is archived on github'.format(repo.name))
    else:
        if repo.name in ['bible-vue']:
            print('Cloning repository {} to local storage'.format(repo.name))
            clone_repo(repo.name)

            # Check if repo exists on AWS
            if is_repo_exists_on_aws(repo.name):
                os.system('ls -ltra')
                os.system('cd {}'.format(repo.name))
                os.system('git remote add sync ssh://AKIAYMLLNMYWP6P7RUB3@git-codecommit.eu-central-1.amazonaws.com/v1/repos/{}'.format(repo.name))
                os.system('git push sync --mirror')
                os.system('cd ..')
            else:
                print("create and mirror")

            print('Deleting repository {} from local storage'.format(repo.name))
            delete_repo_local(repo.name)
