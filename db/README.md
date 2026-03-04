#MuseDiary

## Tech Stack
* **Database**: MongoDB

### 📊 Database Structure (JSON)

### 📊 Database Structure (JSON)

```javascript

const moodMapping = {
    happy: 10,
    angry: 1,
    love: 10,
    pleasure: 6,
  };

const userSchema = {
    ID: "String",
    email: "String",
    PW: "String"

    // 2. Number by moodMapping
    moodScore: {
        type: "Number",
        // When user click 'happy', enter 10
    },

    comment: "String",
    date: { type: "Date", default: Date.now }
};

