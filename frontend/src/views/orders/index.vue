<template>
  <div class="orders-container">
    <el-tabs v-model="activeName" class="tab-box">
      <el-tab-pane label="待付款" name="first">待付款</el-tab-pane>
      <el-tab-pane label="待发货" name="second">待发货</el-tab-pane>
      <el-tab-pane label="待收货" name="third">待收货</el-tab-pane>
      <el-tab-pane label="已收获" name="fourth">已收获</el-tab-pane>
      <el-tab-pane label="已关闭" name="five">已关闭</el-tab-pane>
      <el-tab-pane label="全部订单" name="sex">全部订单</el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
  export default {
    name: 'Index',
    data() {
      return {
        activeName: 'first'
      }
    }
  }
</script>

<style lang="scss" scoped>
  .orders-container{
    padding: 33px;
    width: 100%;
    height: 100vh;
    background-color: rgb(240, 242, 245);
    .tab-box{
      background-color: #fff;
      padding: 10px;
    }
  }

</style>
