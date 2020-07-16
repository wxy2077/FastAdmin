<template>
  <div :class="className" :style="{height,width}"></div>
</template>

<script>
import echarts from 'echarts'

const animationDuration = 3000
export default {
  name: 'RadarChart',
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
          text: '交易状况',
          subtext: '最近三日',
          left: 'right'
        },
        tooltip: {
          trigger: 'item', // axis不显示数据
          axisPointer: { // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        radar: {
          radius: '66%',
          center: ['50%', '42%'],
          splitNumber: 8,
          splitArea: {
            areaStyle: {
              color: 'rgba(255,192,203,.3)',
              opacity: 1,
              shadowBlur: 45,
              shadowColor: 'rgba(0,0,0,.5)',
              shadowOffsetX: 0,
              shadowOffsetY: 15
            }
          },
          indicator: [
            { name: '添加购物车', max: 10000 },
            { name: '下单', max: 10000 },
            { name: '支付', max: 10000 },
            { name: '订单完成', max: 10000 },
            { name: '订单失败', max: 10000 },
            { name: '收藏', max: 10000 }
          ]
        },
        legend: {
          left: 'center',
          bottom: '10',
          data: ['13号', '14号', '今天']
        },
        series: [{
          type: 'radar',
          symbolSize: 0,
          areaStyle: {
            normal: {
              shadowBlur: 13,
              shadowColor: 'rgba(0,0,0,.2)',
              shadowOffsetX: 0,
              shadowOffsetY: 10,
              opacity: 1
            }
          },
          data: [
            {
              value: [5000, 7000, 8000, 9000, 9000, 5000],
              name: '13号',
              label: {
                show: true
              }
            },
            {
              value: [4000, 9000, 3000, 9000, 8000, 8000],
              name: '14号',
              label: {
                show: true
              }
            },
            {
              value: [5500, 6000, 9000, 6000, 7000, 7000],
              name: '今天',
              label: {
                show: true
              }
            }
          ],
          animationDuration: animationDuration
        }]
      })
    }
  }
}
</script>
