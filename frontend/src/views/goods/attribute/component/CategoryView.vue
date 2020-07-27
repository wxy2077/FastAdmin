<template>
  <div class="category">
    <h3 v-if="modifyCateId">修改分类</h3>
    <h3 v-else>新增分类</h3>
    <el-form ref="form" :rules="rules" :model="form" label-width="100px">
      <el-form-item label="分类名称:" required prop="name">
        <el-input v-model="form.name" style="width: 300px" clearable></el-input>
      </el-form-item>

      <el-form-item label="分类简介:" prop="front_desc">
        <el-input v-model="form.front_desc" type="textarea" style="width: 500px" clearable></el-input>
      </el-form-item>

      <el-form-item label="分类图片" required>
        <el-upload
          action="http://127.0.0.1:8010/api/mall/v1/admin/utils/upload/file/"
          :headers="headers"
          list-type="picture-card"
          :file-list="fileArr"
          :limit="1"
          :on-success="handleAvatarSuccess"
        >
          <i class="el-icon-plus"></i>
          <div slot="tip" class="el-upload__tip">限制上传一张, 只能上传jpg/png文件，且不超过500kb</div>
        </el-upload>
      </el-form-item>
      <el-form-item label="排序">
        <el-input-number v-model="form.sort_order" :min="1" :max="100" label="范围1-100">
        </el-input-number>
      </el-form-item>
      <el-form-item label="开启分类">
        <!-- 使用数字类型1为开 0为关 -->
        <el-switch
          v-model="form.enabled"
          :active-value="1"
          :inactive-value="0"
          active-color="#13ce66"
          inactive-color="#E4E7ED"
        >
        </el-switch>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm('form')">
          <template v-if="modifyCateId">立即修改</template>
          <template v-else>立即创建</template>
        </el-button>
        <el-button type="success" plain @click="resetFrom('form')">重置表单</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  import { addCategory, getCategory, modifyCategory } from '@/api/goods'
  import { getToken } from '@/utils/auth'

  export default {
    name: 'CategoryView',
    props: {
      modifyCateId: {
        type: Number,
        default: null
      }
    },
    data() {
      return {
        form: {
          name: '',
          front_desc: '',
          icon_url: '',
          sort_order: 1,
          enabled: 1
        },
        rules: {
          name: [
            { required: true, message: '请输入分类名称', trigger: 'blur' },
            { min: 1, max: 5, message: '长度限制1到5个字符', trigger: 'blur' }
          ],
          front_desc: [
            { min: 1, max: 30, message: '长度限制1到30个字符', trigger: 'blur' }
          ]
        }
      }
    },
    computed: {
      headers() {
        // 上传图片添加请求头header
        return {
          'token': getToken() // 从本地获取token就行
        }
      },
      fileArr() {
        // 上传图片 显示默认图片
        return this.form.icon_url ? [{ url: this.form.icon_url }] : []
      }
    },
    mounted() {
      this.editInit()
    },
    methods: {
      handleAvatarSuccess(res, file) {
        // 处理上传图标
        if (res.code === 200) {
          this.form.icon_url = res.data.image
        } else {
          this.$message.error(`图片上传失败:${res.message}`)
        }
      },
      submitForm(formName) {
        // 提交表单
        this.$refs[formName].validate((valid) => {
          if (valid) {
            if (this.modifyCateId) {
              // 修改数据
              modifyCategory(this.form).then((res) => {
                this.$message({
                  message: res.message,
                  type: 'success'
                })
              })
            } else {
              // 添加数据
              addCategory(this.form).then((res) => {
                this.$message({
                  message: res.message,
                  type: 'success'
                })
              })
            }
          } else {
            return false
          }
        })
      },
      editInit() {
        // 编辑初始化加载数据
        if (this.modifyCateId) {
          getCategory({ 'cate_id': this.modifyCateId }).then(res => {
            this.form = res.data
          })
        }
      },
      resetFrom(formName) {
        this.$refs[formName].resetFields()
      }
    }
  }
</script>

<style scoped>
  .category {
    margin-top: 10px;
  }

</style>
