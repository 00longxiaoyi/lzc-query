<script setup>
import TBC from "./TableContent.vue"
import CON from "./Content.vue"
import CopyButton from "./CopyButton.vue";
import { MainMenu, SubMenu, TableData, ContentData, IsLoading, TabelHeaderData } from "../utils/store"
// 测试数据
import { TabTestData, ContentTestData, MoenyTestData } from "../utils/testData"

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
          <div class="content-sub-copy-but">
            <CopyButton :getCopyText />
          </div>
        </div>
      </div>
    </div>

    <div class="content-main">
      <TBC v-if="SubMenu.type == 'table'" :data="MoenyTestData" :isLoadingData="IsLoading"
        :tableHeader="TabelHeaderData">
      </TBC>
      <CON v-if="SubMenu.type == 'content'" :data="ContentData" :isLoadingData="IsLoading"></CON>
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

.content-sub-copy-but {
  padding: 10px 0;
}

.content-main {
  flex: 1;
  overflow: auto;
  margin: 0 0 10vh 0;
}
</style>
