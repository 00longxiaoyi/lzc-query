<template>
  <button class="copy-btn" @click="fallbackCopyTextToClipboard">
    <span v-if="!copied">📋 复制</span>
    <span v-else>✅ 已复制</span>
  </button>
</template>

<script setup>
import { ref } from "vue"
import { pushMessage } from "../utils/toastStore"

const props = defineProps({
  getCopyText: {
    type: Function,
    required: true,
  },
})

const copied = ref(false)

// const copyText = async () => {
//   try {
//     const text = props.getCopyText()
//     if (!text) return
//     console.log(text)
//     await navigator.clipboard.writeText(text)
//     copied.value = true
// 
//     setTimeout(() => {
//       copied.value = false
//     }, 2000)
//   } catch (err) {
//     fallbackCopyTextToClipboard(text)
//   }
// }

const fallbackCopyTextToClipboard = () => {
  const text = props.getCopyText()
  const textArea = document.createElement("textarea")
  textArea.value = text
  document.body.appendChild(textArea)
  textArea.select()
  try {
    document.execCommand('copy')
    copied.value = true
  } catch (err) {
    console.error('Fallback 复制失败', err)
    pushMessage(err, "error")
  }
  document.body.removeChild(textArea)
}

</script>

<style scoped>
.copy-btn {
  padding: 6px 12px;
  font-size: 14px;
  color: #fff;
  background-color: var(--btn-primary-bg);
  border: none;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: background-color 0.2s ease;
  z-index: 100;
  top: 60px;
}

.copy-btn:hover {
  background-color: var(--btn-primary-hover);
}
</style>
