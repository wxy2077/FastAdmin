<template>
  <div class="dashboard-container">
    <div class="mid">
      <el-row :gutter="32">
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
  </div>
</template>

<script>
import RadarChart from './component/RadarChart'
import HistogramChart from './component/HistogramChart'
import PieChart from './component/PieChart'
export default {
  name: 'Dashboard',
  components: {
    RadarChart,
    HistogramChart,
    PieChart
  },
  data() {
    return {
    }
  }

}
</script>

<style lang="scss" scoped>
  .dashboard-container{
    margin: 30px 0 0 0;
    padding-top: 0;
    .mid{
      width: 100%;
      height: 380px;
      .chart-wrapper {
        height: 340px;
        padding: 16px 16px 0;
        margin-bottom: 32px;
      }
    }
  }
</style>
