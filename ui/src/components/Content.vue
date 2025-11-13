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
    <div class="content_wrapper">
      <pre>{{ data }}</pre>
      <!-- 使用 LoadingOverlay -->
      <LoadingOverlay :show=isLoadingData />
    </div>
  </div>
</template>

<style scoped>
.content_con {
  width: 100%;
  height: 100%;
}

.content_wrapper {
  /* 表格高度，可调整 */
  overflow: auto;
}

pre {
  width: 100%;
  height: 100%;
}
</style>
