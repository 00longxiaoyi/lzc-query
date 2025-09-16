<template>
  <div v-if="show" class="loading-overlay">
    <div class="loading">
      <slot>Loading<span></span><span></span><span></span></slot>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from "vue";

const props = defineProps({
  show: { type: Boolean, default: false } // 控制显示
})
</script>

<style scoped>
.loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255,255,255,0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
  user-select: none; /* 标准写法 */
  -webkit-user-select: none; /* Chrome/Safari */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* IE10+ */
}

.loading {
  font-size: 20px;
  font-weight: 500;
  color: #4a90e2;
  display: flex;
  align-items: center;
  gap: 4px;
}

.loading span {
  display: inline-block;
  width: 6px;
  height: 6px;
  background-color: #4a90e2;
  border-radius: 50%;
  animation: bounce 1s infinite;
}

.loading span:nth-child(2) { animation-delay: 0.2s; }
.loading span:nth-child(3) { animation-delay: 0.4s; }

@keyframes bounce {
  0%, 80%, 100% { transform: scale(0); opacity: 0.3; }
  40% { transform: scale(1); opacity: 1; }
}
</style>

