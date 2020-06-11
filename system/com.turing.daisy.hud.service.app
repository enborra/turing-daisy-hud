[Unit]
Description=Turing Daisy Droid HUD
Wants=network.target
After=network.target

[Service]
Type=simple
ExecStart=/bin/bash /etc/turing/services/turing-daisy-hud/boot.sh
Restart=on-abort

[Install]
WantedBy=multi-user.target
