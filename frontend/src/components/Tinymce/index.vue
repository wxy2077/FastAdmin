<template>
  <div :class="{fullscreen:fullscreen}" class="tinymce-container" :style="{width:containerWidth}">
    <textarea :id="tinymceId" class="tinymce-textarea" @change="onPaste"></textarea>
    <div class="editor-custom-btn-container">
      <editorImage color="#1890ff" class="editor-upload-btn" @successCBK="imageSuccessCBK" />
    </div>
  </div>
</template>

<script>
  /**
   * docs:
   * https://panjiachen.github.io/vue-element-admin-site/feature/component/rich-editor.html#tinymce
   */
  import editorImage from './components/EditorImage'
  import plugins from './plugins'
  import toolbar from './toolbar'
  import load from './dynamicLoadScript'

  // why use this cdn, detail see https://github.com/PanJiaChen/tinymce-all-in-one
  const tinymceCDN = 'https://cdn.jsdelivr.net/npm/tinymce-all-in-one@4.9.3/tinymce.min.js'

  import { UpLoadImg } from '@/api/utils'
  export default {
    name: 'Tinymce',
    components: { editorImage },
    props: {
      id: {
        type: String,
        default: function() {
          return 'vue-tinymce-' + +new Date() + ((Math.random() * 1000).toFixed(0) + '')
        }
      },
      value: {
        type: String,
        default: ''
      },
      toolbar: {
        type: Array,
        required: false,
        default() {
          return []
        }
      },
      menubar: {
        type: String,
        default: 'file edit insert view format table'
      },
      height: {
        type: [Number, String],
        required: false,
        default: 360
      },
      width: {
        type: [Number, String],
        required: false,
        default: 'auto'
      },
      languageType: {
        type: String,
        required: false,
        default: 'zh'
      }
    },
    data() {
      return {
        hasChange: false,
        hasInit: false,
        tinymceId: this.id,
        fullscreen: false,
        languageTypeList: {
          'en': 'en',
          'zh': 'zh_CN',
          'es': 'es_MX',
          'ja': 'ja'
        }
      }
    },
    computed: {
      containerWidth() {
        const width = this.width
        if (/^[\d]+(\.[\d]+)?$/.test(width)) { // matches `100`, `'100'`
          return `${width}px`
        }
        return width
      }
    },
    watch: {
      value(val) {
        // 正则去掉base64编码到图片
        // val = val.replace(/<p><img\s?src="data.*?<\/p>/g, '')
        console.log('内容', val)
        if (!this.hasChange && this.hasInit) {
          this.$nextTick(() =>
            window.tinymce.get(this.tinymceId).setContent(val || ''))
        }
      }
    },
    mounted() {
      this.init()
    },
    activated() {
      if (window.tinymce) {
        this.initTinymce()
      }
    },
    deactivated() {
      this.destroyTinymce()
    },
    destroyed() {
      this.destroyTinymce()
    },
    methods: {
      init() {
        // dynamic load tinymce from cdn
        load(tinymceCDN, (err) => {
          if (err) {
            this.$message.error(err.message)
            return
          }
          this.initTinymce()
        })
      },
      initTinymce() {
        const _this = this
        window.tinymce.init({
          selector: `#${this.tinymceId}`, // 绑定输入框
          language: this.languageTypeList[this.languageType], // 选择语言
          height: this.height, // 高度
          body_class: 'panel-body ',
          object_resizing: false,
          toolbar: this.toolbar.length > 0 ? this.toolbar : toolbar, // 头部导航栏
          menubar: this.menubar, // 菜单
          plugins: plugins, // 插件
          end_container_on_empty_block: true,
          powerpaste_word_import: 'clean',
          code_dialog_height: 450, // 插入代码对话框
          code_dialog_width: 1000,
          advlist_bullet_styles: 'square',
          advlist_number_styles: 'default',
          default_link_target: '_blank',
          paste_data_images: false, // 粘贴图片
          link_title: false,
          nonbreaking_force_tab: true, // inserting nonbreaking space &nbsp; need Nonbreaking Space Plugin
          init_instance_callback: editor => {
            if (_this.value) {
              editor.setContent(_this.value)
            }
            _this.hasInit = true
            editor.on('NodeChange Change KeyUp SetContent', () => {
              this.hasChange = true
              // const val = editor.getContent().replace(/<p><img\s?src="data.*?<\/p>/g, '')
              this.$emit('input', editor.getContent())
            })
            editor.on('paste', (evt) => {
              // 监听粘贴事件
              this.onPaste(evt)
            })
          },
          setup(editor) {
            editor.on('FullscreenStateChanged', (e) => {
              _this.fullscreen = e.state
            })
          },
          // it will try to keep these URLs intact
          // https://www.tiny.cloud/docs-3x/reference/configuration/Configuration3x@convert_urls/
          // https://stackoverflow.com/questions/5196205/disable-tinymce-absolute-to-relative-url-conversions
          convert_urls: false
        })
      },
      destroyTinymce() {
        const tinymce = window.tinymce.get(this.tinymceId)
        if (this.fullscreen) {
          tinymce.execCommand('mceFullScreen')
        }

        if (tinymce) {
          tinymce.destroy()
        }
      },
      setContent(value) {
        window.tinymce.get(this.tinymceId).setContent(value)
      },
      getContent() {
        window.tinymce.get(this.tinymceId).getContent()
      },
      imageSuccessCBK(arr) {
        // 添加按钮上传图片
        arr.forEach(v => window.tinymce.get(this.tinymceId).insertContent(`<img class="wscnph" src="${v.url}" >`))
      },
      onPaste(event) {
        // 实现图片粘贴上传
        const items = (event.clipboardData || window.clipboardData).items
        // 搜索剪切板items 全部的选项
        // for (let i = 0; i < items.length; i++) {
        //   if (items[i].type.indexOf('image') !== -1) {
        //     console.log('粘贴的是图片')
        //     const file = items[i].getAsFile()
        //     const formData = new FormData()
        //     formData.append('file', file)
        //     UpLoadImg(formData).then(res => {
        //       console.log(res)
        //       if (res.code === 200) {
        //         window.tinymce.get(this.tinymceId).insertContent(`<img class="wscnph" src="${res.data.image}" >`)
        //       } else {
        //         this.$message.error('上传失败,联系管理员')
        //       }
        //     })
        //     break
        //   } else {
        //     console.log('粘贴的-不-是-图片')
        //   }
        // }
        // 搜索剪切板items 只取第一张
        if (items[0].type.indexOf('image') !== -1) {
          console.log('粘贴的是图片类型')
          const file = items[0].getAsFile()
          const formData = new FormData()
          formData.append('file', file)
          UpLoadImg(formData).then(res => {
            console.log(res)
            if (res.code === 200) {
              // 放到内容当中
              window.tinymce.get(this.tinymceId).insertContent(`<img class="wscnph" src="${res.data.image}" >`)
            } else {
              this.$message.error('上传失败,联系开发人员')
            }
          })
        } else {
          console.log('粘贴的不是图片，不能上传')
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
  .tinymce-container {
    position: relative;
    line-height: normal;
  }

  .tinymce-container {
    ::v-deep {
      .mce-fullscreen {
        z-index: 10000;
      }
    }
  }

  .tinymce-textarea {
    visibility: hidden;
    z-index: -1;
  }

  .editor-custom-btn-container {
    position: absolute;
    right: 4px;
    top: 4px;
    /*z-index: 2005;*/
  }

  .fullscreen .editor-custom-btn-container {
    z-index: 10000;
    position: fixed;
  }

  .editor-upload-btn {
    display: inline-block;
  }
</style>
