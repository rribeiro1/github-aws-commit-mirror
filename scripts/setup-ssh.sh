rm -Rf ~/.ssh/config

cat ~/.ssh/id_rsa_ffeb190510d862a23307b06f1dd70fcf

echo "Host git-codecommit.*.amazonaws.com
User APKAYMLLNMYWO5TS2QMO
IdentityFile /home/circleci/.ssh/id_rsa_ffeb190510d862a23307b06f1dd70fcf" >> ~/.ssh/config