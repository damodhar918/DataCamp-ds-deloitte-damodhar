$ docker build .Sending build context to Docker daemon  9.216kB
Step 1/1 : FROM ubuntu:22.0422.04: Pulling from library/ubuntu
37aaf24cf781: Pull complete
Digest: sha256:9b8dec3bf938bc80fbe758d856e96fdfab5f56c39d44b0cff351e847bb1b01ea
Status: Downloaded newer image for ubuntu:22.04
 ---> 3565a89d9e81
Successfully built 3565a89d9e81
$ docker build -t my_first_image .
Sending build context to Docker daemon  9.216kB
Step 1/1 : FROM ubuntu:22.04
 ---> 3565a89d9e81
Successfully built 3565a89d9e81
Successfully tagged my_first_image:latest


$ cat > Dockerfile
$ cat > Dockerfile
FROM ubuntu
$ echo "RUN apt-get update" >> Dockerfile
$ cat Dockerfile
FROM ubuntu
RUN apt-get update


$ vi Dockerfile
$ docker build -t my_app .
Sending build context to Docker daemon  10.75kBStep 1/2 : FROM ubuntu:22.04
22.04: Pulling from library/ubuntu
37aaf24cf781: Pull complete
Digest: sha256:9b8dec3bf938bc80fbe758d856e96fdfab5f56c39d44b0cff351e847bb1b01ea
Status: Downloaded newer image for ubuntu:22.04
 ---> 3565a89d9e81
Step 2/2 : RUN mkdir my_app
 ---> Running in 04293ad73cd5
Removing intermediate container 04293ad73cd5
 ---> d8ec3efe478f
Successfully built d8ec3efe478f
Successfully tagged my_app:latest
$ cat Dockerfile
FROM ubuntu:22.04
RUN mkdir my_app


$ cat Dockerfilecat: Dockerfile: No such file or directory
$ cat > DockerfileFROM ubuntu:latest
$ vi Dockerfile
$ vi Dockerfile
$ cat Dockerfile
FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python3
$ docker build -t my_python_image .
Sending build context to Docker daemon  11.26kB
Step 1/3 : FROM ubuntu:latest
latest: Pulling from library/ubuntu
Digest: sha256:9b8dec3bf938bc80fbe758d856e96fdfab5f56c39d44b0cff351e847bb1b01ea
Status: Downloaded newer image for ubuntu:latest
 ---> 3565a89d9e81
Step 2/3 : RUN apt-get update
 ---> Running in ed48fbd35d4b
