# Hive Demo

## 1. Starting the VM and Installing Ambari.

These instructions allow for the use of Apache Ambari. They follow the guide located on [docs.hortonworks.com](https://docs.hortonworks.com/HDPDocuments/Ambari/Ambari-2.6.0.0/index.html)

Start the VM and fire up SSH. This demo uses a Windows host. Your host prompt may differ.

```
C:\work> vagrant up
```


## 2. Configuring Ambari

Once Ambari has been successfully installed, it is time to configure.

```
$ sudo ambari-server setup
```

Follow the instructions on screen.

* By default, Ambari runs as `root`. When asked `Customize user account for ambari-server daemon [y/n]`, enter `n`. There is no need to change this value for demo purposes.
* When asked about JRE version, select `Oracle JDK 1.8 + Java Cryptography Extension (JCE) Policy Files 8`.
* When asked to `Enter advanced database configuration [y/n]`, enter `n`. This will use the integrated Postgres database.


## 3. Running Ambari

You are now ready to run Ambari for the first time.

```
$ sudo ambari-server start
```

Navigate to [localhost:8080](http://localhost:8080). The default username and password is `admin`/`admin`.

Create a new cluster named `demo`. The machine name is `vagrant.vm`.

*Hint: create an entry in your local hosts file to point vagrant.vm to 127.0.0.1.*


## 4. Choose Services

Enable the following services.

1.  HDFS
2.  YARN + MapReduce2
3.  Tez
4.  Hive
5.  Pig
6.  Zookeeper
7.  Slider

All services will run on your VM.

You will need to set passwords for your databases. I recommend that you make them as simple as possible (e.g. `hive`/`hive` for your Hive database).

Once all issues have been addressed, you are ready to install your cluster. Go grab a coffee. Eat a sandwich. Send a handwritten letter to your mother. She misses you. This will take a while.


## 5. Settings

The following settings need to be updated. You can set these easily using the Ambari Admin UI. Once you change these settings, you will need to restart services.

### HDFS

```
dfs.replication = 1
```

#### Hive

```
hive.server2.enable.doAs = false
```

### Local Settings

You will find many things are easier if you make the `vagrant` user a member of the `hdfs` group. (`hdfs` is the local administrator group for HDFS. This can be set in Hive under `dfs.cluster.administrators`.)

```
$ sudo usermod -a -G hdfs vagrant
```
