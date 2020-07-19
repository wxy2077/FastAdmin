<template>
  <div class="dashboard-container">
    <div class="base-info">
      <el-row :gutter="8">
        <el-col :lg="6" :md="12" :xs="24">
          <div class="chart-wrapper">
            <card-view />
          </div>
        </el-col>
        <el-col :lg="6" :md="12" :xs="24">
          <div class="chart-wrapper">
            <card-view />
          </div>
        </el-col>
        <el-col :lg="6" :md="12" :xs="24">
          <div class="chart-wrapper">
            <card-view />
          </div>
        </el-col>
        <el-col :lg="6" :md="12" :xs="24">
          <div class="chart-wrapper">
            <card-view />
          </div>
        </el-col>
      </el-row>
    </div>

    <div class="mid">
      <el-row :gutter="10">
        <el-col :xs="24" :sm="24" :lg="8">
          <div class="chart-wrapper">
            <pie-chart />
          </div>
        </el-col>
        <el-col :xs="24" :sm="24" :lg="8">
          <div class="chart-wrapper">
            <histogram-chart />
          </div>
        </el-col>
        <el-col :xs="24" :sm="24" :lg="8">
          <div class="chart-wrapper">
            <radar-chart />
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="bottom">
      <el-row :gutter="10">
        <el-col :xs="24" :sm="24" :lg="24">
          <div class="chart-wrapper">
            <line-chart />
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
  import RadarChart from './component/RadarChart'
  import HistogramChart from './component/HistogramChart'
  import PieChart from './component/PieChart'
  import CardView from './component/CardView'
  import LineChart from './component/LineChart'

  export default {
    name: 'Dashboard',
    components: {
      RadarChart,
      HistogramChart,
      PieChart,
      CardView,
      LineChart
    },
    data() {
      return {}
    }

  }
</script>

<style lang="scss" scoped>
  .dashboard-container {
    padding: 20px;
    height: 100%;
    background-color: rgb(240, 242, 245);
    .mid {
      width: 100%;
      height: 380px;
      .chart-wrapper {
        height: 340px;
        background-color: #fff;
        padding: 10px 10px 0;
        margin-bottom: 10px;
        border-radius: 5px;
      }
    }
    .base-info {
      width: 100%;
    }
    .bottom{
      background-color: #FFF;
      padding: 20px;
      height: 550px;
      margin-bottom: 20px;
    }
  }
</style>
