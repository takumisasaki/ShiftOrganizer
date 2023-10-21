<template>
  <div class="calendar-card">
    <div class="header-container">
      <div @click="prev" class="carousel__prev">
        <i class="fas fa-angle-left fa-5x"></i>
      </div>
      <h1>{{ currentYear }}年{{ currentMonth + 1 }}月</h1>
      <br />
      <div @click="next" class="carousel__next">
        <i class="fas fa-angle-right fa-5x"></i>
      </div>
    </div>
    <table>
      <thead>
        <tr>
          <th v-for="day in daysOfWeek" :key="day">{{ day }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="week in weeks" :key="week">
          <td v-for="day in week" :key="day">
            <button @click.prevent="dayClickEvent(day)">{{ day }}</button>
          </td>
        </tr>
      </tbody>
    </table>
    <div v-if="showDialog">
      <InputScheduleComponent
        :currentYear="currentYear"
        :currentMonth="currentMonth"
        :showDialog="showDialog"
        :selectedDay="selectedDay"
        :startTime="startTime"
        :endTime="endTime"
        :judgeSchedule="judgeSchedule"
        :submittedSchedule="submittedSchedule"
        @closeDialog="closed"
      />
    </div>
  </div>
</template>

<script>
import InputScheduleComponent from "./InputScheduleForm.vue";
import axios from "axios";

export default {
  data() {
    return {
      daysOfWeek: ["日", "月", "火", "水", "木", "金", "土"],
      currentDate: new Date(),
      selectedDay: null,
      showDialog: false,
      // timeDialog: false
      selectedTime: null,
      timesArray: [],
      startTime: "",
      endTime: "",
      judgeSchedule: false,
      submittedSchedule: []

    };
  },
  components: {
    InputScheduleComponent,
  },
  mounted() {
    for (let i = 0; i <= 24; i++) {
      let hour = i.toString().padStart(2, "0");
      this.timesArray.push("24:00");
      this.timesArray.push(hour + ":00");
      this.timesArray.push(hour + ":30");
    }
    return this.timesArray;
  },
  methods: {
    prev() {
      const prevMonth = this.currentDate.getMonth() - 1;
      this.currentDate = new Date(this.currentDate.setMonth(prevMonth));
    },
    next() {
      const nextMonth = this.currentDate.getMonth() + 1;
      this.currentDate = new Date(this.currentDate.setMonth(nextMonth));
    },
    dayClickEvent(day) {
      let tmp = new Date(this.currentDate.getFullYear(), this.currentDate.getMonth(), day)
      let date = tmp.toString();
      axios
        .get("http://127.0.0.1:8000/api/getdata", {
          params: {
            date: date
          }
        })
        .then((response) => {
          let parsedData = JSON.parse(response.data);
          this.submittedSchedule = parsedData
          // this.startTime = response.data.read_data["start_time"];
          // this.endTime = response.data.read_data["end_time"];
          this.judgeSchedule = !this.judgeSchedule;
          console.log("parsedData", parsedData);
        })
        .catch((error) => {
          console.log("errorが発生しました。", error);
        });
      this.selectedDay = day;
      this.showDialog = true;
    },
    closed() {
      this.showDialog = false;
      this.judgeSchedule = !this.judgeSchedule;
    },
  },
  computed: {
    currentYear() {
      return this.currentDate.getFullYear();
    },
    currentMonth() {
      let currentMonth = this.currentDate.getMonth();
      return currentMonth;
    },
    weeks() {
      let weeks = [];
      let firstDayOfMonth = new Date(
        this.currentDate.getFullYear(),
        this.currentDate.getMonth(),
        1
      );
      let lastDayOfMonth = new Date(
        this.currentDate.getFullYear(),
        this.currentDate.getMonth() + 1,
        0
      );
      let currentDay = firstDayOfMonth;

      // 最初の週を処理
      let firstWeek = new Array(7).fill("");
      for (let i = firstDayOfMonth.getDay(); i < 7; i++) {
        firstWeek[i] = currentDay.getDate();
        currentDay.setDate(currentDay.getDate() + 1);
      }
      weeks.push(firstWeek);

      // 残りの週を処理
      while (currentDay <= lastDayOfMonth) {
        let week = new Array(7).fill("");
        for (let i = 0; i < 7 && currentDay <= lastDayOfMonth; i++) {
          week[i] = currentDay.getDate();
          currentDay.setDate(currentDay.getDate() + 1);
        }
        weeks.push(week);
      }

      return weeks;
    },
  },
};
</script>

<style>
.header-container {
  display: flex; /* flexboxを使用して横に並べる */
  align-items: center; /* アイテムを中央揃え */
  justify-content: center;
}

.carousel__prev,
.carousel__next {
  cursor: pointer; /* クリック可能であることを示す */
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  border: 1px solid #ccc;
  padding: 10px;
  text-align: center;
}

.calendar-card {
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  overflow: hidden; /* 丸みを帯びた角を子要素にも適用する */
  background-color: #fff; /* カードの背景色 */
  padding: 20px; /* カード内の余白 */
  width: 80%;
  margin: 0 auto;
  background-color: snow;
}

@media only screen and (max-width: 600px) {
  .calendar-card {
    padding: 10px; /* 余白を減らす */
  }
  th,
  td {
    padding: 5px; /* セルのパディングを減らす */
  }
}

@media only screen and (max-width: 900px) {
  .calendar-card {
    padding: 15px; /* 余白を少し減らす */
  }
  th,
  td {
    padding: 7px; /* セルのパディングを少し減らす */
  }
}

.dialog {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  border-radius: 5px;
}

.carousel__prev i, .carousel__next i {
  font-size: 30px; /* 24ピクセルに変更、または好みのサイズに調整 */
  margin-right: 10px;
  margin-left: 10px;
}
</style>