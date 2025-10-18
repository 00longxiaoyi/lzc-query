<script setup>
import { ref, watchEffect } from 'vue'
import { useRequest } from "./utils/useRequest.js"

import Header from "./components/Header.vue"
import CCN from "./components/ContentContainer.vue"


import TBC from "./components/TableContent.vue"
import CON from "./components/Content.vue"
import MS from "./components/MoenySum.vue"
import GlobalToast from "./components/GlobalToast.vue"
import Settings from "./components/Settings.vue"
import { pushMessage } from "./utils/toastStore.js"
import downloadZip from "./utils/downloadZip.js"
import { contentWebSocket } from "./utils/webSocketContent.js"

import './themes.css'

const selectedCom = ref()
const contentData = ref()
const tableData = ref([])
var isLoadingData = ref()
var isDownloadingPic = ref(true)
const selectType = ref("")

const selectComponent = async (data) => {
  const { type, index } = data
  const oldIndex = selectedCom.value
  selectedCom.value = index
  selectType.value = type
  console.log(selectType.value)
  if (type == "software") {
    if (index == 1) {
      await setData(tableData, [], useRequest("/get_soft_ware_pending_data"))
    }
    if (index == 2) {
      // 获取所有应用数据
      await setData(contentData, "", useRequest("/get_soft_ware_data"))
      // contentWebSocket(isDownloadingPic)
    }
    if (index == 3) {
      // dom保持不变
      selectedCom.value = oldIndex
      // 获取图片数据
      await downloadZip()
    }
  } else if (type == "article") {
    if (index == 1) {
      await setData(tableData, [], useRequest("/get_article_pending_data"))
    }
    if (index == 2) {
      await setData(contentData, "", useRequest("/get_article_data"))
    } else {

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
  <div class="app bright-theme">
    <div class="title">
      <h1>每日审核数据获取</h1>
    </div>

    <div class="main">

      <!-- <Settings /> -->
      <!-- <GlobalToast /> -->

      <Header class="main-header" @update="selectComponent" :isLoadingData :isDownloadingPic></Header>
      <CCN class="main-content"></CCN>
    </div>

    <div v-if="false">
      <div v-if="selectType == 'other'">
        <MS v-if="selectComponent == 1"></MS>
      </div>
      <div v-else>
        <TBC v-if="selectedCom == 1" :data="tableData" :isLoadingData></TBC>
        <CON v-if="selectedCom == 2" :data="contentData" :isLoadingData></CON>
      </div>
    </div>
  </div>
</template>

<style scoped>
.app {
  width: 100vw;
  height: 100vh;
  padding: 0 10vw;
}

.title h1 {
  font-size: 30px;
  color: #333;
}

.main {
  display: flex;
  height: 100%;
  width: 100%;
}

.main-header {
  width: 200px;
}

.main-content {
  flex: 1;
  min-width: 0;
  min-height: 0;
}
</style>
