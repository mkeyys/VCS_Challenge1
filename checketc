
echo "[Log checketc - `date +%T` `date +%D'/'%m'/'%Y`]" >> /var/log/checketc.log
function createFile(){
	if [ ! -e $1 ]; then
		touch $1
	fi
}
function checkTextFile(){
	check=$(file -i $1 | grep -w "text/plain")
	if [[ $check ]]; then
		echo $line >> /var/log/checketc.log
		head -n 10 "$1" >> /var/log/checketc.log
	else 
		echo $1 >> /var/log/checketc.log
	fi
}

function checkNewFile(){
	old=$1
	now=$2
	while read -r line; do
		check=$(grep -w $line -m 1 $old)
		if [ ! $check ]; then
			checkTextFile $line >> /var/log/checketc.log
			echo -e "\n" >> /var/log/checketc.log
		fi
	done < $now
} 

function checkDeleteFile(){
	old=$1
	now=$2
	while read -r line; do
		check=$(grep -w $line -m 1 $now)
		if [ ! $check ]; then
			echo $line >> /var/log/checketc.log
		fi
	done < $old

}

	
listOldFiles='/home/vcsmkey/Desktop/Chall01/listoldfiles.txt'
listCurrentFiles='/home/vcsmkey/Desktop/Chall01/listcurrentfiles.txt'
listCheck='/home/vcsmkey/Desktop/Chall01/listcheck.txt'

#create files
createFile $listOldFiles
createFile $listCurrentFiles
createFile $listCheck
#write files
sudo find /etc -type f > $listCurrentFiles 
sudo find /etc -type f -cmin -30 > $listCheck

echo -e "\n===== Danh sach file tao moi =====\n" >> /var/log/checketc.log
checkNewFile $listOldFiles $listCheck

echo -e "\n===== Danh sach file sua doi =====\n" >> /var/log/checketc.log		
checkModified=$(sudo find /etc -mmin -30)
echo $checkModified | sed 's/ /\n/g' >> /var/log/checketc.log

echo -e "\n===== Danh sach file bi xoa =====\n" >> /var/log/checketc.log
checkDeleteFile $listOldFiles $listCurrentFiles
cat $listCurrentFiles > $listOldFiles

mail -s "Log checketc" root@localhost < /var/log/checketc.log

