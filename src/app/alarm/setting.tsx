import React, { useState } from "react";

const AlarmSettingPage: React.FC = () => {
  const [time, setTime] = useState<string>("07:00");
  const [repeat, setRepeat] = useState<string[]>([]);
  const [dismissMethod, setDismissMethod] = useState<string>("default");
  const [sound, setSound] = useState<string>("default");

  return (
    <div className="p-6 max-w-md mx-auto bg-white rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-6 text-center">⏰ 알람 설정</h2>

      {/* 알람 시간 설정 */}
      <div className="mb-4">
        <label className="block text-lg font-semibold mb-2">알람 시간</label>
        <input
          type="time"
          value={time}
          onChange={(e) => setTime(e.target.value)}
          className="border p-2 rounded w-full focus:ring focus:ring-blue-300"
          aria-label="알람 시간 선택"
        />
      </div>

      {/* 반복 요일 설정 */}
      <div className="mb-4">
        <label className="block text-lg font-semibold mb-2">반복 요일</label>
        <div className="flex space-x-2">
          {["월", "화", "수", "목", "금", "토", "일"].map((day) => (
            <button
              key={day}
              className={`p-2 rounded border ${
                repeat.includes(day) ? "bg-blue-500 text-white" : "bg-gray-200"
              }`}
              onClick={() =>
                setRepeat((prevRepeat) =>
                  prevRepeat.includes(day)
                    ? prevRepeat.filter((d) => d !== day)
                    : [...prevRepeat, day]
                )
              }
              aria-label={`${day}요일 반복`}
            >
              {day}
            </button>
          ))}
        </div>
      </div>

      {/* 알람 해제 방식 선택 */}
      <div className="mb-4">
        <label className="block text-lg font-semibold mb-2">알람 해제 방식</label>
        <select
          value={dismissMethod}
          onChange={(e) => setDismissMethod(e.target.value)}
          className="border p-2 rounded w-full focus:ring focus:ring-blue-300"
          aria-label="알람 해제 방식 선택"
        >
          <option value="default">기본 알람 해제</option>
          <option value="quiz">퀴즈 미션</option>
          <option value="toothbrush">칫솔 인식</option>
          <option value="voice">AI 음성 명령</option>
        </select>
      </div>

      {/* 사운드 설정 */}
      <div className="mb-4">
        <label className="block text-lg font-semibold mb-2">알람 사운드</label>
        <select
          value={sound}
          onChange={(e) => setSound(e.target.value)}
          className="border p-2 rounded w-full focus:ring focus:ring-blue-300"
          aria-label="알람 사운드 선택"
        >
          <option value="default">기본 알람음</option>
          <option value="custom">사용자 지정</option>
        </select>
      </div>

      {/* 저장 버튼 */}
      <button
        className="mt-4 w-full bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition"
        aria-label="알람 설정 저장"
      >
        저장
      </button>
    </div>
  );
};

export default AlarmSettingPage;

