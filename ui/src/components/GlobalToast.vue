<template>
  <div class="toast-container">
    <transition-group name="fade" tag="div">
      <div
        v-for="toast in toasts"
        :key="toast.id"
        class="toast"
        :class="toast.type"
      >
        {{ toast.message }}
      </div>
    </transition-group>
  </div>
</template>

<script setup>
import { toRefs } from "vue"
import { toastStore } from "../utils/toastStore.js"

const { toasts } = toRefs(toastStore)
</script>

<style scoped>
.toast-container {
  position: fixed;
  top: 16px;
  right: 16px;
  z-index: 9999;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.toast {
  color: white;
  padding: 10px 16px;
  border-radius: 6px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  font-size: 14px;
  margin: 0 0 10px 0;
}

/* 类型样式 */
.toast.success {
  background-color: #34d399; /* 绿色 */
}
.toast.error {
  background-color: #f87171; /* 红色 */
}
.toast.info {
  background-color: #60a5fa; /* 蓝色 */
}
.toast.warning {
  background-color: #fbbf24; /* 黄色 */
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s, transform 0.3s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}
</style>
