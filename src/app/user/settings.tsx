import React, { useState } from "react";

const SettingsPage: React.FC = () => {
  const [darkMode, setDarkMode] = useState(false);
  const [sound, setSound] = useState("default");
  const [language, setLanguage] = useState("ko");

  return (
    <div className="p-4 max-w-md mx-auto bg-white rounded-lg shadow">
      <h2 className="text-2xl font-bold mb-4">설정</h2>
      <div className="space-y-4">
        {/* 다크 모드 */}
        <div className="flex justify-between items-center">
          <label className="text-lg">다크 모드</label>
          <input
            type="checkbox"
            checked={darkMode}
            onChange={() => setDarkMode(!darkMode)}
            className="w-5 h-5"
          />
        </div>

        {/* 알람 소리 설정 */}
        <div>
          <label className="block text-lg">알람 소리</label>
          <select
            value={sound}
            onChange={(e) => setSound(e.target.value)}
            className="border p-2 rounded w-full"
          >
            <option value="default">기본 알람음</option>
            <option value="custom">사용자 지정</option>
          </select>
        </div>

        {/* 언어 변경 */}
        <div>
          <label className="block text-lg">언어</label>
          <select
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
            className="border p-2 rounded w-full"
          >
            <option value="ko">한국어</option>
            <option value="en">English</option>
          </select>
        </div>
      </div>
    </div>
  );
};

export default SettingsPage;
