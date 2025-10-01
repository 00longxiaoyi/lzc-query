<script setup>
import { ref, defineEmits, defineProps, watchEffect } from "vue";

const emit = defineEmits(["update"])
const activeBut = ref(0); // 0 = none, 1 = 文章, 2 = 应用

const subClickHandler = (type, index) => {
  emit("update", { type, index })
}

const prpos = defineProps({
  isLoadingData: Boolean,
  isDownloadingPic: Boolean
})

watchEffect(() => {
  console.log(prpos)
  console.log(prpos.isDownloadingPic)
});

</script>

<template>
  <div class="category-container">
    <div class="title">
      <h1>每日审核数据获取</h1>
    </div>

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
        </div>
      </div>


      <div class="main_but_container_right">
        <!-- 子按钮 -->
        <div class="subcategory" v-if="activeBut === 1">
          <button :disabled=isLoadingData class="sub_but_item" @click="subClickHandler('article', 1)">获取待审核的文章</button>
          <button :disabled=isLoadingData class="sub_but_item" @click="subClickHandler('article', 2)">获取已审核的文章</button>
        </div>

        <div class="subcategory" v-if="activeBut === 2">
          <button :disabled=isLoadingData class="sub_but_item" @click="subClickHandler('software', 1)">获取待审核的应用</button>
          <button :disabled=isLoadingData class="sub_but_item" @click="subClickHandler('software', 2)">获取已审核的应用</button>
          <button :disabled=isDownloadingPic class="sub_but_item"
            @click="subClickHandler('software', 3)">获取图片数据</button>
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

.title h1 {
  font-size: 30px;
  color: #333;
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
