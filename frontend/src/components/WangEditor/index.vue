<template>
  <div>wangEditor</div>
</template>

<script>

  export default {
    name: 'WangEditor',
    components: {
    },
    props: {
      value: {
        type: String,
        default: ''
      }
    },
    data() {
      return {
        editor: null
      }
    },
    computed: {},
    methods: {
    }
  }
</script>
