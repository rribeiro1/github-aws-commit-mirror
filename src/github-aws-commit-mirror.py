from github import Github
import os

GITHUB_API_TOKEN = os.getenv('GITHUB_API_TOKEN')

g = Github(GITHUB_API_TOKEN)


def is_archived(repo):
  repo.archived


def clone(repo_name):
  os.system('git clone https://github.com/rribeiro1/{}.git'.format(repo_name))


for repo in g.get_user().get_repos():
  if is_archived(repo):
    print('Skipping repository {}, it is archived on github'.format(repo.name))
  else:
    if repo.name in ['bible-vue', 'bible-edge']:
      print('Clonning repository {} locally'.format(repo.name))
      clone(repo.name)
      