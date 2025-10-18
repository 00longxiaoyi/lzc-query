<template>
  <div>
    <!-- 小把手 -->
    <div class="settings-handle" @click="togglePanel">
      设置
    </div>

    <!-- 遮罩 -->
    <div v-if="visible" class="settings-overlay" @click="closePanel"></div>

    <!-- 抽屉 -->
    <div class="settings-drawer" :class="{ visible }">
      <div class="settings-header">
        <div>设置</div>
        <button class="settings-close" @click="closePanel">×</button>
      </div>
      <div class="settings-body">
        <div class="row">
          <div class="label">当前 Token</div>
          <div class="token-box">{{ currentToken || "(空)" }}</div>
        </div>
        <div class="row">
          <div class="label">设置 Token</div>
          <div class="input-wrap">
            <input class="input" v-model="newToken" placeholder="请输入新的 Token" />
            <button :disable="enableSub" class="icon-btn" @click="confirmToken">
              <!-- ✅ 图标 -->
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20" fill="none"
                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 6L9 17l-5-5" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useRequest } from "../utils/useRequest.js"
import { pushMessage } from "../utils/toastStore.js"

// token 存 localStorage，可以改成从 props 或 API 来
const visible = ref(false)
const currentToken = ref("")
const newToken = ref("")
var enableSub = ref(true)

const openPanel = () => (visible.value = true)
const closePanel = () => (visible.value = false)
const togglePanel = () => (visible.value = !visible.value)


const loadToken = async () => {
  const { data, error, loading, run } = useRequest("/get_token")

  if (error.value) {
    pushMessage("token 获取失败", "error")
  }

  await run()

  if (data.value) {
    pushMessage("token获取成功", "success")
    currentToken.value = data.value
  }
}

const confirmToken = async () => {
  if (newToken.value == "") {
    pushMessage("token 不能为空", "error")
    return
  }

  const { data, error, loading, run } = useRequest("/set_token", { method: "POST" })

  enableSub = loading

  await run({ "token": newToken.value })

  if (error.value) {
    pushMessage("token 设置失败", "error")
  }

  if (data.value) {
    pushMessage("token 设置成功", "success")
    currentToken.value = data.value
  }
}

onMounted(loadToken)
</script>

<style scoped>
.settings-overlay {
  position: fixed;
  inset: 0;
  background: var(--overlay-bg);
  z-index: 9998;
}

.settings-drawer {
  position: fixed;
  top: 0;
  right: 0;
  height: 100vh;
  width: 30vw;
  min-width: 300px;
  background: #fff;
  box-shadow: -2px 0 12px rgba(0, 0, 0, 0.15);
  z-index: 9999;
  display: flex;
  flex-direction: column;
  transform: translateX(100%);
  transition: transform 0.3s ease;
}

.settings-drawer.visible {
  transform: translateX(0);
}

.settings-header {
  height: 56px;
  padding: 0 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #eee;
  font-size: 16px;
  font-weight: 600;
}

.settings-close {
  border: none;
  background: transparent;
  cursor: pointer;
  font-size: 20px;
  line-height: 1;
}

.settings-body {
  padding: 16px;
  overflow: auto;
  flex: 1;
}

.row {
  margin-bottom: 16px;
}

.label {
  font-size: 12px;
  color: #666;
  margin-bottom: 6px;
}

.token-box {
  background: #f7f7f7;
  border: 1px solid #e5e5e5;
  border-radius: 6px;
  padding: 5px;
  word-break: break-all;
}

.input-wrap {
  display: flex;
  align-items: center;
  gap: 8px;
}

.input {
  flex: 1;
  height: 36px;
  border: 1px solid #ddd;
  border-radius: 6px;
  padding: 0 10px;
  outline: none;
}

.input:focus {
  border-color: #7c3aed;
  box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.15);
}

.icon-btn {
  width: 36px;
  height: 36px;
  border-radius: 6px;
  border: 1px solid #7c3aed;
  background: var(--btn-primary-bg);
  color: #fff;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.08s ease, opacity 0.2s ease;
}

.icon-btn:hover {
  background-color: var(--btn-primary-hover);
}

.icon-btn:active {
  transform: scale(0.98);
}

.settings-handle {
  position: fixed;
  right: 0;
  transform: translateY(-50%);
  z-index: 9997;
  background: var(--btn-primary-bg);
  color: #fff;
  padding: 15px 12px;
  cursor: pointer;
  box-shadow: -2px 2px 8px rgba(0, 0, 0, 0.2);
  writing-mode: vertical-rl;
  text-orientation: mixed;
  user-select: none;
}

.settings-handle:hover {
  background: var(--btn-primary-hover);
}
</style>
