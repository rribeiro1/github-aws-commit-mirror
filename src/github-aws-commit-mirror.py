import os
import boto3
from github import Github

print("Done Importing")

# AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
# GITHUB_API_TOKEN = os.getenv('GH_API_TOKEN')
# AWS_SSH_KEY_ID = os.getenv('AWS_SSH_KEY_ID')

# github_client = Github(GITHUB_API_TOKEN)

# codecommit_client = boto3.client('codecommit', region_name='us-east-1',
#                                 aws_access_key_id=AWS_ACCESS_KEY_ID,
#                                 aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'


# def clone_repo(repo_name):
#     print(f"{bcolors.OKGREEN}--> Cloning repository {repo_name} to local storage {bcolors.ENDC}")
#     # string = ('git clone --mirror https://github.com/PedigreeTechnologies/{}.git {}'.format(repo_name, repo_name))
#     # print(string)
#     os.system('git clone --mirror https://github.com/PedigreeTechnologies/{}.git {}'.format(repo_name, repo_name))
#     print("Clone Finished")


# def delete_repo_local(repo_name):
#     print(f"{bcolors.OKGREEN}--> Deleting repository {repo_name} from local storage {bcolors.ENDC}")
#     os.system('rm -Rf {}'.format(repo_name))


# def is_repo_exists_on_aws(repo_name):
#     try:
#         codecommit_client.get_repository(repositoryName=repo_name)
#         return True
#     except Exception:
#         return False


# def create_repo_code_commit(repo_name):
#     print(f"{bcolors.OKBLUE}--> Creating repository {repo_name} on AWS CodeCommit {bcolors.ENDC}")
#     codecommit_client.create_repository(
#         repositoryName=repo_name,
#         repositoryDescription='Backup repository for {}'.format(repo_name),
#         tags={
#             'name': repo_name
#         }
#     )


# def sync_code_commit_repo(repo_name):
#     print(f"{bcolors.OKGREEN}--> Pushing changes from repository {repo_name} to AWS CodeCommit {bcolors.ENDC}")
#     os.system('cd {} && git remote add sync ssh://{}@git-codecommit.us-east-1.amazonaws.com/v1/repos/{}'.format(repo_name, AWS_SSH_KEY_ID, repo_name))
#     os.system('cd {} && git push sync --mirror'.format(repo.name))
#     print("Done Syncing")

# # repo_list = github_client.get_user().get_repos()
# # print("Number of repositories: " + str(repo_list.totalCount))

# for repo in github_client.get_user().get_repos():
#     if repo.archived:
#         print(f"{bcolors.WARNING}> Skipping repository {repo.name}, it is archived on github {bcolors.ENDC}")
#     else:
#         print(f"{bcolors.HEADER}> Processing repository: {repo.name} {bcolors.ENDC}")
#         clone_repo(repo.name)

#         if is_repo_exists_on_aws(repo.name):
#             sync_code_commit_repo(repo.name)
#         else:
#             create_repo_code_commit(repo.name)
#             sync_code_commit_repo(repo.name)

#         delete_repo_local(repo.name)
