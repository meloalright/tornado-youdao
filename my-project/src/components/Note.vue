<template>
  <div class="root">
    <div class="top-line clearfix">
      <div class="save-statement" v-on:click="putModified()">{{save.statement}}</div>
    </div>
    <div class="line"></div>
    <input class="youdao-title" v-model="title"/>
    <div class="line"></div>
    <div class="note-wrapper">
      <textarea v-model="note" class="youdao-note"></textarea>
    </div>
  </div>
</template>

<script>
export default {
  name: 'note',
  data () {
    return {
      save: {
        statement: '保存'
      },
      title: '无笔记标题',
      note: '1.我的笔记主要内容\n\n2...',
      ws: null
    }
  },
  methods: {
    /*
     * @
     * @ 获取heartbeat
     * @
     **/
    heartbeat: function () {
      fetch('http://localhost:8002/api/heartbeat/').then((res) => {
        return res.json()
      }).then((data) => {
        console.log(data);
      })
    },

    /*
     * @
     * @ 提交更改
     * @
     **/
    putModified: function () {
      this.ws.send(this.note);
    },

    /*
     * @
     * @ init
     * @
     **/
     init: function () {
      var ws = new WebSocket("ws://localhost:8002/api/ws/echo/");
      ws.onopen = function() {
         ws.send("Hello, world");
      };
      ws.onmessage = function (evt) {
         alert(evt.data);
      };
      this.ws = ws;
     }
  },
  beforeMount: function () {
    this.init();
    //
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/**
 * @
 * @ youdao
 * @
 **/
.clearfix:after{content:".";display:block;height:0;clear:both;visibility:hidden}
.clearfix{*+height:1%;}

.root .top-line {
  height: 50px;
  display: block;
}
.root .top-line .save-statement {
  margin: 10px 20px 0 10px;
  border: solid 1px #EEE;
  display: inline-block;
  border-radius: 6px;
  line-height: 30px;
  cursor: pointer;
  padding: 0 10px;
  float: right;
  color: #777;
}

.root .line {
  height: 1px;
  border: none;
  display: block;
  background-color: #EEE;
}

.root .youdao-title {
  text-align: center;
  margin: 10px auto;
  line-height: 30px;
  font-size: 30px;
  color: #2c3e50;
  outline: none;
  border: none;
}

.root .note-wrapper {
  display: block;
}


.root .note-wrapper .youdao-note {
  width: 100%;
  border: none;
  resize: none;
  margin: auto;
  height: 900px;
  outline: none;
  display: block;
  color: #2c3e50;
  padding: 0px 0;
  font-size: 14px;
  padding: 10px 0;
  text-align: center;
}





h1, h2 {
  font-weight: normal;
  line-height: 16px;
  font-size: 16px;
  margin: 10px 0;
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
