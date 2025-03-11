import React, { useState } from "react";

const AlarmMissionPage: React.FC = () => {
  const [quizAnswer, setQuizAnswer] = useState("");
  const [correct, setCorrect] = useState(false);

  const handleQuizSubmit = () => {
    if (quizAnswer === "42") {
      setCorrect(true);
      alert("정답입니다! 알람이 해제되었습니다.");
    } else {
      alert("틀렸습니다! 다시 시도하세요.");
    }
  };

  return (
    <div className="p-4 max-w-md mx-auto bg-white rounded-lg shadow">
      <h2 className="text-2xl font-bold mb-4">알람 미션</h2>

      {/* 퀴즈 문제 */}
      <div>
        <label className="block text-lg">퀴즈를 풀어야 알람이 해제됩니다!</label>
        <p className="mb-2">"삶, 우주, 그리고 모든 것의 궁극적인 질문에 대한 답은?"</p>
        <input
          type="text"
          value={quizAnswer}
          onChange={(e) => setQuizAnswer(e.target.value)}
          className="border p-2 rounded w-full"
        />
        <button onClick={handleQuizSubmit} className="mt-2 bg-blue-500 text-white px-4 py-2 rounded">
          제출
        </button>
      </div>

      {/* 칫솔 인식 (예제) */}
      <div className="mt-4">
        <label className="block text-lg">칫솔을 인식하세요</label>
        <button className="bg-green-500 text-white px-4 py-2 rounded">칫솔 인식 시작</button>
      </div>
    </div>
  );
};

export default AlarmMissionPage;
