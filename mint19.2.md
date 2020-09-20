mint_xfce4_19.2安装设置

- 默认安装时候选自动登录，不能加密家目录。
- 启动分区别写到硬盘，和win冲突。
- home, root, boot, swap分区


### 卸载
sudo apt-get remove --purge hexchat thunderbird tomboy compiz* printer-driver-* simple-scan timeshift transmission-* xfce4-taskmanager xserver-xorg-video-fbdev xserver-xorg-video-amdgpu xserver-xorg-video-ati xserver-xorg-video-nouveau xserver-xorg-video-qxl xserver-xorg-video-radeon xserver-xorg-video-vesa xserver-xorg-video-vmware gnome-logs mint-backgrounds-tessa mint-backgrounds-tara mintreport hplip-data* modemmanager cups*

## 日志


### systemd进程
sudo systemctl disable kerneloops.service rsyslog.service 


### log文件
- logrotate journal设置


- ln -sf /dev/null ~/.xsession-errors
- ln -sf /dev/null ~/.xsession-errors.old



---
- cd /var/log
- sudo ln -sf /dev/null kern.log
- sudo ln -sf /dev/null lastlog
- sudo ln -sf /dev/null ufw.log
- sudo ln -sf /dev/null wtmp
- sudo ln -sf /dev/null Xorg.0.log
- sudo ln -sf /dev/null auth.log
- sudo ln -sf /dev/null boot.log
- sudo ln -sf /dev/null alternatives.log
- sudo rm -rf speech-dispatcher samba openvpn ntpstats
- sudo ln -sf /dev/null dpkg.log
- sudo ln -sf /dev/null faillog
- sudo ln -sf /dev/null gpu-manager.log
- sudo ln -sf /dev/null fontconfig.log
- sudo rm rf- gufw.log
- sudo ln -sf /dev/null bootstrap.log
- cd ~

---

# 安装软件
sudo apt-get install firefox firefox-locale-zh-hans xournal mypaint bleachbit fcitx fcitx-googlepinyin fcitx-ui-classic fcitx-frontend-all fcitx-frontend-qt4 xclip qrencode gnome-system-monitor gnome-screenshot 

### bleachbit清理垃圾

### firefox 
- https://www.mozilla.org/zh-CN/firefox/all/#product-desktop-release
- about:config, 里面字符串 browser.cache.disk.parent_directory, 值 /dev/shm/firefox
- adblock, zoom level, gesture

### ufw
- sudo ufw default deny incoming
- sudo ufw default allow outgoing
- sudo ufw enable

### 亮度
- chmod 777 /sys/class/backlight/intel_backlight/brightness
- a=$(cat /sys/class/backlight/intel_backlight/brightness)
- a=`expr $a + 10`
- echo $a > /sys/class/backlight/intel_backlight/brightness

### xfce4
- ~/.comfig/xfce4 只读，禁止修改写入
- 竖面板orage时钟
- 快捷键设置

### 写硬盘检测 
- fatrace