Get:1 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
Get:2 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [1081 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy InRelease [270 kB]
Get:4 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [1002 kB]
Get:5 http://security.ubuntu.com/ubuntu jammy-security/multiverse amd64 Packages [44.0 kB]
Get:6 http://security.ubuntu.com/ubuntu jammy-security/restricted amd64 Packages [1226 kB]
Get:7 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [119kB]
Get:8 http://archive.ubuntu.com/ubuntu jammy-backports InRelease [109 kB]
Get:9 http://archive.ubuntu.com/ubuntu jammy/main amd64 Packages [1792 kB]
Get:10 http://archive.ubuntu.com/ubuntu jammy/multiverse amd64 Packages [266 kB]
Get:11 http://archive.ubuntu.com/ubuntu jammy/restricted amd64 Packages [164 kB]
Get:12 http://archive.ubuntu.com/ubuntu jammy/universe amd64 Packages [17.5 MB]
Get:13 http://archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 Packages [49.8 kB]
Get:14 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [1266 kB]
Get:15 http://archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 Packages [1252 kB]
Get:16 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [1342 kB]
Get:17 http://archive.ubuntu.com/ubuntu jammy-backports/main amd64 Packages [50.4 kB]
Get:18 http://archive.ubuntu.com/ubuntu jammy-backports/universe amd64 Packages [28.1 kB]
Fetched 27.6 MB in 3s (11.0 MB/s)
Reading package lists...
Removing intermediate container ed48fbd35d4b
 ---> 41c64e9e2631
Step 3/3 : RUN apt-get install -y python3
 ---> Running in a7fcb29022ab
Reading package lists...
Building dependency tree...
Reading state information...
The following additional packages will be installed:
  libexpat1 libmpdec3 libpython3-stdlib libpython3.10-minimal
  libpython3.10-stdlib libreadline8 libsqlite3-0 media-types python3-minimal
  python3.10 python3.10-minimal readline-common
Suggested packages:
  python3-doc python3-tk python3-venv python3.10-venv python3.10-doc binutils
  binfmt-support readline-doc
The following NEW packages will be installed:
  libexpat1 libmpdec3 libpython3-stdlib libpython3.10-minimal
  libpython3.10-stdlib libreadline8 libsqlite3-0 media-types python3
  python3-minimal python3.10 python3.10-minimal readline-common
0 upgraded, 13 newly installed, 0 to remove and 2 not upgraded.
Need to get 6531 kB of archives.
After this operation, 23.5 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libpython3.10-minimal amd64 3.10.12-1~22.04.2 [811 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libexpat1 amd64 2.4.7-1ubuntu0.2 [91.0 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3.10-minimal amd64 3.10.12-1~22.04.2 [2258 kB]
Get:4 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3-minimal amd64 3.10.6-1~22.04 [24.3 kB]
Get:5 http://archive.ubuntu.com/ubuntu jammy/main amd64 media-typesall 7.0.0 [25.5 kB]
Get:6 http://archive.ubuntu.com/ubuntu jammy/main amd64 libmpdec3 amd64 2.5.1-2build2 [86.8 kB]
Get:7 http://archive.ubuntu.com/ubuntu jammy/main amd64 readline-common all 8.1.2-1 [53.5 kB]
Get:8 http://archive.ubuntu.com/ubuntu jammy/main amd64 libreadline8 amd64 8.1.2-1 [153 kB]
Get:9 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libsqlite3-0 amd64 3.37.2-2ubuntu0.1 [641 kB]
Get:10 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libpython3.10-stdlib amd64 3.10.12-1~22.04.2 [1849 kB]
Get:11 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3.10 amd64 3.10.12-1~22.04.2 [509 kB]
Get:12 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libpython3-stdlib amd64 3.10.6-1~22.04 [6910 B]
Get:13 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3 amd64 3.10.6-1~22.04 [22.8 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 6531 kB in 1s (4987 kB/s)
Selecting previously unselected package libpython3.10-minimal:amd64.
(Reading database ... 4395 files and directories currently installed.)
Preparing to unpack .../libpython3.10-minimal_3.10.12-1~22.04.2_amd64.deb ...
Unpacking libpython3.10-minimal:amd64 (3.10.12-1~22.04.2) ...
Selecting previously unselected package libexpat1:amd64.
Preparing to unpack .../libexpat1_2.4.7-1ubuntu0.2_amd64.deb ...
Unpacking libexpat1:amd64 (2.4.7-1ubuntu0.2) ...
Selecting previously unselected package python3.10-minimal.
Preparing to unpack .../python3.10-minimal_3.10.12-1~22.04.2_amd64.deb ...
Unpacking python3.10-minimal (3.10.12-1~22.04.2) ...
Setting up libpython3.10-minimal:amd64 (3.10.12-1~22.04.2) ...
Setting up libexpat1:amd64 (2.4.7-1ubuntu0.2) ...
Setting up python3.10-minimal (3.10.12-1~22.04.2) ...
Selecting previously unselected package python3-minimal.
(Reading database ... 4699 files and directories currently installed.)
Preparing to unpack .../0-python3-minimal_3.10.6-1~22.04_amd64.deb ...
Unpacking python3-minimal (3.10.6-1~22.04) ...
Selecting previously unselected package media-types.
Preparing to unpack .../1-media-types_7.0.0_all.deb ...
Unpacking media-types (7.0.0) ...
Selecting previously unselected package libmpdec3:amd64.
Preparing to unpack .../2-libmpdec3_2.5.1-2build2_amd64.deb ...
Unpacking libmpdec3:amd64 (2.5.1-2build2) ...
Selecting previously unselected package readline-common.
Preparing to unpack .../3-readline-common_8.1.2-1_all.deb ...
Unpacking readline-common (8.1.2-1) ...
Selecting previously unselected package libreadline8:amd64.
Preparing to unpack .../4-libreadline8_8.1.2-1_amd64.deb ...
Unpacking libreadline8:amd64 (8.1.2-1) ...
Selecting previously unselected package libsqlite3-0:amd64.
Preparing to unpack .../5-libsqlite3-0_3.37.2-2ubuntu0.1_amd64.deb ...
Unpacking libsqlite3-0:amd64 (3.37.2-2ubuntu0.1) ...
Selecting previously unselected package libpython3.10-stdlib:amd64.
Preparing to unpack .../6-libpython3.10-stdlib_3.10.12-1~22.04.2_amd64.deb ...
Unpacking libpython3.10-stdlib:amd64 (3.10.12-1~22.04.2) ...
Selecting previously unselected package python3.10.
Preparing to unpack .../7-python3.10_3.10.12-1~22.04.2_amd64.deb ...
Unpacking python3.10 (3.10.12-1~22.04.2) ...
Selecting previously unselected package libpython3-stdlib:amd64.
Preparing to unpack .../8-libpython3-stdlib_3.10.6-1~22.04_amd64.deb ...
Unpacking libpython3-stdlib:amd64 (3.10.6-1~22.04) ...
Setting up python3-minimal (3.10.6-1~22.04) ...
Selecting previously unselected package python3.
(Reading database ... 5129 files and directories currently installed.)
Preparing to unpack .../python3_3.10.6-1~22.04_amd64.deb ...
Unpacking python3 (3.10.6-1~22.04) ...
Setting up media-types (7.0.0) ...
Setting up libsqlite3-0:amd64 (3.37.2-2ubuntu0.1) ...
Setting up libmpdec3:amd64 (2.5.1-2build2) ...
Setting up readline-common (8.1.2-1) ...
Setting up libreadline8:amd64 (8.1.2-1) ...
Setting up libpython3.10-stdlib:amd64 (3.10.12-1~22.04.2) ...
Setting up libpython3-stdlib:amd64 (3.10.6-1~22.04) ...
Setting up python3.10 (3.10.12-1~22.04.2) ...
Setting up python3 (3.10.6-1~22.04) ...
running python rtupdate hooks for python3.10...
running python post-rtupdate hooks for python3.10...
Processing triggers for libc-bin (2.35-0ubuntu3.3) ...
Removing intermediate container a7fcb29022ab
 ---> 32208fd51d2f
Successfully built 32208fd51d2f
Successfully tagged my_python_image:latest


$ vi Dockerfile$ cat Dockerfile
FROM ubuntu:22.04RUN apt-get update
RUN apt-get -y install python3
COPY pipeline.py /app/


$ vi Dockerfile$ cat Dockerfile
FROM ubuntu:22.04RUN apt-get update
RUN apt-get -y install python3
COPY pipeline_v3 /app

$ docker build -t pipeline_v3 .
Sending build context to Docker daemon  13.31kB
Step 1/4 : FROM ubuntu:22.04
 ---> 3565a89d9e81
Step 2/4 : RUN apt-get update
 ---> Using cache
 ---> 41c64e9e2631
Step 3/4 : RUN apt-get -y install python3
 ---> Running in 9137c8a87cbf
Reading package lists...
Building dependency tree...
Reading state information...
The following additional packages will be installed:
  libexpat1 libmpdec3 libpython3-stdlib libpython3.10-minimal
  libpython3.10-stdlib libreadline8 libsqlite3-0 media-types python3-minimal
  python3.10 python3.10-minimal readline-common
Suggested packages:
  python3-doc python3-tk python3-venv python3.10-venv python3.10-doc binutils
  binfmt-support readline-doc
The following NEW packages will be installed:
  libexpat1 libmpdec3 libpython3-stdlib libpython3.10-minimal
  libpython3.10-stdlib libreadline8 libsqlite3-0 media-types python3
  python3-minimal python3.10 python3.10-minimal readline-common
0 upgraded, 13 newly installed, 0 to remove and 2 not upgraded.
Need to get 6531 kB of archives.
After this operation, 23.5 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libpython3.10-minimal amd64 3.10.12-1~22.04.2 [811 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libexpat1 amd64 2.4.7-1ubuntu0.2 [91.0 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3.10-minimal amd64 3.10.12-1~22.04.2 [2258 kB]
Get:4 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3-minimal amd64 3.10.6-1~22.04 [24.3 kB]
Get:5 http://archive.ubuntu.com/ubuntu jammy/main amd64 media-typesall 7.0.0 [25.5 kB]
Get:6 http://archive.ubuntu.com/ubuntu jammy/main amd64 libmpdec3 amd64 2.5.1-2build2 [86.8 kB]
Get:7 http://archive.ubuntu.com/ubuntu jammy/main amd64 readline-common all 8.1.2-1 [53.5 kB]
Get:8 http://archive.ubuntu.com/ubuntu jammy/main amd64 libreadline8 amd64 8.1.2-1 [153 kB]
Get:9 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libsqlite3-0 amd64 3.37.2-2ubuntu0.1 [641 kB]
Get:10 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libpython3.10-stdlib amd64 3.10.12-1~22.04.2 [1849 kB]
Get:11 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3.10 amd64 3.10.12-1~22.04.2 [509 kB]
Get:12 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libpython3-stdlib amd64 3.10.6-1~22.04 [6910 B]
Get:13 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3 amd64 3.10.6-1~22.04 [22.8 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 6531 kB in 0s (36.4 MB/s)
Selecting previously unselected package libpython3.10-minimal:amd64.
(Reading database ... 4395 files and directories currently installed.)
Preparing to unpack .../libpython3.10-minimal_3.10.12-1~22.04.2_amd64.deb ...
Unpacking libpython3.10-minimal:amd64 (3.10.12-1~22.04.2) ...
Selecting previously unselected package libexpat1:amd64.
Preparing to unpack .../libexpat1_2.4.7-1ubuntu0.2_amd64.deb ...
Unpacking libexpat1:amd64 (2.4.7-1ubuntu0.2) ...
Selecting previously unselected package python3.10-minimal.
Preparing to unpack .../python3.10-minimal_3.10.12-1~22.04.2_amd64.deb ...
Unpacking python3.10-minimal (3.10.12-1~22.04.2) ...
Setting up libpython3.10-minimal:amd64 (3.10.12-1~22.04.2) ...
Setting up libexpat1:amd64 (2.4.7-1ubuntu0.2) ...
Setting up python3.10-minimal (3.10.12-1~22.04.2) ...
Selecting previously unselected package python3-minimal.
(Reading database ... 4699 files and directories currently installed.)
Preparing to unpack .../0-python3-minimal_3.10.6-1~22.04_amd64.deb ...
Unpacking python3-minimal (3.10.6-1~22.04) ...
Selecting previously unselected package media-types.
Preparing to unpack .../1-media-types_7.0.0_all.deb ...
Unpacking media-types (7.0.0) ...
Selecting previously unselected package libmpdec3:amd64.
Preparing to unpack .../2-libmpdec3_2.5.1-2build2_amd64.deb ...
Unpacking libmpdec3:amd64 (2.5.1-2build2) ...
Selecting previously unselected package readline-common.
Preparing to unpack .../3-readline-common_8.1.2-1_all.deb ...
Unpacking readline-common (8.1.2-1) ...
Selecting previously unselected package libreadline8:amd64.
Preparing to unpack .../4-libreadline8_8.1.2-1_amd64.deb ...
Unpacking libreadline8:amd64 (8.1.2-1) ...
Selecting previously unselected package libsqlite3-0:amd64.
Preparing to unpack .../5-libsqlite3-0_3.37.2-2ubuntu0.1_amd64.deb ...
Unpacking libsqlite3-0:amd64 (3.37.2-2ubuntu0.1) ...
Selecting previously unselected package libpython3.10-stdlib:amd64.
Preparing to unpack .../6-libpython3.10-stdlib_3.10.12-1~22.04.2_amd64.deb ...
Unpacking libpython3.10-stdlib:amd64 (3.10.12-1~22.04.2) ...
Selecting previously unselected package python3.10.
Preparing to unpack .../7-python3.10_3.10.12-1~22.04.2_amd64.deb ...
Unpacking python3.10 (3.10.12-1~22.04.2) ...
Selecting previously unselected package libpython3-stdlib:amd64.
Preparing to unpack .../8-libpython3-stdlib_3.10.6-1~22.04_amd64.deb ...
Unpacking libpython3-stdlib:amd64 (3.10.6-1~22.04) ...
Setting up python3-minimal (3.10.6-1~22.04) ...
Selecting previously unselected package python3.
(Reading database ... 5129 files and directories currently installed.)
Preparing to unpack .../python3_3.10.6-1~22.04_amd64.deb ...
Unpacking python3 (3.10.6-1~22.04) ...
Setting up media-types (7.0.0) ...
Setting up libsqlite3-0:amd64 (3.37.2-2ubuntu0.1) ...
Setting up libmpdec3:amd64 (2.5.1-2build2) ...
Setting up readline-common (8.1.2-1) ...
Setting up libreadline8:amd64 (8.1.2-1) ...
Setting up libpython3.10-stdlib:amd64 (3.10.12-1~22.04.2) ...
Setting up libpython3-stdlib:amd64 (3.10.6-1~22.04) ...
Setting up python3.10 (3.10.12-1~22.04.2) ...
Setting up python3 (3.10.6-1~22.04) ...
running python rtupdate hooks for python3.10...
running python post-rtupdate hooks for python3.10...
Processing triggers for libc-bin (2.35-0ubuntu3.3) ...
Removing intermediate container 9137c8a87cbf
 ---> 3a52bc79cfbd
Step 4/4 : COPY pipeline_v3 /app
 ---> ca93fd948bfd
Successfully built ca93fd948bfd
Successfully tagged pipeline_v3:latest


RUN curl https://assets.datacamp.com/production/repositories/6082/datasets/31a5052c6a5424cbb8d939a7a6eff9311957e7d0/pipeline_final.zip  -o /pipeline_final.zip \ && unzip /pipeline_final.zip -d <unzipped-directory> \ && rm /pipeline_final.zip 
$ cat > Dockerfile$ cat > Dockerfile
FROM ubuntu:latestRUN apt-get update
RUN apt-get install -y python3 curl unzip
$ vi Dockerfile
$ vi Dockerfile
$ cat Dockerfile
FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python3 curl unzip

# The follwing command will append the RUN instructions to the end of the Dockerfile.
# echo -e "RUN curl https://assets.datacamp.com/production/repositories/6082/datasets/31a5052c6a5424cbb8d939a7a6eff9311957e7d0/pipeline_final.zip -o /pipeline_final.zip\nRUN unzip /pipeline_final.zip\nRUN rm /pipeline_final.zip" >> Dockerfile
# Alternaed tively:
# 1. Open the Dockerfile using `nano Dockerfile`.
RUN curl https://assets.datacamp.com/production/repositories/6082/datasets/31a5052c6a5424cbb8d939a7a6eff9311957e7d0/pipeline_final.zip -o /pipeline_final.zip
#` to the end of the Dockerfile.
# 3. Add `
RUN unzip /pipeline_final.zip
#` to the end of the Dockerfile.
# 4. Add `
RUN rm /pipeline_final.zip
#` to the end of the Dockerfile.
# 5. Save the file and exit nano using CTRL+s and CTRL+x
$ docker build -t pipeline .
Sending build context to Docker daemon   5.12kB
Error response from daemon: dockerfile parse error line 6: unknown instruction: ECHO


$ vi Dockerfile$ echo "CMD python3" >> Dockerfile
$ cat DockerfileFROM ubuntu:22.04
RUN apt-get update
RUN apt-get -y install python3
CMD python3
$ docker build -t pipeline_debug .
Sending build context to Docker daemon  10.75kB
Step 1/4 : FROM ubuntu:22.04
22.04: Pulling from library/ubuntu
37aaf24cf781: Pull complete
Digest: sha256:9b8dec3bf938bc80fbe758d856e96fdfab5f56c39d44b0cff351e847bb1b01ea
Status: Downloaded newer image for ubuntu:22.04
 ---> 3565a89d9e81
Step 2/4 : RUN apt-get update
 ---> Running in e15e5ebdbdab
Get:1 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy InRelease [270 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [119kB]
Get:4 http://archive.ubuntu.com/ubuntu jammy-backports InRelease [109 kB]
Get:5 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [1081 kB]
Get:6 http://security.ubuntu.com/ubuntu jammy-security/multiverse amd64 Packages [44.0 kB]
Get:7 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [1002 kB]
Get:8 http://security.ubuntu.com/ubuntu jammy-security/restricted amd64 Packages [1226 kB]
Get:9 http://archive.ubuntu.com/ubuntu jammy/restricted amd64 Packages [164 kB]
Get:10 http://archive.ubuntu.com/ubuntu jammy/multiverse amd64 Packages [266 kB]
Get:11 http://archive.ubuntu.com/ubuntu jammy/main amd64 Packages [1792 kB]
Get:12 http://archive.ubuntu.com/ubuntu jammy/universe amd64 Packages [17.5 MB]
Get:13 http://archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 Packages [1252 kB]
Get:14 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [1342 kB]
Get:15 http://archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 Packages [49.8 kB]
Get:16 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [1266 kB]
Get:17 http://archive.ubuntu.com/ubuntu jammy-backports/main amd64 Packages [50.4 kB]
Get:18 http://archive.ubuntu.com/ubuntu jammy-backports/universe amd64 Packages [28.1 kB]
Fetched 27.6 MB in 1s (25.1 MB/s)
Reading package lists...
Removing intermediate container e15e5ebdbdab
 ---> e6f660d95136
Step 3/4 : RUN apt-get -y install python3
 ---> Running in 3142210e461c
Reading package lists...
Building dependency tree...
Reading state information...
The following additional packages will be installed:
  libexpat1 libmpdec3 libpython3-stdlib libpython3.10-minimal
  libpython3.10-stdlib libreadline8 libsqlite3-0 media-types python3-minimal
  python3.10 python3.10-minimal readline-common
Suggested packages:
  python3-doc python3-tk python3-venv python3.10-venv python3.10-doc binutils
  binfmt-support readline-doc
The following NEW packages will be installed:
  libexpat1 libmpdec3 libpython3-stdlib libpython3.10-minimal
  libpython3.10-stdlib libreadline8 libsqlite3-0 media-types python3
  python3-minimal python3.10 python3.10-minimal readline-common
0 upgraded, 13 newly installed, 0 to remove and 2 not upgraded.
Need to get 6531 kB of archives.
After this operation, 23.5 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libpython3.10-minimal amd64 3.10.12-1~22.04.2 [811 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libexpat1 amd64 2.4.7-1ubuntu0.2 [91.0 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3.10-minimal amd64 3.10.12-1~22.04.2 [2258 kB]
Get:4 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3-minimal amd64 3.10.6-1~22.04 [24.3 kB]
Get:5 http://archive.ubuntu.com/ubuntu jammy/main amd64 media-typesall 7.0.0 [25.5 kB]
Get:6 http://archive.ubuntu.com/ubuntu jammy/main amd64 libmpdec3 amd64 2.5.1-2build2 [86.8 kB]
Get:7 http://archive.ubuntu.com/ubuntu jammy/main amd64 readline-common all 8.1.2-1 [53.5 kB]
Get:8 http://archive.ubuntu.com/ubuntu jammy/main amd64 libreadline8 amd64 8.1.2-1 [153 kB]
Get:9 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libsqlite3-0 amd64 3.37.2-2ubuntu0.1 [641 kB]
Get:10 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libpython3.10-stdlib amd64 3.10.12-1~22.04.2 [1849 kB]
Get:11 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3.10 amd64 3.10.12-1~22.04.2 [509 kB]
Get:12 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libpython3-stdlib amd64 3.10.6-1~22.04 [6910 B]
Get:13 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3 amd64 3.10.6-1~22.04 [22.8 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 6531 kB in 0s (39.1 MB/s)
Selecting previously unselected package libpython3.10-minimal:amd64.
(Reading database ... 4395 files and directories currently installed.)
Preparing to unpack .../libpython3.10-minimal_3.10.12-1~22.04.2_amd64.deb ...
Unpacking libpython3.10-minimal:amd64 (3.10.12-1~22.04.2) ...
Selecting previously unselected package libexpat1:amd64.
Preparing to unpack .../libexpat1_2.4.7-1ubuntu0.2_amd64.deb ...
Unpacking libexpat1:amd64 (2.4.7-1ubuntu0.2) ...
Selecting previously unselected package python3.10-minimal.
Preparing to unpack .../python3.10-minimal_3.10.12-1~22.04.2_amd64.deb ...
Unpacking python3.10-minimal (3.10.12-1~22.04.2) ...
Setting up libpython3.10-minimal:amd64 (3.10.12-1~22.04.2) ...
Setting up libexpat1:amd64 (2.4.7-1ubuntu0.2) ...
Setting up python3.10-minimal (3.10.12-1~22.04.2) ...
Selecting previously unselected package python3-minimal.
(Reading database ... 4699 files and directories currently installed.)
Preparing to unpack .../0-python3-minimal_3.10.6-1~22.04_amd64.deb ...
Unpacking python3-minimal (3.10.6-1~22.04) ...
Selecting previously unselected package media-types.
Preparing to unpack .../1-media-types_7.0.0_all.deb ...
Unpacking media-types (7.0.0) ...
Selecting previously unselected package libmpdec3:amd64.
Preparing to unpack .../2-libmpdec3_2.5.1-2build2_amd64.deb ...
Unpacking libmpdec3:amd64 (2.5.1-2build2) ...
Selecting previously unselected package readline-common.
Preparing to unpack .../3-readline-common_8.1.2-1_all.deb ...
Unpacking readline-common (8.1.2-1) ...
Selecting previously unselected package libreadline8:amd64.
Preparing to unpack .../4-libreadline8_8.1.2-1_amd64.deb ...
Unpacking libreadline8:amd64 (8.1.2-1) ...
Selecting previously unselected package libsqlite3-0:amd64.
Preparing to unpack .../5-libsqlite3-0_3.37.2-2ubuntu0.1_amd64.deb ...
Unpacking libsqlite3-0:amd64 (3.37.2-2ubuntu0.1) ...
Selecting previously unselected package libpython3.10-stdlib:amd64.
Preparing to unpack .../6-libpython3.10-stdlib_3.10.12-1~22.04.2_amd64.deb ...
Unpacking libpython3.10-stdlib:amd64 (3.10.12-1~22.04.2) ...
Selecting previously unselected package python3.10.
Preparing to unpack .../7-python3.10_3.10.12-1~22.04.2_amd64.deb ...
Unpacking python3.10 (3.10.12-1~22.04.2) ...
Selecting previously unselected package libpython3-stdlib:amd64.
Preparing to unpack .../8-libpython3-stdlib_3.10.6-1~22.04_amd64.deb ...
Unpacking libpython3-stdlib:amd64 (3.10.6-1~22.04) ...
Setting up python3-minimal (3.10.6-1~22.04) ...
Selecting previously unselected package python3.
(Reading database ... 5129 files and directories currently installed.)
Preparing to unpack .../python3_3.10.6-1~22.04_amd64.deb ...
Unpacking python3 (3.10.6-1~22.04) ...
Setting up media-types (7.0.0) ...
Setting up libsqlite3-0:amd64 (3.37.2-2ubuntu0.1) ...
Setting up libmpdec3:amd64 (2.5.1-2build2) ...
Setting up readline-common (8.1.2-1) ...
Setting up libreadline8:amd64 (8.1.2-1) ...
Setting up libpython3.10-stdlib:amd64 (3.10.12-1~22.04.2) ...
Setting up libpython3-stdlib:amd64 (3.10.6-1~22.04) ...
Setting up python3.10 (3.10.12-1~22.04.2) ...
Setting up python3 (3.10.6-1~22.04) ...
running python rtupdate hooks for python3.10...
running python post-rtupdate hooks for python3.10...
Processing triggers for libc-bin (2.35-0ubuntu3.3) ...
Removing intermediate container 3142210e461c
 ---> 0bf86a39a0fc
Step 4/4 : CMD python3
 ---> Running in f3d2ef3baa36
Removing intermediate container f3d2ef3baa36
 ---> 14c90e7ff1ba
Successfully built 14c90e7ff1ba
Successfully tagged pipeline_debug:latest
$ docker run -it pipeline_debug
Python 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
$ docker run pipeline_debug


