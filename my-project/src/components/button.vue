<template>
  <div>
    <div class="button-wrapper">
      <div class="left green button" v-on:click="back()">Back</div>
      <div class="left green button" v-on:click="open()">共享我的笔记链接</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Button',
  data () {
    return {
      msg: 'tornado-youdao'
    }
  },
  methods: {
    back: function () {
      window.location.href = "/home/"
    },
    open: function () {
      window.location.href = "#/note/share/"
    }
  },
  beforeMount: function () {
    this.msg = location.href;
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.button-wrapper {
    display: block;
    height: 40px;
    width: 100%;
}
.left {
    float: left;
}
.green {
    background: #70e0a0;
}
.green:hover {
    background: #5abf85;
}
.button {
    color: #FFF;
    padding: 0 10px;
    cursor: pointer;
    line-height: 26px;
    text-align: center;
    border-radius: 3px;
    margin: 5px 0 0 5px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>