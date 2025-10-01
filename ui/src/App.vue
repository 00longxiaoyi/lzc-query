<script setup>
import { ref, watchEffect } from 'vue'
import { useRequest } from "./utils/useRequest.js"

import Header from "./components/Header.vue"
import TBC from "./components/TableContent.vue"
import CON from "./components/Content.vue"
import GlobalToast from "./components/GlobalToast.vue"
import Settings from "./components/Settings.vue"
import { pushMessage } from "./utils/toastStore.js"
import downloadZip from "./utils/downloadZip.js"
import { contentWebSocket } from "./utils/webSocketContent.js"

const selectedCom = ref(0)
const contentData = ref()
const tableData = ref([])
var isLoadingData = ref()
var isDownloadingPic = ref(true)

const selectComponent = async (data) => {
  const { type, index } = data
  const oldIndex = selectedCom.value
  selectedCom.value = index
  if (type == "software") {
    if (index == 1) {
      await setData(tableData, [], useRequest("/get_soft_ware_pending_data"))
    }
    if (index == 2) {
      // 获取所有应用数据
      await setData(contentData, "", useRequest("/get_soft_ware_data"))
      contentWebSocket(isDownloadingPic)
    }
    if (index == 3) {
      // dom保持不变
      selectedCom.value = oldIndex 
      // 获取图片数据
      await downloadZip()
    }
  } else {
    if (index == 1) {
      await setData(tableData, [], useRequest("/get_article_pending_data"))
    }
    if (index == 2) {
      await setData(contentData, "", useRequest("/get_article_data"))
    }
  }
}
const setData = async (setDataVar, setDataVarDefault, getDataFun) => {
  setDataVar.value = setDataVarDefault
  const getData = getDataFun
  const { error, loading, data, run } = getData
  isLoadingData = loading
  await run()
  if (error.value != null) {
    pushMessage(error.value, "error")
    setDataVar.value = setDataVarDefault
  } else {
    pushMessage("数据获取成功", "success")
    setDataVar.value = data.value
  }
}

</script>

<template>
  <Settings />
  <GlobalToast />
  <Header @update="selectComponent" :isLoadingData :isDownloadingPic></Header>
  <TBC v-if="selectedCom == 1" :data="tableData" :isLoadingData></TBC>
  <CON v-if="selectedCom == 2" :data="contentData" :isLoadingData></CON>
</template>

<style scoped></style>
