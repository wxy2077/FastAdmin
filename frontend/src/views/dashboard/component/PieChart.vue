<template>
  <div :class="className" :style="{height,width}"></div>
</template>

<script>
  import echarts from 'echarts'

  // require('echarts/theme/macarons') // echarts theme

  export default {
    name: 'PieChart',
    props: {
      className: {
        type: String,
        default: 'chart'
      },
      width: {
        type: String,
        default: '100%'
      },
      height: {
        type: String,
        default: '300px'
      }
    },
    data() {
      return {
        chart: null
      }
    },
    mounted() {
      this.initChart()
    },
    // 每次销毁前清空
    beforeDestroy() {
      if (!this.chart) {
        return
      }
      this.chart.dispose()
      this.chart = null
    },
    methods: {
      initChart() {
        this.chart = echarts.init(this.$el, 'light')
        this.chart.setOption({
          title: {
            text: '访问来源',
            left: 'center'
          },
          tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
          },
          legend: {
            orient: 'vertical',
            left: 'left',
            data: ['PC', '微信小程序', '安卓App', 'IOS']
          },
          series: [
            {
              name: '访问来源',
              type: 'pie',
              radius: '55%',
              center: ['50%', '60%'],
              data: [
                { value: 335, name: 'PC' },
                { value: 310, name: '微信小程序' },
                { value: 234, name: '安卓App' },
                { value: 135, name: 'IOS' }
              ],
              emphasis: {
                itemStyle: {
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
              }
            }
          ]
        })
      }
    }
  }
</script>

<style scoped>

</style>
