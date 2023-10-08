$ # The following command will replace the third line of the Dockerfile with `USER repl`.
$ sed -i '3s/.*/USER repl/' Dockerfile$ cat Dockerfile
FROM ubuntu:22.04
RUN useradd -m repl
USER repl
RUN mkdir /home/repl/projects/pipeline_final
COPY /home/repl/project /home/repl/projects/pipeline_final


$ cat DockerfileFROM ubuntu:22.04
RUN useradd -m repl
USER repl
...
RUN mkdir projects/pipeline_final
COPY /home/repl/project projects/pipeline_final
$ sed -i '4s/.*/WORKDIR \/home\/repl/' Dockerfile
$ cat Dockerfile
FROM ubuntu:22.04
RUN useradd -m repl
USER repl
WORKDIR /home/repl
RUN mkdir projects/pipeline_final
COPY /home/repl/project projects/pipeline_final


$ docker build -t hello_image .Sending build context to Docker daemon  9.216kB
Step 1/3 : FROM ubuntu:22.04 ---> 3565a89d9e81
Step 2/3 : ENV NAME=Tim
 ---> Running in 5819d1d3499c
Removing intermediate container 5819d1d3499c
 ---> f424f9a7a48a
Step 3/3 : CMD echo "Hello, my name is $NAME"
 ---> Running in d05078601ff0
Removing intermediate container d05078601ff0
 ---> f3ae96c5ceae
Successfully built f3ae96c5ceae
Successfully tagged hello_image:latest
$ docker run -e NAME=YourName hello_image
Hello, my name is YourName



$ docker run repl_try_installE: Could not open lock file /var/lib/dpkg/lock-frontend - open (13:Permission denied)E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
$ cat Dockerfile
FROM ubuntu:22.04
RUN useradd -m repl
USER repl
CMD apt-get install python3
$