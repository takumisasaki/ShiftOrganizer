<template>
  <div>
    <div class="header-container">
      <div @click="prev" class="carousel__prev"><i class="fas fa-angle-left fa-5x"></i></div>
        <h1>{{ currentMonth }}</h1>
      <div @click="next" class="carousel__next"><i class="fas fa-angle-right fa-5x"></i></div>
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
            {{ day }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      daysOfWeek: ['日', '月', '火', '水', '木', '金', '土'],
      currentDate: new Date()
    };
  },
  methods:{
    prev(){
      const prevMonth = this.currentDate.getMonth() - 1;
      this.currentDate = new Date(this.currentDate.setMonth(prevMonth));
    },
    next(){
      const nextMonth = this.currentDate.getMonth() + 1;
      this.currentDate = new Date(this.currentDate.setMonth(nextMonth));
    }
  },
  computed: {
    currentMonth() {
      console.log(this.currentDate, 'computedで呼び出されました');
      return this.currentDate.toLocaleString('default', {month: 'long'});
    },
    weeks() {
      let weeks = [];
      let firstDayOfMonth = new Date(this.currentDate.getFullYear(), this.currentDate.getMonth(), 1);
      let lastDayOfMonth = new Date(this.currentDate.getFullYear(), this.currentDate.getMonth() + 1, 0);
      let currentDay = firstDayOfMonth;

      // 最初の週を処理
      let firstWeek = new Array(7).fill('');
      for (let i = firstDayOfMonth.getDay(); i < 7; i++) {
      firstWeek[i] = currentDay.getDate();
      currentDay.setDate(currentDay.getDate() + 1);
      }
      weeks.push(firstWeek);

      // 残りの週を処理
      while (currentDay <= lastDayOfMonth) {
      let week = new Array(7).fill('');
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
  display: flex;      /* flexboxを使用して横に並べる */
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

th, td {
  border: 1px solid #ccc;
  padding: 10px;
  text-align: center;
}
</style>