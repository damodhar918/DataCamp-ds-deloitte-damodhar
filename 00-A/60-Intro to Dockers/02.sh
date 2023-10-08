$ docker run -d --name colleague_project my_projectf615613cd12f41aba09528f2615a42728c3a75db87f88ce37657a65f6d262479
$ docker ps -f "name=colleague_project"
CONTAINER ID   IMAGE        COMMAND                  CREATED  STATUS          PORTS     NAMES
f615613cd12f   my_project   "/bin/sh -c 'tail -f…"   10 minutes ago  Up 10 minutes             colleague_project
$ docker logs colleague_project


$ docker stop colleague_project
colleague_project
$ docker container rm colleague_project
colleague_project
$


$ docker pull hello-world
Using default tag: latest
latest: Pulling from library/hello-world719385e32844: Pull complete
Digest: sha256:4f53e2564790c8e7856ec08e384732aa38dc43c52f02952483e3f003afbf23db
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest


$ docker images
REPOSITORY          TAG       IMAGE ID       CREATED        SIZE
alpine              latest    8ca4688f4f35   9 days ago     7.33MBmariadb             latest    8ca4688f4f35   9 days ago     7.33MB
project_local_dev   latest    8ca4688f4f35   9 days ago     7.33MB
ubuntu              18.04     8ca4688f4f35   9 days ago     7.33MB
hello-world         latest    9c7a54a9a43c   5 months ago   13.3kB
$ docker pull ubuntu:22.04
22.04: Pulling from library/ubuntu
37aaf24cf781: Pull complete
Digest: sha256:9b8dec3bf938bc80fbe758d856e96fdfab5f56c39d44b0cff351e847bb1b01ea
Status: Downloaded newer image for ubuntu:22.04
docker.io/library/ubuntu:22.04


$ docker image rm ubuntuError response from daemon: conflict: unable to remove repository reference "ubuntu" (must force) - container 08ed53b77ca2 is using itsreferenced image 3565a89d9e81
$ docker container purne

Usage:  docker container COMMAND

Manage containers

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  commit      Create a new image from a container\'s changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  inspect     Display detailed information on one or more containers
  kill        Kill one or more running containers
  logs        Fetch the logs of a container
  ls          List containers
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  prune       Remove all stopped containers
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  run         Run a command in a new container
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker container COMMAND --help' for more information on a command.
$ docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
08ed53b77ca2fdf62a6d763d0fecb45f903de5695f785a0ab88b663b2f321426

Total reclaimed space: 0B
$ docker image rm ubuntu
Untagged: ubuntu:latest
Untagged: ubuntu@sha256:9b8dec3bf938bc80fbe758d856e96fdfab5f56c39d44b0cff351e847bb1b01ea
Deleted: sha256:3565a89d9e81a4cb4cb2b0d947c7c11227a3f358dc216d19fc54bfd77cd5b542
Deleted: sha256:01d4e4b4f381ac5a9964a14a650d7c074a2aa6e0789985d843f8eb3070b58f7d
$ docker images prune -a
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
$ docker image prune -a
WARNING! This will remove all images without at least one containerassociated to them.
Are you sure you want to continue? [y/N] y
Total reclaimed space: 0B


$ docker tag spam:v1 docker.mycompany.com/spam:v1
$ docker image push docker.mycompany.com/spam:v1
The push refers to repository [docker.mycompany.com/spam]
Get "https://docker.mycompany.com/v2/": dial tcp: lookup docker.mycompany.com on 169.254.20.10:53: no such host


$ docker save -o spam_updated.tar spam:v2


$ docker pull docker.mycompany.com/spam_alice:v3Error response from daemon: Get "https://docker.mycompany.com/v2/":dial tcp: lookup docker.mycompany.com on 169.254.20.10:53: no such host
$ docker run docker.mycompany.com/spam_alice:v3
Spam detection sample run. Spam correctly detected: 92%
$ tar -xvf spam_bob.tar
7d0d859b0472087e01c95f0b6eb6e9ec0e7ab311304dc913472c5d50fe5b232f/
7d0d859b0472087e01c95f0b6eb6e9ec0e7ab311304dc913472c5d50fe5b232f/VERSION
7d0d859b0472087e01c95f0b6eb6e9ec0e7ab311304dc913472c5d50fe5b232f/json
7d0d859b0472087e01c95f0b6eb6e9ec0e7ab311304dc913472c5d50fe5b232f/layer.tar
a2b616e451a0e2c23b5a4d7d79e66619820e9906c3ecbe4c3ace74c4f46e298a.json
manifest.json
repositories
$ docker load --input spam_bob.tar
Loaded image: spam_bob:v3
$ docker run -it spam_bob:v3
Spam detection sample run. Spam correctly detected: 87%
$ docker run spam_bob:v3
Spam detection sample run. Spam correctly detected: 87%
$
