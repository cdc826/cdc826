import React, { useEffect, useState } from "react";

// 알람의 타입을 정의
interface Alarm {
  id: number;
  time: string; // "07:00" 형식
  label: string;
  isActive: boolean;
}

interface AlarmTriggerProps {
  alarms: Alarm[];
}

const AlarmTrigger: React.FC<AlarmTriggerProps> = ({ alarms }) => {
  const [currentTime, setCurrentTime] = useState(
    new Date().toLocaleTimeString("ko-KR", { hour: "2-digit", minute: "2-digit" })
  );

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentTime(new Date().toLocaleTimeString("ko-KR", { hour: "2-digit", minute: "2-digit" }));
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    const activeAlarms = alarms.filter((alarm) => alarm.isActive && alarm.time === currentTime);
    if (activeAlarms.length > 0) {
      alert("🔔 알람이 울립니다!"); // 팝업 알림 (소리 추가 가능)
      // new Audio("/alarm-sound.mp3").play(); // 알람 소리 추가 가능
    }
  }, [currentTime, alarms]);

  return null; // UI를 렌더링하지 않고 백그라운드에서 실행
};

export default AlarmTrigger;
