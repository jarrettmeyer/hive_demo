#!/usr/bin/env bash

SSH_DIR=/root/.ssh

# Update Ubuntu, make sure all packages are up to date.
apt-get update -y
apt-get dist-upgrade -y

# Disable transparent hugepages.
echo never > /sys/kernel/mm/transparent_hugepages/enabled

# Install networking time protocol (NTP).
apt-get install -y ntp
timedatectl set-ntp on

# Create SSH keys for root.
ssh-keygen -t rsa -P '' -C root.localhost -f $SSH_DIR/id_rsa
cat $SSH_DIR/id_rsa.put >> $SSH_DIR/authorized_keys
chmod 600 $SSH_DIR/authorized_keys

# Copy configuration files.
cp /vagrant/config/hosts /etc/hosts

# Add the apt repository for Ambari. Install Ambari.
wget -O /etc/apt/sources.list.d/ambari.list http://public-repo-1.hortonworks.com/ambari/ubuntu16/2.x/updates/2.6.0.0/ambari.list
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com B9733A7A07513CAD
apt-get update -y
apt-get install -y ambari-server
