<template>
  <div>
    <header>
        <router-link to="/"><h1>小泉シフト管理アプリ</h1></router-link><br>
        <MenuBar @toggle-menu="showMenu = !showMenu" />
          <div v-if="showMenu" class="menu dialog-mask">
            <div class="menu dialog-content">
              <button @click="closeMenu" class="list-str">閉じる</button>
              <ul class="list-str">
                <li>hoge1</li>
                <li>hoge2</li>
                <li>hoge3</li>
              </ul>
            </div>
          </div>

    </header>
  </div>
</template>

<script>
import MenuBar from '@/components/MenuBar.vue';

export default {
name: 'HomeComponent',
data() {
  return {
    showMenu: false
  }
},
components:{
  MenuBar
},
props: {
    msg: String
  },
methods:{
  closeMenu() {
    this.showMenu = false;
  }
}
}
</script>

<style>
.dialog-mask {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7); /* 黒の半透明の背景 */
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}
.dialog-content {
    width: 300px;
    max-width: 90%; /* 必要に応じて調整 */
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}
.list-str{
  color:black;
}
</style>