0x0B. Redis basic


## Learning Objectives

- Learn how to use redis for basicoperations
- Learn how to use redis as a simplecache

## Requirements

- All of your files will beinterpreted/compiled on Ubuntu 18.04LTS using python3 (version 3.7)
- All of your files should end with anew line
- A ```README.md``` file, at the root of thefolder of the project, is mandatory
- The first line of all your filesshould be exactly ```#!/usr/bin/envpython3```
- Your code should use the ```pycodestylestyle``` (version 2.5)
- All your modules should havedocumentation (```python3 -c 'prin(__import__("my_module").__doc__)'```)
- All your classes should havedocumentation (```python3 -c 'prin(__import__("my_module").MyClass__doc__)'```)
- All your functions and methodsshould have documentation (```python3-c 'print(__import__("my_module")my_function.__doc__)'``` and ```python3 -c'print(__import__("my_module")MyClass.my_function.__doc__)'```)
- A documentation is not a simpleword, it’s a real sentenceexplaining what’s the purpose of themodule, class or method (the lengthof it will be verified)
- All your functions and coroutinesmust be type-annotated.

## Install Redis on Ubuntu 18.04
```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```
## Use Redis in a container

Redis server is stopped by default - when you are starting a container, you should start it with: ```service redis-server start```
