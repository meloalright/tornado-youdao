<template>
  <div class="root">
    <div class="header-wrapper">
      <input class="share-input" v-model="msg" id="shareInput" />
      <p class="close" v-on:click="close()">x</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Head',
  data () {
    return {
      msg: 'tornado-youdao'
    }
  },
  methods: {
    share: function () {
      var shareInput = document.getElementById('shareInput');
      var len = shareInput.value;
      shareInput.selectionStart = 0;
      shareInput.selectionEnd = len;
    },
    close: function () {
      window.location.href = "#/note/";
    },
    init: function () {
      this.msg = location.href;
    }
  },
  beforeMount: function () {
    this.init();
  },
  mounted: function () {
    this.share();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.header-wrapper {
  color: #FFF;
  height: 40px;
  position: relative;
  text-align: center;
  background: #70e0a0;
}

.header-wrapper .share-input {
  background: rgba(256, 256, 256, 0.3);
  margin: -12px 0 0 -300px;
  position: absolute;
  text-align: center;
  line-height: 24px;
  font-size: 14px;
  display: block;
  outline: none;
  width: 600px;
  border: none;
  color: #FFF;
  left: 50%;
  top: 50%;
}

.header-wrapper .close {
  position: absolute;
  line-height: 24px;
  cursor: pointer;
  font-size: 24px;
  height: 24px;
  right: 20px;
  margin: 0;
  top: 8px;
}

.header-wrapper .close:hover {
  font-weight: bolder;
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