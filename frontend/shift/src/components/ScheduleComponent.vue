<template>
    <div>
      <h1>{{ currentMonth }}</h1>
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
      };
    },
    computed: {
      currentMonth() {
        const date = new Date();
        return date.toLocaleString('default', { month: 'long' });
      },
      weeks() {
        const weeks = [];
        const date = new Date();
        const firstDayOfMonth = new Date(date.getFullYear(), date.getMonth(), 1);
        const lastDayOfMonth = new Date(date.getFullYear(), date.getMonth() + 1, 0);
        let currentDay = firstDayOfMonth;

        // 最初の週を処理
        const firstWeek = new Array(7).fill('');
        for (let i = firstDayOfMonth.getDay(); i < 7; i++) {
        firstWeek[i] = currentDay.getDate();
        currentDay.setDate(currentDay.getDate() + 1);
        }
        weeks.push(firstWeek);

        // 残りの週を処理
        while (currentDay <= lastDayOfMonth) {
        const week = new Array(7).fill('');
        for (let i = 0; i < 7 && currentDay <= lastDayOfMonth; i++) {
            week[i] = currentDay.getDate();
            console.log(currentDay);
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
  