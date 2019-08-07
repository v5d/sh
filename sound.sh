RUNDIR=`dirname $0`
PIDFILE="${RUNDIR}/$0.pid"
#找到pid文件，判断当前脚本是否运行
if [ -s ${PIDFILE} ]; then
   SPID=`cat ${PIDFILE}`
   if [ -e /proc/${SPID}/status ]; then
      zenity --notification --text="已经运行"
      exit 1
  fi
  cat /dev/null > ${PIDFILE}
fi
echo $$ > ${PIDFILE}

#jobs need to do...

cd /dev/shm
if [ -e wd];then
audacious -Hp /dev/shm/wd
else
wd=`xclip -o` && curl http://dict.youdao.com/dictvoice?audio=${wd}  >/dev/shm/wd  && audacious -Hp  /dev/shm/wd
fi

cat /dev/null > ${PIDFILE}

