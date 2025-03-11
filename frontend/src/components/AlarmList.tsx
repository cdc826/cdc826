import React from "react";
import AlarmCard from "./AlarmCard";

const dummyAlarms = [
  { time: "07:00", label: "기상", repeatDays: ["월", "화", "수"], isActive: true },
  { time: "22:00", label: "취침 준비", repeatDays: ["월", "수", "금"], isActive: false },
];

const AlarmList: React.FC = () => {
  return (
    <div className="space-y-4">
      {dummyAlarms.map((alarm, index) => (
        <AlarmCard 
          key={index} 
          {...alarm} 
          onToggle={() => console.log("토글")} 
          onDelete={() => console.log("삭제")}
        />
      ))}
    </div>
  );
};

export default AlarmList;
