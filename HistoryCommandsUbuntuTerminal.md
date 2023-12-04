## Задание 1

mkdir Kennel<br/>
cd ~/Kennel<br/>
cat > home_animals<br/>
cat > pack_animals<br/>
cat home_animals pack_animals > animals<br/>
cat animals<br/>
mv animals mans_friends<br/>
ls -ali<br/>

## Задание 2

cd ..<br/>
mkdir Kennel_system<br/>
cd ~/Kennel<br/>
mv mans_friends ~/Kennel_system<br/>
cd ~/Kennel_system<br/>
ls -ali<br/>

## Задание 3

sudo wget https://dev.mysql.com/get/mysql-apt-config_0.8.23-1_all.deb<br/>
sudo dpkg -i mysql-apt-config_0.8.23-1_all.deb<br/>
sudo apt-get update<br/>
sudo apt-get install mysql-server<br/>

## Задание 4

sudo wget https://download.docker.com/linux/ubuntu/dists/jammy/pool/stable/amd64/docker-ce-cli_20.10.13~3-0~ubuntu-jammy_amd64.deb<br/>
sudo dpkg -i docker-ce-cli_20.10.13ubuntu-jammy_amd64.deb<br/>
sudo dpkg -r docker-ce-cli<br/>
