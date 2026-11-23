wget -qO - https://packagecloud.io/shiftkey/desktop/gpgkey \
  | gpg --dearmor \
  | sudo tee /usr/share/keyrings/shiftkey-desktop.gpg > /dev/null

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/shiftkey-desktop.gpg] https://packagecloud.io/shiftkey/desktop/any/ any main" \
  | sudo tee /etc/apt/sources.list.d/shiftkey-desktop.list

sudo apt update

sudo apt install github-desktop -y