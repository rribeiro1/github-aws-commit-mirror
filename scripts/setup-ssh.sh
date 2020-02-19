# Remove default config for ssh
rm -Rf /home/circleci/.ssh/config

# Create ssh config for AWS Code Commit 
echo "Host !github.com *
User APKAYMLLNMYWO5TS2QMO
IdentityFile /home/circleci/.ssh/id_rsa_ffeb190510d862a23307b06f1dd70fcf" >> /home/circleci/.ssh/config

# Add server as Known Host
ssh-keyscan -H git-codecommit.eu-central-1.amazonaws.com >> ~/.ssh/known_hosts