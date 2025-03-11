import React from "react";

interface AlarmCardProps {
  time: string;
  label: string;
  repeatDays: string[];
  isActive: boolean;
  onToggle: () => void;
  onDelete: () => void;
}

const AlarmCard: React.FC<AlarmCardProps> = ({ time, label, repeatDays, isActive, onToggle, onDelete }) => {
  return (
    <div className="border p-4 rounded-md shadow-md flex justify-between items-center">
      <div>
        <h2 className="text-xl font-bold">{time}</h2>
        <p className="text-sm text-gray-500">{label}</p>
        <p className="text-xs">{repeatDays.join(", ")}</p>
      </div>
      <div className="flex items-center space-x-2">
        <button onClick={onToggle} className={`px-3 py-1 rounded ${isActive ? "bg-green-500" : "bg-gray-400"}`}>
          {isActive ? "ON" : "OFF"}
        </button>
        <button onClick={onDelete} className="px-3 py-1 bg-red-500 text-white rounded">삭제</button>
      </div>
    </div>
  );
};

export default AlarmCard;
