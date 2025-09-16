import { reactive } from "vue"

export const toastStore = reactive({
  toasts: []
})

let seed = 0

/**
 * @param {string} message 提示内容
 * @param {string} type 类型 success / error / info / warning
 * @param {number} duration 显示时长
 */
export function pushMessage(message, type = "info", duration = 3000) {
  const id = seed++
  toastStore.toasts.push({ id, message, type })

  setTimeout(() => {
    const idx = toastStore.toasts.findIndex(t => t.id === id)
    if (idx !== -1) {
      toastStore.toasts.splice(idx, 1)
    }
  }, duration)
}

