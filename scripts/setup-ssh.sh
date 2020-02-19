# Clean default SSH config
rm -Rf /home/circleci/.ssh/config

# Add CodeCommit to SSH Configuration
echo "Host !github.com *
User APKAYMLLNMYWO5TS2QMO
IdentityFile /home/circleci/.ssh/id_rsa_ffeb190510d862a23307b06f1dd70fcf" >> /home/circleci/.ssh/config

# Add CodeCommit Server as Known Host
ssh-keyscan -H git-codecommit.eu-central-1.amazonaws.com >> ~/.ssh/known_hosts