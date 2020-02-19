from github import Github
import boto3
import os

GITHUB_API_TOKEN = os.getenv('GITHUB_API_TOKEN')

github_client = Github(GITHUB_API_TOKEN)
codecommit_client = boto3.client('codecommit')


def clone_repo(repo_name):
    print('-----------------------------------------------------------')
    print('Cloning repository {} to local storage'.format(repo_name))
    print('-----------------------------------------------------------')
    os.system('git clone --mirror https://github.com/rribeiro1/{}.git {}'.format(repo_name, repo_name))


def delete_repo_local(repo_name):
    print('-----------------------------------------------------------')
    print('Deleting repository {} from local storage'.format(repo_name))
    print('-----------------------------------------------------------')
    os.system('rm -Rf {}'.format(repo_name))


def is_repo_exists_on_aws(repo_name):
    try:
        codecommit_client.get_repository(repositoryName=repo_name)
        return True
    except Exception:
        return False


def create_repo_code_commit(repo_name):
    print('-----------------------------------------------------------')
    print('Creating repository {} on AWS CodeCommit'.format(repo_name))
    print('-----------------------------------------------------------')
    codecommit_client.create_repository(
        repositoryName=repo_name,
        repositoryDescription='Backup repository for {}'.format(repo_name),
        tags={
            'name': repo_name
        }
    )


def sync_code_commit_repo(repo_name):
    print('-----------------------------------------------------------------')
    print('Pushing changes from repository {} to AWS CodeCommit'.format(repo_name))
    print('-----------------------------------------------------------------')
    os.system('cd {} && git remote add sync ssh://git-codecommit.eu-central-1.amazonaws.com/v1/repos/{}'.format(repo_name, repo_name))
    os.system('cd {} && git push sync --mirror'.format(repo.name))


for repo in github_client.get_user().get_repos():
    if repo.archived:
        print('-----------------------------------------------------------------')
        print('Skipping repository {}, it is archived on github'.format(repo.name))
        print('-----------------------------------------------------------------')
    else:
        if repo.name in ['bible-vue', 'bible-edge', 'github-backend', 'dummy-repo', 'daily-coding-problem']:
            clone_repo(repo.name)

            if is_repo_exists_on_aws(repo.name):
                sync_code_commit_repo(repo.name)
            else:
                create_repo_code_commit(repo.name)
                sync_code_commit_repo(repo.name)

            delete_repo_local(repo.name)
