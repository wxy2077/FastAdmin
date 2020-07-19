<template>
  <div class="add-container">
    <div class="box-wrapper">
      <el-tabs v-model="activeName" class="tab-box">
        <el-tab-pane label="添加商品" name="first">
          <goods-view />
        </el-tab-pane>
        <el-tab-pane label="添加分类" name="second">
          <category-view />
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
  import GoodsView from './component/GoodsView'
  import CategoryView from './component/CategoryView'
  export default {
    name: 'Index',
    components: {
      GoodsView,
      CategoryView
    },
    data() {
      return {
        activeName: 'first'
      }
    }
  }
</script>

<style lang="scss" scoped>
  .add-container {
    padding: 20px;
    height: 100vh;
    background-color: rgb(240, 242, 245);
    .box-wrapper{
      background-color: #fff;
      border-radius: 3px;
      padding: 20px;
    }
  }

</style>
