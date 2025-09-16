import GlobalToast from "../components/GlobalToast.vue"
import { pushMessage } from "../utils/toastStore.js"

export default {
  install(app) {
    app.component("GlobalToast", GlobalToast)
    app.config.globalProperties.$toast = pushMessage
  }
}

export { pushMessage }

