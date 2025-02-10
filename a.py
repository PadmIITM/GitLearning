
checking availale keys:-
ls -al ~/.ssh

create key:
ssh-keygen -t ed25519 -C "your-email@example.com"

#commit pushin command 
git push origin main

add agent:
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519  # or ~/.ssh/id_rsa

access key
cat ~/.ssh/id_ed25519.pub  # or ~/.ssh/id_rsa.pub


afasbjkfas