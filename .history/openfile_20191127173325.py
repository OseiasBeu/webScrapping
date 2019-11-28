import xlrd

for file in *.xls; 
do; 
echo "Transcoding $file"; pyexcel transcode "$file" "${file}x";

 done;



xlread(arque)