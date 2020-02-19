# Clean default SSH config
ls -ltra ~/.ssh

#rm -Rf /home/circleci/.ssh/config

# Add CodeCommit to SSH Configuration
# see https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-without-cli.html#setting-up-without-cli-configure-client
echo "Host !github.com *
User APKAYMLLNMYWO5TS2QMO
IdentityFile /home/circleci/.ssh/id_rsa_ffeb190510d862a23307b06f1dd70fcf" >> /home/circleci/.ssh/config

echo "After changes"
cat /home/circleci/.ssh/config

# Add CodeCommit Server as Known Host
ssh-keyscan -H git-codecommit.$1.amazonaws.com >> ~/.ssh/known_hosts