rm -Rf /home/circleci/.ssh/config

echo "Host !github.com *
User APKAYMLLNMYWO5TS2QMO
IdentityFile /home/circleci/.ssh/id_rsa_ffeb190510d862a23307b06f1dd70fcf" >> /home/circleci/.ssh/config

echo "Known hosts"
cat /home/circleci/.ssh/known_hosts

ssh-keyscan -H git-codecommit.us-east-2.amazonaws.com >> ~/.ssh/known_hosts

ssh -v APKAYMLLNMYWO5TS2QMO@git-codecommit.us-east-2.amazonaws.com