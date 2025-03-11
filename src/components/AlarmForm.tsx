import React, { useState } from "react";

const AlarmForm: React.FC = () => {
  const [time, setTime] = useState("");
  const [label, setLabel] = useState("");
  const [repeatDays, setRepeatDays] = useState<string[]>([]);
  
  const handleSubmit = () => {
    console.log("알람 설정:", { time, label, repeatDays });
  };

  return (
    <form onSubmit={(e) => { e.preventDefault(); handleSubmit(); }} className="flex flex-col space-y-2">
      <label>
        시간:
        <input type="time" value={time} onChange={(e) => setTime(e.target.value)} className="border p-2 rounded" />
      </label>
      <label>
        이름:
        <input type="text" value={label} onChange={(e) => setLabel(e.target.value)} className="border p-2 rounded" />
      </label>
      <button type="submit" className="bg-blue-500 text-white p-2 rounded">알람 추가</button>
    </form>
  );
};

export default AlarmForm;
