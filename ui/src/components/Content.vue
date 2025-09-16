<script setup>
  import LoadingOverlay from './LoadingOverlay.vue'
  import CopyButton from './CopyButton.vue'
  import { ref, defineProps } from "vue"; 

  const props = defineProps({
    data: String,
    isLoadingData: Boolean
  });

</script>
<template>
  <div class="content_con">
    
    <div class="title">
      <h1>获取到的内容</h1>
      <p>(⚠️获取到的数据仅作为辅助手段，请认真核查每条数据)</p>
    </div>

    <div class="content_wrapper">
      <CopyButton v-show="!isLoadingData && data" :getCopyText="() => props.data" class="copy_but" />
      <pre>{{ data }}</pre>
      <!-- 使用 LoadingOverlay -->
      <LoadingOverlay :show=isLoadingData />
    </div>
  </div>
  </template>

<style scoped>
.content_con {
  padding: 40px 0px 0px 0px;
}
.title {
  display: flex;
  align-items: center;
}
.title h1 {
  font-size: 30px;
  color: #1f2937;
}
.title p {
  color: red;
  margin-left: 10px;
}

.content_wrapper {
  max-height: 60vh; /* 表格高度，可调整 */
  overflow-y: auto;
  position: relative;
  min-height: 60vh;
}

.copy_but {
  top: 20px;
}
</style>
