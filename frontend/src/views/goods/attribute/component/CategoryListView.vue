<template>
  <div class="CategoryListView">
    <el-row :gutter="3" class="list-operation">
      <el-col :span="8" :xs="12">
        <div class="grid-content bg-purple">
          <el-input v-model="key_world" placeholder="搜索分类,描述" clearable style="width: 350px"></el-input>
          <el-button type="primary" plain @click="searchCate">搜索</el-button>
        </div>
      </el-col>
      <el-col :span="2" :xs="6">
        <div class="grid-content bg-purple">
          <el-button type="success" plain @click="multipleEnabled(1)">批量开启</el-button>
        </div>
      </el-col>
      <el-col :span="2" :xs="6">
        <div class="grid-content bg-purple">
          <el-button type="warning" plain @click="multipleEnabled(0)">批量关闭</el-button>
        </div>
      </el-col>
      <el-col :span="3" :xs="6">
        <div class="grid-content bg-purple">
          <el-button type="danger" @click="multipleDel">批量删除</el-button>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-table
        ref="multipleTable"
        :data="CategoryList"
        border
        style="width: 100%"
        @selection-change="handleSelectionChange"
      >
        <el-table-column
          type="selection"
          align="center"
          width="50"
        >
        </el-table-column>
        <el-table-column
          type="index"
          label="序号"
          width="50"
          header-align="center"
          align="center"
        >
        </el-table-column>
        <el-table-column
          prop="name"
          label="分类名"
          header-align="center"
          align="center"
          width="150"
        >
        </el-table-column>
        <el-table-column
          prop="icon_url"
          label="分类图片"
          align="center"
          header-align="center"
          width="200"
        >
          <template slot-scope="scope">
            <el-image style="width: 100px; height: 100px" :src="scope.row.icon_url" fit="cover"></el-image>
          </template>
        </el-table-column>
        <el-table-column
          prop="front_desc"
          label="描述"
          header-align="center"
        >
        </el-table-column>
        <el-table-column
          prop="sort_order"
          label="排序权重"
          header-align="center"
          align="center"
          width="150"
          sortable
        >
        </el-table-column>
        <el-table-column
          prop="enabled"
          label="开启"
          header-align="center"
          align="center"
          width="150"
          sortable
        >
          <template slot-scope="scope">
            <el-switch
              v-model="scope.row.enabled"
              :active-value="1"
              :inactive-value="0"
              active-color="#13ce66"
              inactive-color="#C0C4CC"
              @change="switchChange($event, scope.row)"
            >
            </el-switch>
          </template>
        </el-table-column>
        <el-table-column
          label="操作"
          header-align="center"
          align="center"
          width="200"
        >
          <template slot-scope="scope">
            <el-button
              size="mini"
              @click="handleEdit(scope.$index, scope.row)"
            >
              编辑
            </el-button>
            <el-button
              size="mini"
              type="danger"
              @click="handleDel(scope.$index, scope.row)"
            >
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
    <el-row class="pagination">
      <el-pagination
        background
        :page-sizes="[10, 20, 30, 40, 50]"
        :page-size="10"
        :current-page="page"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
      >
      </el-pagination>
    </el-row>
  </div>
</template>

<script>
  import {
    getCategoryList,
    delCategory,
    enabledCategory,
    searchCategoryList
  } from '@/api/goods'

  export default {
    name: 'CategoryListView',
    data() {
      return {
        CategoryList: [],
        total: 0,
        page: 1,
        page_size: 10,
        key_world: '', // 搜索key
        multipleSelection: [] // 多选
      }
    },
    filter: {},
    computed: {},
    mounted() {
      // 初始化查询
      this.queryApiCateList(this.page, this.page_size)
    },
    methods: {
      handleEdit(index, row) {
        // 编辑
        this.$emit('editCate', row.id)
      },
      handleDel(index, row) {
        // 删除
        this.$confirm('此操作将删除此分类是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
          center: true
        }).then(() => {
          delCategory({ ids: [row.id] }).then(res => {
            this.$message({
              type: 'success',
              message: res.message
            })
            // 重新加载列表
            this.queryApiCateList(this.page, this.page_size)
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })
      },
      queryApiCateList(page, page_size) {
        // 查询分类
        getCategoryList({ page, page_size }).then(res => {
          this.CategoryList = res.data.items
          this.total = res.data.total
        })
      },
      searchApiCategoryList(key_world, page, page_size) {
        // 搜索分类
        searchCategoryList({ key_world, page, page_size }).then(res => {
          this.$message.success(res.message)
          this.CategoryList = res.data.items
          this.total = res.data.total
        })
      },
      handleSizeChange(page_size) {
        // 处理切换每页长度
        this.page_size = page_size
        if (this.key_world) {
          this.searchApiCategoryList(this.key_world, this.page, this.page_size)
        } else {
          this.queryApiCateList(this.page, this.page_size)
        }
      },
      handleCurrentChange(page) {
        // 切换分页
        this.page = page
        if (this.key_world) {
          // 有搜索关键字就按搜索查询下一页
          this.searchApiCategoryList(this.key_world, this.page, this.page_size)
        } else {
          // 没有搜索关键词就默认全部
          this.queryApiCateList(this.page, this.page_size)
        }
      },
      handleSelectionChange(val) {
        // 批量操作
        this.multipleSelection = val
      },
      enableCate(ids, enabled) {
        enabledCategory({ ids, enabled }).then(res => {
          this.$message.success(res.message)
        })
      },
      switchChange(enabled, val) {
        // 切换enabled状态
        this.enableCate([val.id], enabled)
      },
      searchCate() {
        // 搜索 默认第一页
        this.page = 1
        this.searchApiCategoryList(this.key_world, this.page, this.page_size)
      },
      multipleEnabled(enabled) {
        const checkedLen = this.multipleSelection.length
        if (checkedLen <= 0) {
          this.$message.info('选择的条数过少')
          return
        }
        let message_tip = ''
        if (enabled === 1) {
          message_tip = '开启'
        } else {
          message_tip = '关闭'
        }
        this.$confirm(`此操作将批量${message_tip}${checkedLen}条数据, 是否继续?`, message_tip, {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          const ids = this.getCheckIds()
          enabledCategory({ ids, enabled }).then(res => {
            this.$message.success(res.message)
          })
          // 重新加载列表
          this.queryApiCateList(this.page, this.page_size)
        }).catch(() => {
          this.$message({
            type: 'info',
            message: `已取消${message_tip}`
          })
        })
      },
      multipleDel() {
        const checkedLen = this.multipleSelection.length
        if (checkedLen <= 0) {
          this.$message.info('选择的条数过少')
          return
        }
        this.$confirm(`此操作将批量删除${checkedLen}条数据, 是否继续?`, '批量删除', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'error'
        }).then(() => {
          const ids = this.getCheckIds()
          delCategory({ ids }).then(res => {
            this.$message({
              type: 'success',
              message: res.message
            })
            // 重新加载列表
            this.queryApiCateList(this.page, this.page_size)
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })
      },
      getCheckIds() {
        // 获取选择对象中的id列表(感觉这个写法不够优雅，暂时没想到其他写法)
        const ids = []
        for (const i of this.multipleSelection) {
          ids.push(i.id)
        }
        return ids
      }
    }
  }
</script>

<style scoped>
  .list-operation {
    margin: 15px 0;
  }

  .pagination {
    margin-top: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .grid-content {
    display: flex;
    justify-content: space-around;
  }

</style>
