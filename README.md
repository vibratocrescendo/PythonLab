# PythonLab

0 Misc
 0.1 Vagrant used with ubuntu-xenial 64 with these settings:
    Vagrant.configure("2") do |config|
    #Box Settings
    config.vm.box = "ubuntu/xenial64"

    # Provider Settings
    config.vm.provider "virtualbox" do |vb|
     vb.memory = 2048
     vb.cpus = 4
    end    
    
1.1. Python OWM
 1.1.1 Tested and working with environmental variables OPENWEATHER_API_KEY and CITY_NAME
 
1.2. Ansible
 1.2.1 Installs docker.io
 1.2.2 Enables logging to docker host syslog file (/var/log/syslog)
 
1.3. Docker
 1.3.1 Dockerfile tested as executable with provided external variables
 1.3.2 getweather.py configured as entrypoint and logs both to the console and to /var/log/syslog
 
2.1. Python Scanner
 2.1.1 Works with portstatus.json file
 2.1.2 Works with a single parameterized target
 2.1.3 Partially works with repetitive scans (no support for multiple previous hosts)
 

 
