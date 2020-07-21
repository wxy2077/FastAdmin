<template>
  <div class="container">
    <div class="box-wrapper">
      <el-tabs v-model="activeName" class="tab-box">
        <el-tab-pane label="商品分类" name="first">
          <div v-if="showCategoryList" class="PageList">
            <el-button type="primary" @click="switchView">
              新增分类
            </el-button>
            <category-list-view @editCate="editCate" />
          </div>
          <div v-if="!showCategoryList" class="add-category">
            <el-button type="primary" @click="switchView">
              返回列表
            </el-button>
            <category-view :modify-cate-id="modifyCateId" />
          </div>
        </el-tab-pane>
        <el-tab-pane label="商品规格" name="third">
          <h1>ccc</h1>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
  import CategoryListView from './component/CategoryListView'
  import CategoryView from './component/CategoryView'

  export default {
    name: 'Index',
    components: {
      CategoryListView,
      CategoryView
    },
    data() {
      return {
        activeName: 'first',
        showCategoryList: true,
        modifyCateId: null
      }
    },
    methods: {
      switchView() {
        this.showCategoryList = !this.showCategoryList
        this.modifyCateId = null
      },
      editCate(cate_id) {
        this.modifyCateId = cate_id
        this.showCategoryList = !this.showCategoryList
      }
    }
  }
</script>

<style lang="scss" scoped>
  .container {
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
