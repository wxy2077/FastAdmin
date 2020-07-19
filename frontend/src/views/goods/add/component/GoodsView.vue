<template>
  <div class="goods-container">
    <el-form ref="form" :model="form" label-width="100px">
      <el-form-item label="商品分类:">
        <el-input v-model="form.category" style="width: 140px"></el-input>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  export default {
    name: 'GoodsView',
    data() {
      return {
        form: {
          category: ''
        }
      }
    },
    methods: {
      onSubmit() {
        this.$message('submit!')
      },
      onCancel() {
        this.$message({
          message: 'cancel!',
          type: 'warning'
        })
      }
    }
  }
</script>

<style lang="scss" scoped>
  .goods-container {
    padding: 10px;
  }

</style>
