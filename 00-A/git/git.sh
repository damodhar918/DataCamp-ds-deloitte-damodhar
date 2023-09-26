git config --list
git --version
git config --global user.name "1234"
git config --global user.email "123@gmail.com"
git remote add origin "https://github.com/123/repl.git"
git remote -V
git init repl/
git remote add origin https://github.com/123/repl.git
git commit -m "init"
git add .
git commit -m "init"
git push -u origin master

#####################3333
ssh-keygen -t ed25519 -C "123@gmail.com"
ll
cd .ssh
ll
cat id_ed25519.pub 
git remote set-url origin git@github.com:damodhar918/repl.git
git push -u origin master
git add .
cd ..

