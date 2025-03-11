import React, { useState } from "react";

const AlarmDismissPage: React.FC = () => {
  const [dismissed, setDismissed] = useState(false);

  const handleDismiss = () => {
    setDismissed(true);
    alert("알람이 해제되었습니다!");
  };

  return (
    <div className="p-4 max-w-md mx-auto bg-white rounded-lg shadow">
      <h2 className="text-2xl font-bold mb-4">알람 해제</h2>
      {dismissed ? (
        <p className="text-green-500">알람이 해제되었습니다.</p>
      ) : (
        <button onClick={handleDismiss} className="bg-red-500 text-white px-4 py-2 rounded">
          알람 해제
        </button>
      )}
    </div>
  );
};

export default AlarmDismissPage;
