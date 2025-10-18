<script setup>
import CLM from "./CollapsibleMenu.vue"
import { ref, defineEmits, defineProps, watchEffect } from "vue";

import { setMainMenu, setSubMenu } from "../utils/store";

const emit = defineEmits(["update"])
const prpos = defineProps({
  isLoadingData: Boolean,
  isDownloadingPic: Boolean
})


const MenuItemsData = [
  {
    "main": {
      "label": "应用审核",
      "value": "soft"
    },
    "sub": [
      {
        "label": "待审核",
        "value": "noReview",
        "type": "table"
      }, {
        "label": "已审核",
        "value": "review",
        "type": "content"
      }
    ]
  },
  {
    "main": {
      "label": "文章审核",
      "value": "article"
    },
    "sub": [
      {
        "label": "代审核",
        "value": "noReview",
        "type": "table"
      }, {
        "label": "已审核",
        "value": "review",
        "type": "content"
      }
    ]
  }, {
    "main": {
      "label": "其他内容",
      "value": "other"
    }, "sub": [
      {
        "label": "金额计算",
        "value": "moeny",
        "type": "table"
      },
      {
        "label": "汇总表格",
        "value": "Summary",
        "type": "content"
      },
      {
        "label": "下载图片",
        "value": "DownloadPic",
        "type": "download",
      }
    ]
  }

]

const changeMenu = (MenuName, subName) => {
  // emit("update", { MenuName, subName })
  setMainMenu(MenuName)
  setSubMenu(subName)
}

</script>

<template>
  <div class="category-container">

    <div class="category-container-menu">
      <CLM :MenuItemData :changeMenu="changeMenu" v-for="MenuItemData in MenuItemsData"></CLM>
    </div>

    <div v-if="false">
      <div class="main_but_container">
        <div class="main_but_container_left">
          <div class="main_but">
            <button class="main_but_item" :disabled=isLoadingData :class="{ active: activeBut === 2 }"
              @click="activeBut = 2">
              应用数据
            </button>
            <button class="main_but_item" :disabled=isLoadingData :class="{ active: activeBut === 1 }"
              @click="activeBut = 1">
              文章数据
            </button>
            <button class="main_but_item" :disabled=isLoadingData :class="{ active: activeBut === 1 }"
              @click="activeBut = 3">
              汇总计算
            </button>
          </div>
        </div>

        <div class="main_but_container_right">
          <!-- 子按钮 -->
          <div class="subcategory" v-if="activeBut === 1">
            <button :disabled=isLoadingData class="sub_but_item"
              @click="subClickHandler('article', 1)">获取待审核的文章</button>
            <button :disabled=isLoadingData class="sub_but_item"
              @click="subClickHandler('article', 2)">获取已审核的文章</button>
          </div>

          <div class="subcategory" v-if="activeBut === 2">
            <button :disabled=isLoadingData class="sub_but_item"
              @click="subClickHandler('software', 1)">获取待审核的应用</button>
            <button :disabled=isLoadingData class="sub_but_item"
              @click="subClickHandler('software', 2)">获取已审核的应用</button>
            <button :disabled=isDownloadingPic class="sub_but_item"
              @click="subClickHandler('software', 3)">获取图片数据</button>
          </div>

          <div class="subcategory" v-if="activeBut === 3">
            <button :disabled=isLoadingData class="sub_but_item" @click="subClickHandler('other', 1)">金额计算器</button>
            <button :disabled=isLoadingData class="sub_but_item" @click="subClickHandler('other', 2)">汇总数据</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.category-container {
  display: flex;
  flex-direction: column;
  gap: 12px;
  font-smooth: 14px;
}

.category-container-menu {
  display: flex;
  flex-direction: column;
  width: 180px;
}

/* 这里使用的是子组件的名称 */
.category-container-menu>.menu-main:not(:first-child) {
  margin-top: 10px;
}

/* 主按钮容器 */
.main_but_container {
  position: relative;
  display: flex;
  /* 子按钮相对它定位 */
}

.main_but_container_left {
  display: flex;
  flex-direction: column;
  padding-right: 30px;
  border-right: 3px solid #4a90e2;
}

/* 主按钮 */
.main_but {
  display: flex;
  flex-direction: column;
  gap: 20px;
  z-index: 1;
}

.main_but_item {
  background-color: #4a90e2;
  color: white;
  border: none;
  border-radius: 6px;
  padding: 10px 20px;
  cursor: pointer;
  transition: background-color 0.25s ease;
}

.main_but_item:hover {
  background-color: #6aa0e8;
}

.main_but_item:active,
.main_but_item.active {
  background-color: #3570b3;
}

.main_but_container_right {
  font-size: 12px;
  padding-left: 30px;
}

/* 子按钮 */
.subcategory {
  /* 紧贴主按钮下方 */
  display: flex;
  gap: 8px;
  background: #fff;
  padding: 8px 0;
  border-radius: 6px;
  z-index: 0;
}

.sub_but_item {
  font-size: 12px;
  background-color: #ffffff;
  color: #4a90e2;
  border: 2px solid #4a90e2;
  border-radius: 6px;
  padding: 8px 12px;
  cursor: pointer;
}

.sub_but_item:hover {
  background-color: #e8f0fe;
}

.sub_but_item:active {
  background-color: #d0e0fc;
  border-color: #3570b3;
  color: #3570b3;
}

.sub_but_item:disabled {
  background-color: #ccc;
  /* 灰色背景 */
  cursor: not-allowed;
  /* 鼠标样式显示不可用 */
  opacity: 0.6;
  /* 让禁用状态看起来更明显 */
}
</style>
