<template>
  <div class="CardView" :style="{'background-color':color}">
    <div class="box">
      <div class="number">
        <count-to :start-val="0" :end-val="number" :duration="2600" />
      </div>
      <div class="desc">{{ desc }}</div>
    </div>
  </div>
</template>

<script>
  import CountTo from 'vue-count-to'
  export default {
    name: 'CardView',
    components: {
      CountTo
    },
    props: {
      number: {
        type: Number,
        default: 100
      },
      desc: {
        type: String,
        default: '描述信息'
      },
      color: {
        type: String,
        default: '#11b95c'
      }
    },
    data() {
      return {}
    },
    methods: {
      numFun(startNum, maxNum) {
        const _that = this
        let numText = startNum
        let golb // 为了清除requestAnimationFrame
        function numSlideFun() { // 数字动画
          numText += 5 // 速度的计算可以为小数 。数字越大，滚动越快
          if (numText >= maxNum) {
            numText = maxNum
            cancelAnimationFrame(golb)
          } else {
            golb = requestAnimationFrame(numSlideFun)
          }
          _that.amount = numText
        }

        numSlideFun() // 调用数字动画
      }
    }
  }
</script>

<style lang="scss" scoped>
  .CardView {
    height: 100px;
    width: 100%;
    border-radius: 10px;
    color: #fff;
    padding: 20px;
    margin-bottom: 20px;
    /*background-color: aquamarine;*/
    .box {
      padding: 5px;
      .number {
        font-size: 30px;
        font-weight: 500;
      }
      .desc {
        margin-top: 5px;
        font-size: 15px;
        font-weight: 500;
      }
    }
  }

</style>
