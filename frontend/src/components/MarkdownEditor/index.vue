<template>
  <div class="index">
    <el-tabs v-model="activeName" type="border-card">
      <el-tab-pane label="编辑" name="first" class="editor-content">
        <div id="textarea-wrapper">
          <textarea id="input-textarea" v-model="content" class="banana-cake"></textarea>
        </div>
        <div class="show-markdwon-content">
          <vue-markdown :source="content"></vue-markdown>
        </div>
      </el-tab-pane>
      <el-tab-pane label="预览" name="second">
        <vue-markdown :source="content"></vue-markdown>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
  import debounce from 'lodash.debounce'
  import { TLN } from '@/utils/textarea-line'
  import VueMarkdown from 'vue-markdown'
  export default {
    name: 'MarkdownEditor',
    components: {
      VueMarkdown // 语法高亮 https://github.com/miaolz123/vue-markdown/issues/21
    },
    data() {
      return {
        activeName: 'first',
        content: '',
        componentKey: 0
      }
    },
    mounted() {
      this.init()
    },
    methods: {
      init() {
        TLN.append_line_numbers('input-textarea')
      },
      forceRerender() {
        this.componentKey += 1
      },
      textChange: debounce(function() {
        // 箭头函数this为 undefined https://github.com/vue-styleguidist/vue-docgen-api/issues/23
         this.forceRerender()
      }, 300)
    }
  }
</script>

<style>
  @import '../../../node_modules/prismjs/themes/prism.css';
  #textarea-wrapper{
    /*border:1px solid grey;*/
    position:relative;
    height:500px;
    width:200px;
    /*margin:15px auto;*/
    margin-left: -15px;
    font-style: normal;
    flex: 1;
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
  }
  #input-textarea{
    letter-spacing:1px;
    font-family: sans-serif;
  }
  .tln-active, .tln-wrapper, .tln-line {
    margin: 0;
    border: 0;
    padding: 0;
    outline: 0;
    box-sizing: border-box;
    vertical-align: middle;
    list-style: none;
  }
  .tln-active {
    display: inline-block;
    padding: 0.625em;
    width: calc(100% - 3em);
    height: 100%;
    font-size: 1em;
    line-height: 1.5;
    font-family: "Roboto Mono", monospace;
    word-break: break-all;
    border-left: 1px solid #aeaeae;
    /*background-color: #fff;*/
    resize: none;
    overflow-wrap: normal;
    overflow-x: auto;
    white-space: pre;
  }
  .tln-wrapper {
    width: 3em;
    padding: 0.6875em 0.3125em 2.1875em;
    height: 100%;
    word-break: break-all;
    overflow: hidden;
    display: inline-block;
    counter-reset: line;
  }
  .tln-line {
    width: 100%;
    display: block;
    text-align: right;
    line-height: 1.5;
    font-size: 1em;
    color: #aeaeae;
  }
  .tln-line::before {
    counter-increment: line;
    content: counter(line);
    font-size: 1em;
    user-select: none;
  }
  .editor-content{
    display: flex;
  }
  .show-markdwon-content{
    flex: 1;
    padding-left: 5px;
    box-shadow: 0 1px 1px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  }

</style>
