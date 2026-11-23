# Eliminar el repositorio problemático
sudo rm -f /etc/apt/sources.list.d/shiftkey-packages.list
sudo rm -f /etc/apt/sources.list.d/shiftkey-desktop.list
sudo rm -f /usr/share/keyrings/shiftkey-packages.gpg
sudo rm -f /usr/share/keyrings/shiftkey-desktop.gpg

# Añadir el mirror alternativo
wget -qO - https://mirror.mwt.me/shiftkey-desktop/gpgkey \
  | gpg --dearmor \
  | sudo tee /usr/share/keyrings/mwt-desktop.gpg > /dev/null

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/mwt-desktop.gpg] https://mirror.mwt.me/shiftkey-desktop/deb/ any main" \
  | sudo tee /etc/apt/sources.list.d/mwt-desktop.list

# Actualizar
sudo apt update

# Instalar
sudo apt install github-desktop -y