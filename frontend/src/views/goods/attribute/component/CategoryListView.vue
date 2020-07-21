<template>
  <div class="CategoryListView">
    <el-row gutter="10" class="list-operation">
      <el-col :span="6">
        <!-- TODO(待完善) -->
        <div class="grid-content bg-purple">
          <el-button type="warning" plain>批量开启</el-button>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple">
          <el-button type="danger">批量删除</el-button>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple">
          <el-button type="warning" plain>批量开启</el-button>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple">
          <el-button type="danger">批量删除</el-button>
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
          label="排序"
          header-align="center"
          align="center"
          width="150"
        >
        </el-table-column>
        <el-table-column
          prop="enabled"
          label="开启"
          header-align="center"
          align="center"
          width="150"
        >
          <template slot-scope="scope">
            <el-switch
              v-model="scope.row.enabled"
              :active-value="1"
              :inactive-value="0"
              active-color="#13ce66"
              inactive-color="#C0C4CC"
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
  import { getCategoryList, delCategory } from '@/api/goods'

  export default {
    name: 'CategoryListView',
    data() {
      return {
        CategoryList: [],
        total: 0,
        page: 1,
        page_size: 10,
        // 多选
        multipleSelection: []
      }
    },
    filter: {},
    computed: {},
    mounted() {
      this.queryCateList(this.page, this.page_size)
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
            this.queryCateList(this.page, this.page_size)
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })
      },
      queryCateList(page, page_size) {
        // 查询分类
        getCategoryList({ page, page_size }).then(res => {
          this.CategoryList = res.data.items
          this.total = res.data.total
        })
      },
      handleSizeChange(page_size) {
        this.page_size = page_size
        this.queryCateList(this.page, this.page_size)
      },
      handleCurrentChange(page) {
        this.page = page
        this.queryCateList(this.page, this.page_size)
      },
      handleSelectionChange(val) {
        // 批量操作
        this.multipleSelection = val
      }
    }
  }
</script>

<style scoped>
  .list-operation {
    margin: 15px 0;
    /*display: flex;*/
  }
  .pagination {
    margin-top: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

</style>
