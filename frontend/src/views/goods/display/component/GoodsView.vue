<template>
  <div class="GoodsView">
    <el-row>
      <el-form ref="form" :model="form" label-width="100px">
        <el-form-item label="商品名称" required style="width: 500px">
          <el-input
            v-model="form.goods_name"
            placeholder="请输入内容"
            clearable
          >
          </el-input>
        </el-form-item>
        <el-form-item label="商品简介:" required style="width: 500px">
          <el-input v-model="form.goods_brief" type="textarea" clearable></el-input>
        </el-form-item>
        <el-form-item label="商品分类:" required style="width: 500px">
          <el-select
            v-model="form.category_id"
            filterable
            clearable
            placeholder="选择分类"
            style="width: 300px"
            :value="form.category_id"
          >
            <el-option
              v-for="item in cateList"
              :key="item.id"
              :label="item.name"
              :value="item.id"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="封面图:">
          <el-upload
            name="file"
            :action="actionUrl"
            :headers="headers"
            :file-list="picBannerArr"
            :limit="1"
            :on-success="handleImgSuccess"
            list-type="picture-card"
          >
            <el-button size="small" type="primary">点击上传</el-button>
            <div slot="tip" class="el-upload__tip">限制最多上传一张,不传默认取轮播图第一张,只能上传jpg/png文件，且不超过500kb</div>
          </el-upload>
        </el-form-item>

        <el-form-item label="轮播图:" required>
          <el-upload
            name="file"
            :action="actionUrl"
            :headers="headers"
            :file-list="picList"
            :limit="10"
            :on-success="handleListImgSuccess"
            :on-remove="handleListImgRemove"
            list-type="picture-card"
          >
            <el-button size="small" type="primary">点击上传</el-button>
            <div slot="tip" class="el-upload__tip">限制最少2张图，最多10张,只能上传jpg/png文件，且不超过500kb</div>
          </el-upload>
        </el-form-item>

        <el-form-item label="商品单位" style="width: 500px">
          <el-input v-model="form.goods_unit"></el-input>
          <div class="form-tip">如：件、包、袋等</div>
        </el-form-item>
        <el-form-item label="是否售卖:">
          <el-switch
            v-model="form.is_on_sale"
            :active-value="1"
            :inactive-value="0"
            active-color="#13ce66"
            inactive-color="#E4E7ED"
          >
          </el-switch>
        </el-form-item>
        <el-form-item label="销量">
          <el-input-number v-model="form.sell_volume" :min="0" label="描述文字"></el-input-number>
        </el-form-item>
        <el-form-item label="商品详情" required>
          <el-radio v-model="form.goods_desc_type" :label="1">富文本编辑器</el-radio>
          <el-radio v-model="form.goods_desc_type" :label="2">MarkDown编辑器</el-radio>
          <Tinymce v-show="form.goods_desc_type===1" ref="editor" v-model="form.goods_desc" :height="400" @input="TinInput" />
          <mavon-editor v-show="form.goods_desc_type===2" v-model="form.goods_desc" :ishljs="true" code-style="atom-one-dark" />
        </el-form-item>
      </el-form>
    </el-row>
  </div>
</template>

<script>
  import { getToken } from '@/utils/auth'
  import { commonSetting } from '@/utils/common'
  import Tinymce from '@/components/Tinymce'

  export default {
    name: 'GoodsView',
    components: {
      Tinymce
    },
    data() {
      return {
        form: {
          goods_name: '',
          goods_brief: '',
          category_id: '',
          pic_banner: '',
          list_pic_url: [],
          goods_unit: '',
          is_on_sale: 1,
          sell_volume: 0, // 销量
          goods_desc_type: 2, // 商品详情格式1=富文本 2=MarkDown
          goods_desc: '' // 商品详情
        },
        rules: {},
        cateList: [
          { id: 1, name: '居家' },
          { id: 2, name: '生活' }
        ],
        actionUrl: commonSetting.uploadUrl
      }
    },
    computed: {
      headers() {
        // 上传图片添加请求头header
        return {
          'token': getToken() // 从本地获取token就行
        }
      },
      picBannerArr() {
        // 上传图片 显示默认图片
        return this.form.pic_banner ? [{ url: this.form.pic_banner }] : []
      },
      picList() {
        if (this.form.list_pic_url) {
          const temp_list = []
          this.form.list_pic_url.forEach(pic => {
            temp_list.push({ url: pic })
          })
          return temp_list
        } else {
          return []
        }
      }
    },
    methods: {
      handleImgSuccess(res, file) {
        // 处理上传图标
        if (res.code === 200) {
          this.form.pic_banner = res.data.image
          this.$message.success(`图片上传成功`)
        } else {
          this.$message.error(`图片上传失败:${res.message}`)
        }
      },
      handleListImgSuccess(res, file) {
        // 处理上传图标
        if (res.code === 200) {
          this.form.list_pic_url.push(res.data.image)
          this.$message.success(`图片上传成功`)
        } else {
          this.$message.error(`图片上传失败:${res.message}`)
        }
      },
      handleListImgRemove(file, fileList) {
        console.log(file, fileList)
      },
      TinInput(v) {
        this.form.goods_desc = v
        console.log('接收到到值', v)
      }
    }
  }
</script>

<style lang="scss" scoped>
  .GoodsView {
    margin-top: 10px;
  }

  .form-tip {
    color: #888;
    font-size: 12px;
    line-height: 30px;
  }

</style>
