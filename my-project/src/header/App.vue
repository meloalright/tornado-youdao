<template>
  <div id="header">
    <router-view keep-alive></router-view>
  </div>
</template>

<script>
export default {
  name: 'header'
}
</script>

<style>
#header {
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
