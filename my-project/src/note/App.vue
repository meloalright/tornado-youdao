<template>
  <div id="app">
    <img src="http://www.bootcss.com/p/flat-ui/images/demo/logo-mask.png">
    <router-view keep-alive></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}


body {
  margin: 0;
  padding: 0;
}
</style>
