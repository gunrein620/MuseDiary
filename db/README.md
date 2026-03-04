#MuseDiary

## Tech Stack
* **Database**: MongoDB

### 📊 Database Structure (JSON)

### 📊 Database Structure (JSON)

```json
{
  "UserSchema": {
    "username": "String",      // 로그인 아이디 또는 닉네임
    "email": "String",         // 이메일
    "pw": "String",  // 암호화된 비밀번호
    "createdAt": {
      "type": "Date",
      "default": "Date.now"
    }
  },
  
  "moodMapping": {             // 감정별 점수 기준표 (독립적인 정보)
    "happy": 10,
    "angry": 1,
    "love": 10,
    "pleasure": 6
  },

  "DiaryEntrySchema": {
    "userId": "ObjectId",      // UserSchema의 _id를 참조 (누가 썼는지)
    "content": "String",       // 일기 본문
    "mood": "String",          // "happy", "angry" 등
    "moodScore": "Number",     // 매핑된 점수 (예: 10)
    "createdAt": {
      "type": "Date",
      "default": "Date.now"
    }
  }
}