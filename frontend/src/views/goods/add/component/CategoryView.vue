<template>
  <div class="category">
    <el-form ref="form" :rules="rules" :model="form" label-width="100px">
      <el-form-item label="分类名称:" required>
        <el-input v-model="form.name" style="width: 300px"></el-input>
      </el-form-item>

      <el-form-item label="分类简介:">
        <el-input v-model="form.front_desc" type="textarea" style="width: 300px"></el-input>
      </el-form-item>

      <el-form-item label="分类图片" required>
        <el-upload
          action="http://127.0.0.1:8010/api/mall/v1/admin/utils/upload/file/"
          :headers="headers"
          list-type="picture-card"
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
        <el-switch
          v-model="defaultSwitch"
          active-color="#13ce66"
          inactive-color="#E4E7ED"
          @change="changeEnable"
        >
        </el-switch>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm('form')">立即创建</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  import { addCategory } from '@/api/goods'
  import { getToken } from '@/utils/auth'
  export default {
    name: 'CategoryView',
    data() {
      return {
        form: {
          name: '',
          front_desc: '',
          icon_url: '',
          sort_order: 1,
          enabled: 1
        },
        defaultSwitch: true,
        rules: {
          name: [
            { required: true, message: '请输入分类名称', trigger: 'blur' },
            { min: 3, max: 5, message: '长度在1到5个字符', trigger: 'blur' }
          ]
        }
      }
    },
    computed: {
      headers() {
        return {
          'token': getToken() // 从本地获取token就行
        }
      }
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
      changeEnable() {
        if (this.defaultSwitch) {
          this.form.enabled = 1
        } else {
          this.form.enabled = 0
        }
      },
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            addCategory(this.form).then((res) => {
              this.$message({
                message: '创建成功',
                type: 'success'
              })
            })
          } else {
            return false
          }
        })
      }
    }
  }
</script>

<style scoped>

</style>
