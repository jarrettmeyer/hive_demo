Vagrant.configure("2") do |config|

    # Use this base image.
    config.vm.box = "bento/ubuntu-16.04"

    # Provision the machine.
    config.vm.provision "shell", path: "provision/provision.sh"

    # Open up the necessary ports for HDFS and Hive. Yes, there are a lot of them. In a more realistic scenario, you
    # would have multiple servers performing various functions. Because this is a test VM, all services are running
    # on this single VM.
    config.vm.network "forwarded_port", guest: 3000,  host: 3000    # Grafana Web UI http://localhost:3000
    config.vm.network "forwarded_port", guest: 8020,  host: 8020
    config.vm.network "forwarded_port", guest: 8042,  host: 8042
    config.vm.network "forwarded_port", guest: 8080,  host: 8080    # Ambari Web UI http://localhost:8080
    config.vm.network "forwarded_port", guest: 8088,  host: 8088
    config.vm.network "forwarded_port", guest: 9000,  host: 9000    # HDFS port
    config.vm.network "forwarded_port", guest: 9999,  host: 9999    # Tez Web UI http://localhost:9999
    config.vm.network "forwarded_port", guest: 10000, host: 10000   # Hiveserver2 thrift port
    config.vm.network "forwarded_port", guest: 10001, host: 10001
    config.vm.network "forwarded_port", guest: 10002, host: 10002   # Hiveserver2 Web UI http://localhost:10002
    config.vm.network "forwarded_port", guest: 19888, host: 19888
    config.vm.network "forwarded_port", guest: 50030, host: 50030
    config.vm.network "forwarded_port", guest: 50070, host: 50070   # Hadoop Namenode UI http://localhost:50070
    config.vm.network "forwarded_port", guest: 50075, host: 50075   # Hadoop Datanode UI http://localhost:50075

    config.vm.provider "virtualbox" do |v|
        v.memory = 16384
        v.cpus = 4
    end

end
