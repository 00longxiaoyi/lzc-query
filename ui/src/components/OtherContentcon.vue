<script setup>
import { onMounted, ref } from "vue";
import { useRequest } from "../utils/useRequest";
import DLC from "./DownloaderCom.vue"
import { pushMessage } from "../utils/toastStore";
import { contentWebSocket } from "../utils/webSocketContent";
import downloadZip from "../utils/downloadZip";

const dowloadSumNumer = ref(0)
const dowloadRef = ref()
const dowloadPicLoading = ref(false)

const { data: dow_num, error: dow_err, loading: dow_loading, run: dow_run } = useRequest("/get_all_pics_num")

onMounted(async () => {
  await dow_run()
  if (dow_err.value != null) {
    pushMessage(error.value, "error")
  }
  if (dow_num.value) {
    dowloadSumNumer.value = dow_num.value.num
  }
})

const dowloadPicClickFunc = async () => {
  if (!dowloadRef.value) return
  // dowloadRef.value.increaseCallback()
  dowloadPicLoading.value = true
  contentWebSocket(() => {
    dowloadRef.value.increaseCallback()
  }, async () => {
    dowloadPicLoading.value = false
    await downloadZip()
  })
}



// 
</script>

<template>
  <DLC ref="dowloadRef" :sumNum="dowloadSumNumer" :clickCallback="dowloadPicClickFunc" :isLoading="dowloadPicLoading">
  </DLC>
</template>

<style scoped></style>
