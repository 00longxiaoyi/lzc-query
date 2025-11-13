<script setup>
import TBC from "./TableContent.vue"
import BUT from "./Button.vue"
import CON from "./Content.vue"
import OCC from "./OtherContentcon.vue"
import CopyButton from "./CopyButton.vue";
import { MainMenu, SubMenu, TableData, ContentData, IsLoading, TabelHeaderData } from "../utils/store"
// 测试数据
import { TabTestData, ContentTestData, MoenyTestData } from "../utils/testData"
import { ref } from "vue";
import { pushMessage } from "../utils/toastStore";
import { useRequest } from "../utils/useRequest";

const getCopyText = () => {
  if (SubMenu.value.type == 'content') {
    return ContentData.value
  }

  // 处理table
  if (SubMenu.value.type == "table") {
    return TableData.reduce((str, t) => {
      return str + Object.keys(t).reduce((s, item) => s + t[item] + "\t", "") + "\n"
    }, "")
  }
}


const tableRef = ref()

// 提交按钮
const submitFunc = () => {
  if (!tableRef.value) {
    pushMessage("提交数据错误", "error")
    return false
  }

  const newData = tableRef.value.sendNewTableData()
  const { data, error, loading, run } = useRequest("/set_soft_article_data", { method: "POST" })
  run({ data: newData })

  if (error.value != null) {
    pushMessage(error, "error")
  } else {
    pushMessage("提交数据成功", "success")
  }
  return false
}

</script>

<template>

  <div class="content-container-main" v-if="MainMenu && SubMenu">
    <div class="content-header-main">
      <div class="content-header">
        <div class="content-header-nav"> {{ MainMenu.label }} / {{ SubMenu.label }} </div>
      </div>

      <div class="content-sub">
        <div class="content-sub-title">
          <h2>⚠️⚠️⚠️获取到的数据仅作为辅助手段，请认真核查每条数据</h2>
          <div class="content-sub-but">
            <CopyButton v-if="!['moeny', 'other', 'Summary'].includes(SubMenu.value)" :getCopyText />
            <BUT v-if="SubMenu.value == 'moeny'" text="提交修改" :submitEvnt="submitFunc"></BUT>
          </div>
        </div>
      </div>
    </div>

    <div class="content-main">
      <TBC v-if="SubMenu.type == 'table'" ref="tableRef" :data="TableData" :isLoadingData="IsLoading"
        :tableHeader="TabelHeaderData">
      </TBC>
      <CON v-if="SubMenu.type == 'content'" :data="ContentData" :isLoadingData="IsLoading"></CON>
      <OCC v-if="SubMenu.type == 'other'"></OCC>
    </div>
  </div>

</template>

<style scoped>
.content-container-main {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  font: 16px;
}

.content-header-main {
  flex-shrink: 0;
  width: 100%;
}

.content-header {
  font-weight: 600;
}

.content-header-nav {
  padding: 5px;
  background-color: #EEEEEE;
}

.content-sub-title {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.content-sub-but {
  padding: 10px 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

.content-sub-but> :not(:first-child) {
  margin-left: 10px;
}

.content-main {
  flex: 1;
  overflow: auto;
  margin: 0 0 10vh 0;
}
</style>
