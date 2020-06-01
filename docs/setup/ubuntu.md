# Ubuntu

!!! warning "Documentation in Progress"
    Check back soon for more updates.

---

## System

**Edit `/etc/hosts`**:

```shell
127.0.0.1 hostname
```
    
**Install JDK, Scala and Git**:
    
```shell
sudo apt install default-jdk scala git -y
```

**Install Poetry**:
    
```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
```
    
**Install Oracle JDK**:

```shell
sudo apt update
sudo add-apt-repository ppa:webupd8team/java
sudo apt update
sudo apt install oracle-java8-installer oracle-java8-set-default
```    
    
## Spark

This [guide](https://phoenixnap.com/kb/install-spark-on-ubuntu) provides more information on how to setup Spark on Ubuntu. 

Start by downloading Spark 2.4.5 for Hadoop 2.7. 

```shell
curl -O https://www.apache.org/dyn/closer.lua/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz
```

Extract the archive. 

```shell
tar xvf spark-2.4.5-bin-hadoop2.7.tgz
```

Move it to `/opt/spark`.

```shell
sudo mv spark-2.4.5-bin-hadoop2.7/ /opt/spark
```

Update the environment variables by adding the following to your shell profile.  

```shell 
export SPARK_HOME=/opt/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
export PYSPARK_PYTHON=/usr/bin/python3
```

Alternatively, add it to your profile using `echo`. 

```shell 
echo "export SPARK_HOME=/opt/spark" >> ~/.profile
echo "export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin" >> ~/.profile
echo "export PYSPARK_PYTHON=/usr/bin/python3" >> ~/.profile
```

This assumes your profile is in `.profile`. It may also be in another location like `~/.bashrc` or `~/.zshrc`.  Activate your changes as follows. 

```shell
source ~/.bashrc
```

Start a stand-alone server. 

```shell
start-master.sh
```

The process will listen on 8080. 

```shell
ss -tunelp | grep 8080
tcp   LISTEN  0       1                           *:8080  
```

Start a worker process. 

```shell
start-slave.sh spark://ubuntu:7077
```

You can stop the processes using the following commands. 

```shell
stop-slave.sh
stop-master.sh
```
    
## TensorFlow

Ubuntu 18.04 ships with Python 3 by default

```shell 
sudo apt install python3-venv
```

!!! note
    If you have a dedicated NVIDIA GPU and want to take advantage of its processing power, instead of tensorflow install the tensorflow-gpu package which includes GPU support.

### GPU Support

Check the following links to more information on GPU support. 

* [CUDA GPUs][cuda-gpus]
* [TensorFlow GPU Install][tensorflow-gpu-install]
    
```shell
# Add NVIDIA package repositories
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.1.243-1_amd64.deb
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
sudo dpkg -i cuda-repo-ubuntu1804_10.1.243-1_amd64.deb
sudo apt-get update
wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
sudo apt install ./nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
sudo apt-get update

# Install NVIDIA driver
sudo apt-get install --no-install-recommends nvidia-driver-430
# Reboot. Check that GPUs are visible using the command: nvidia-smi

# Install development and runtime libraries (~4GB)
sudo apt-get install --no-install-recommends \
    cuda-10-1 \
    libcudnn7=7.6.4.38-1+cuda10.1  \
    libcudnn7-dev=7.6.4.38-1+cuda10.1


# Install TensorRT. Requires that libcudnn7 is installed above.
sudo apt-get install -y --no-install-recommends libnvinfer6=6.0.1-1+cuda10.1 \
    libnvinfer-dev=6.0.1-1+cuda10.1 \
    libnvinfer-plugin6=6.0.1-1+cuda10.1
```

[cuda-gpus]: https://developer.nvidia.com/cuda-gpus    
[docker-linux-builds]: https://www.tensorflow.org/install/source#docker_linux_builds
[tensorflow-gpu-install]: https://www.tensorflow.org/install/gpu#install_cuda_with_apt
