<template>
  <div class="container">
    <div class="box-wrapper">
      <div v-if="showGoodsList" class="PageList">
        <el-button type="primary" @click="switchView">
          新增商品
        </el-button>
        <goods-list-view />
      </div>
      <div v-if="!showGoodsList" class="add-category">
        <el-button type="primary" @click="switchView">
          返回列表
        </el-button>
        <goods-view />
      </div>
    </div>
  </div>
</template>

<script>
  import GoodsView from './component/GoodsView'
  import GoodsListView from './component/GoodsListView'
  export default {
    name: 'Index',
    components: {
      GoodsListView,
      GoodsView
    },
    data() {
      return {
        showGoodsList: true,
        modifyGoodsId: null
      }
    },
    methods: {
      switchView() {
        this.showGoodsList = !this.showGoodsList
        this.modifyGoodsId = null
      }
    }
  }
</script>

<style lang="scss" scoped>
  .container{
    padding: 20px;
    min-height: 100vh;
    background-color: rgb(240, 242, 245);
    .box-wrapper {
      background-color: #fff;
      border-radius: 3px;
      padding: 20px;
    }
  }

</style>
