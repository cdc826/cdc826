import React, { useState } from "react";

const ProfilePage: React.FC = () => {
  const [name, setName] = useState("사용자 이름");
  const [email, setEmail] = useState("user@example.com");
  const [editing, setEditing] = useState(false);

  return (
    <div className="p-4 max-w-md mx-auto bg-white rounded-lg shadow">
      <h2 className="text-2xl font-bold mb-4">프로필</h2>
      <div className="flex flex-col space-y-2">
        <img
          src="https://via.placeholder.com/100"
          alt="프로필 사진"
          className="w-24 h-24 rounded-full mx-auto"
        />
        <div>
          <label className="block text-sm font-medium">이름</label>
          {editing ? (
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="border p-2 rounded w-full"
            />
          ) : (
            <p className="text-lg">{name}</p>
          )}
        </div>
        <div>
          <label className="block text-sm font-medium">이메일</label>
          <p className="text-lg">{email}</p>
        </div>
        <button
          onClick={() => setEditing(!editing)}
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          {editing ? "저장" : "프로필 편집"}
        </button>
      </div>
    </div>
  );
};

export default ProfilePage;
