# Clean default SSH config
ls -ltra ~/.ssh

cat /home/circleci/.ssh/id_rsa_ffeb190510d862a23307b06f1dd70fcf

#rm -Rf /home/circleci/.ssh/config

# Add CodeCommit to SSH Configuration
# see https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-without-cli.html#setting-up-without-cli-configure-client
 echo "Host git-codecommit.*.amazonaws.com
 User $1
 IdentityFile /home/circleci/.ssh/id_rsa" >> /home/circleci/.ssh/config

ls -ltra ~/.ssh

# echo "After changes"
# cat /home/circleci/.ssh/config

# Add CodeCommit Server as Known Host
ssh-keyscan -H git-codecommit.$2.amazonaws.com >> ~/.ssh/known_hosts