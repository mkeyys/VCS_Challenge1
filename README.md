# VCS_Challenge1
# Get_infor_system.sh 
      Viết shell script info.sh hiển thị các thông tin về hệ thống, bao gồm:
      1.	Tên máy, tên bản phân phối
      2.	Phiên bản hệ điều hành
      3.	Thông tin CPU (tên, 32bit hay 64bit, tốc độ)
      4.	Thông tin bộ nhớ vật lí (tổng bao nhiêu MB)
      5.	Thông tin ổ đĩa còn trống bao nhiêu MB
      6.	Danh sách địa chỉ IP của hệ thống
      7.	Danh sách user trên hệ thống (sắp xếp theo thứ tự abc)
      8.	Thông tin  các tiến trình đang chạy với quyền root (sắp xếp theo thứ tự abc)
      9.	Thông tin các port đang mở (sắp xếp theo port tăng dần)
      10.	Danh sách các thư mục trên hệ thống cho phép other có quyền ghi
      11.	Danh sách các gói phần mềm  (tên gói, phiên bản) được cài trên hệ thống
# checketc.sh
      Viết shell script checketc.sh đặt lịch chạy định kỳ 30 phút / lần để thực hiện:
      1.	Kiểm tra thư mục /etc có file nào được tạo mới (so với lần chạy trước) không? Nếu có, hiển thị thông tin file đó và nếu là file text thì hiển thị 10 dòng đầu tiên của file
      2.	Kiểm tra thư mục /etc có file nào thay đổi không?  Nếu có hiển thị tên file bị thay đổi
      3.	Thư mục /etc có file nào bị xóa không? Nếu có hiển thị tên file bị xóa
      4.	Đẩy log ra file /var/log/checketc.log
      5.	Gửi email cho quản trị viên root@localhost
# checkssh.sh
      Viết shell script sshmonitor.sh đặt lịch chạy định kỳ 5 phút / lần để thực hiện:
      1.	List danh sách các phiên đăng nhập mới qua ssh (so với lần chạy trước)
      2.	Nếu phát hiện có phiên đăng nhập mới qua ssh (so với lần chạy trước) thì gửi email cho quản trị viên root@localhost.
# search_bin.py
      Lập trình ngôn ngữ python trên linux: Viết chương trình cài đặt lại thuật toán tìm kiếm nhị phân trên python 
