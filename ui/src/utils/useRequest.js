import { ref } from "vue"

// 获取后端地址，生产环境从 VITE_API_BASE，开发环境直接用 /api 代理
//const BASE_URL = import.meta.env.PROD
//  ? import.meta.env.VITE_API_BASE
//  : "/api"

const BASE_URL = "/api"

export function useRequest(url, options = {}) {
  const loading = ref(false)
  const error = ref(null)
  const data = ref(null)

  const run = async (params = {}) => {
    loading.value = true
    error.value = null

    try {
      const res = await fetch(`${BASE_URL}${url}`, {
        method: options.method || "GET",
        headers: {
          "Content-Type": "application/json",
          ...(options.headers || {})
        },
        body: options.method === "POST" ? JSON.stringify(params) : null,
      })

      if (!res.ok) {
        error.value = "未知错误，请联系开发者"
        throw new Error(`HTTP 错误: ${res.status}`)
      }

      const result = await res.json()

      // 处理业务 code
      if (result.code === 401) {
        error.value = "鉴权错误，请检查token的值是否正确!!!"
      } else if (result.code === 500) {
        error.value = "服务器错误，请联系开发者"
      } else if (result.code === 200) {
        data.value = result.data
      } else {
        error.value = result.msg || "未知业务错误"
      }

    } catch (err) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }

  return {
    data,
    error,
    loading,
    run,
  }
}
