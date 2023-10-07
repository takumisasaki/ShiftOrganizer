<template>
  <form @submit.prevent="sendData">
    <div class="day-dialog-mask"></div>
    <div class="dialog">
      {{ currentYear }}年{{ currentMonth + 1 }}月
      <h3>予定を入力してください: {{ selectedDay }}日</h3>
      <div class="time-container">
      <select v-model="selectedStartTime" name="start-time">
        <option class="start-time" value="" disabled>開始時刻</option>
        <option v-for="time in timesArray" :key="time" :value="time">
          {{ time }}
        </option>
      </select>
      <span class="time-separator">〜</span>
      <select v-model="selectedEndTime" name="end-time">
        <option class="start-time" value="" disabled>終了時刻</option>
        <option v-for="time in timesArray" :key="time" :value="time">
          {{ time }}
        </option>
      </select>
    </div>
      <!-- <input v-model="schedule" name="scheduleValue" /> -->
      <div class="button-group">
        <button class="close-button" @click="closed">キャンセル</button>
        <button class="save-button" type="submit">保存</button>
      </div>
    </div>
  </form>
</template>

<script>
import { ref } from "vue";
import axios from "axios";

export default {
  props: {
    showDialog: {
      type: Boolean,
      required: true,
    },
    selectedDay: {
      type: Number,
      required: false,
    },
    currentYear: {
      type: Number,
      required: true,
    },
    currentMonth: {
      type: Number,
      required: true,
    },
    startTime:{
        type:String,
        required: false
    },
    endTime:{
        type:String,
        required: false
    }
  },
  data() {
    return {
      timesArray: [],
    };
  },
  mounted() {
    for (let i = 0; i <= 24; i++) {
      let hour = i.toString().padStart(2, "0");
      this.timesArray.push(hour + ":00");
      this.timesArray.push(hour + ":30");
    //   if(i == 24){
    //     this.timesArray.push("24:00");
    //   }else {
    //     this.timesArray.push(hour + ":00");
    //     this.timesArray.push(hour + ":30");
    //   }
    }
  },
  setup(props) {
    const schedule = ref("");
    const selectedStartTime = ref("");
    const selectedEndTime = ref("");
    let startDateObj = new Date();
    let endDateObj = new Date();

    const sendData = () => {
      const formData = new FormData();
      const [start_hour, start_minute] = selectedStartTime.value
        .split(":")
        .map(Number);
      const [end_hour, end_minute] = selectedEndTime.value
        .split(":")
        .map(Number);
      startDateObj = new Date(
        props.currentYear,
        props.currentMonth,
        props.selectedDay,
        start_hour,
        start_minute,
        0,
        0
      );
      endDateObj = new Date(
        props.currentYear,
        props.currentMonth,
        props.selectedDay,
        end_hour,
        end_minute,
        0,
        0
      );

      formData.append("value", schedule.value);
      formData.append("start-date", startDateObj);
      formData.append("end-date", endDateObj);

      axios
        .post("http://127.0.0.1:8000/api/data", formData)
        .then((response) => {
          console.log("response_data", response.data);
        })
        .catch((error) => {
          console.log("errorが発生しました。", error);
        });
    };
    return {
      schedule,
      startDateObj,
      endDateObj,
      selectedStartTime,
      selectedEndTime,
      sendData,
    };
  },
  methods: {
    closed() {
      this.$emit("close-dialog");
    },
  },
};
</script>

<style>
.day-dialog-mask {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex; /* Flexboxを使用して中央配置 */
  align-items: center; /* 垂直方向の中央に配置 */
  justify-content: center; /* 水平方向の中央に配置 */
}

.dialog {
  width: 60vw; /* ビューポートの60%の幅 */
  max-width: 90%; /* 最大の幅は90%に制限 */
  background-color: #fff;
  padding: 2%; /* パディングを適切な値に変更 */
  border-radius: 5px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); /* 影を追加して立体感を出す */
  padding:4%;
}

h3 {
  margin-bottom:20px;
  border-bottom: 1px solid #ccc;
}

select,
input,
button {
  margin-bottom: 15px; /* 要素間にマージンを追加 */
  padding: 8px; /* パディングを追加して入力要素を使いやすくする */
  border-radius: 5px;
}

select[name="start-time"],
select[name="end-time"] {
  width: 50%; 
  background-color: #b3b3b3; 
  color: #525252;
  margin-bottom: 0px; 
}

select[name="start-time"]:focus,
select[name="end-time"]:focus {
  color: #000;
}

.time-container {
    display: flex;
    align-items: center;
    justify-content:  space-between;
}

.time-separator {
  display: inline-block; /* インラインブロックとして表示 */
  margin: 0px 10px; /* 左右に10pxのマージンを追加 */
  
  vertical-align: middle; /* selectボックスとの中央揃え */
}


input {
    margin-bottom: 20px;
}


button {
  cursor: pointer;
  background-color: #007bff;
  color: #fff;
  border: none;
}

.button-group {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
}

.close-button, .save-button {
    flex: 1;
    margin: 5px 5px;
    padding: 8px 10px;
    box-sizing: border-box;
    width: 48px; 
}

.close-button{
    background-color: #ccc;
    color: #333;
}

.save-button {
    background-color: #007bff;
    color: #fff;
}

/* button:hover {
  background-color: #0056b3;
} */

/* button:active {
  background-color: #003f80;
} */

select {
  background-color: #b3b3b3; /* 背景色を白に設定 */
  color: #525252; /* テキストの色を濃い灰色に設定 */
}


/* 選択された時のテキストの色を指定 */
select:focus {
  color: #000;
}

.start-time {
  color: #b3b3b3;
}
</style>
