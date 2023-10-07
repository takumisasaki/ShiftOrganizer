<template>
  <div>
    <HomeComponent class="header"></HomeComponent>
    <!-- <router-link to="/login">Login</router-link><br> -->
    <!-- <router-link to="/schedule">スケジュール</router-link> -->
    <router-view/>
    <ScheduleComponent></ScheduleComponent>
  </div>
</template>

<script>
import HomeComponent from './components/HomeComponent'
import ScheduleComponent from './components/ScheduleComponent'

export default {
  name: 'App',
  components: {
    HomeComponent,
    ScheduleComponent
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.header {
  background-color: green;
  color: white; /* もし文字色も変更したい場合 */
  padding: 10px; /* 必要に応じてパディングも追加 */
}
</style>