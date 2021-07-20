#!/bin/bash

pip3 uninstall -y ezsmdeploy
rm -rf ezsmdeploy-1.0*
wget https://files.pythonhosted.org/packages/57/bb/5eef92c5afb64589293185d20580c35e55ab45336d6ed28013c62945b882/ezsmdeploy-1.0.8.tar.gz
tar xf ezsmdeploy-1.0.8.tar.gz
sed -i '3s/1.0.8/1.0.9/' ezsmdeploy-1.0.8/PKG-INFO
sed -i '3s/1.0.8/1.0.9/' ezsmdeploy-1.0.8/ezsmdeploy.egg-info/PKG-INFO
sed -i '22s/1.0.8/1.0.9/' ezsmdeploy-1.0.8/setup.py
sed -i '22s/1.0.8/1.0.9/' ezsmdeploy-1.0.8/ezsmdeploy/__init__.py
!sed -i '359s/prefix/self.prefix/' ezsmdeploy-1.0.8/ezsmdeploy/__init__.py
sed -i '359s/prefix/""/' ezsmdeploy-1.0.8/ezsmdeploy/__init__.py
mv ezsmdeploy-1.0.8 ezsmdeploy-1.0.9
tar czf ezsmdeploy-1.0.9.tar.gz  ezsmdeploy-1.0.9
pip3 install ./ezsmdeploy-1.0.9.tar.gz 

