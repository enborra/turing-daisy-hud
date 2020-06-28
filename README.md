# TURING SERVICE: DAISY-HUD

Heads up display for Daisy, a greenhouse droid

git clone https://github.com/enborra/turing-daisy-hud.git
sudo ln -s turing-daisy-hud /etc/turing/services/turing-daisy-hud

# Install Kivy
https://kivy.org/doc/stable/installation/installation-rpi.html

sudo apt update
sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
   pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   python-setuptools libgstreamer1.0-dev git-core \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} python-dev libmtdev-dev \
   xclip xsel libjpeg-dev
   
python3 -m pip3 install --upgrade --user pip setuptools
python3 -m pip3 install --upgrade --user Cython==0.29.10 pillow

pip3 install kivy


### On RaspberryPi
https://kivy.org/doc/stable/installation/installation-rpi.html  

`sudo apt update`  
  
`sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev pkg-config libgl1-mesa-dev libgles2-mesa-dev python-setuptools libgstreamer1.0-dev git-core gstreamer1.0-plugins-{bad,base,good,ugly} gstreamer1.0-{omx,alsa} python-dev libmtdev-dev xclip xsel libjpeg-dev`

`python -m pip install --upgrade --user pip setuptools` 
`python -m pip install --upgrade --user Cython==0.29.10 pillow`  


# TODOS
