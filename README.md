# Introduction

This is a simple code implementation for the Software Engineering - RHEL Migrations interview, it's intended to run on any rpm-based operating system, such as: Fedora, CentOS, RHEL, etc...

This code aims to get the current kernel versions installed on a running machine, it uses the `dnf` API to get metadata information about those packages and print them in a simple format to the stdout. 

# Getting the kernel version on your system

To run the script and check the installed versions, you can simple run the following command in any terminal you like.

```bash
$ python redhat_interview/main.py
```

Or, if you prefer, you could use `make` to run the same exactly command.

```bash
$ make
```

Also, there is a recording showing the output of the above command being ran in my own machine.
[![asciicast](https://asciinema.org/a/3TBTGdzXFnPwC8zpTChD1HHeo.svg)](https://asciinema.org/a/3TBTGdzXFnPwC8zpTChD1HHeo)

As a counter example, this is a record of the above command being ran with python2 (I don't have the `python2-dnf` pacakge installed on my machine) and failling immediatly as it cannot recognize the `dnf` module being imported.

[![asciicast](https://asciinema.org/a/xvAQXgm6f47JOyW69avXQX9ri.svg)](https://asciinema.org/a/xvAQXgm6f47JOyW69avXQX9ri)



# Common problems found during the development

While I was trying to implement a test case using `virtualenv` and `pytest` I found out that the newly generated `virtualenv` couldn't see the outside libraries in my machine (thus, the `python3-dnf` wasn't loaded for the `dnf` module use). I don't known if this is a common case or a misconfiguration by my side, but the workaround I got was making a `Dockerfile` for `CentOS` and `Fedora` to run the tests on. Those images are intended to run inside the `Github Actions` pipeline, but can be executed on any local machine with `Docker` installed too.

In the next section is covered on how to the tests are ran, and how to run then locally. 

# Running the tests

The tests are ran primarly in the `Gtihub Actions` pipeline CI with the help of a customized `Dockerfile` build, that will install the necessary packages and the right pip requirements. Besides the pipeline, the same commands can be ran in a local environment, such as the following:

The command below is used to build and run the docker container for the `CentOS Linux 8`.

```bash
$ docker build -f dockerfiles/centos8.Dockerfile -t centos-tests:latest 
$ docker run centos-tests:latest make test
```

And for the `Fedora Linux 34`, this is the equivalent command.

```bash
$ docker build -f dockerfiles/fedora34.Dockerfile -t fedora-tests:latest 
$ docker run fedora-tests:latest make test
```

# Additional stuff

This project was developed on a running `Fedora Linux 34` in my personal laptop.

Build information as follows: 

```
[r0x0d@fedora rhel-migrations-interview]$ uname -a
Linux fedora 5.13.12-200.fc34.x86_64 #1 SMP Wed Aug 18 13:27:18 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
```

And the list of kernels installed on my machine based on the command `rpm -q kernel` as follows: 

```
[r0x0d@fedora rhel-migrations-interview]$ rpm -q kernel
kernel-5.12.15-300.fc34.x86_64
kernel-5.12.17-300.fc34.x86_64
kernel-5.13.4-200.fc34.x86_64
kernel-5.13.6-200.fc34.x86_64
kernel-5.13.8-200.fc34.x86_64
kernel-5.13.9-200.fc34.x86_64
kernel-5.13.10-200.fc34.x86_64
kernel-5.13.12-200.fc34.x86_64
```