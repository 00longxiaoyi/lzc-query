<script setup>
import { ref, defineEmits, defineProps, watchEffect } from "vue";

const emit = defineEmits(["update"])
const activeBut = ref(0); // 0 = none, 1 = 文章, 2 = 应用

const subClickHandler = (type, index) => {
  emit("update", {type, index})
}

const prpos = defineProps({
  isLoadingData: Boolean
})


watchEffect(() => {
  
console.log(prpos)
});

</script>

<template>
  <div class="category-container">
    <div class="title">
      <h1>每日审核数据获取</h1>
    </div>

    <div class="main_but_container">
      <div class="main_but">
        <button 
          class="main_but_item" 
          :disabled=isLoadingData
          :class="{ active: activeBut === 1 }" 
          @click="activeBut = activeBut === 1 ? 0 : 1">
          文章数据
        </button>
        <button 
          class="main_but_item"
          :disabled=isLoadingData
          :class="{ active: activeBut === 2 }" 
          @click="activeBut = activeBut === 2 ? 0 : 2">
          应用数据
        </button>
      </div>

      <!-- 子按钮 -->
      <transition name="fade-slide">
        <div class="subcategory" v-if="activeBut === 1">
          <button :disabled=isLoadingData class="sub_but_item" @click="subClickHandler('article', 1)">获取每日待审核的文章</button>
          <button :disabled=isLoadingData class="sub_but_item" @click="subClickHandler('article', 2)">获取每日已审核的文章</button>
        </div>
      </transition>

      <transition name="fade-slide">
        <div class="subcategory" v-if="activeBut === 2">
          <button :disabled=isLoadingData class="sub_but_item" @click="subClickHandler('software', 1)">获取每日待审核的应用</button>
          <button :disabled=isLoadingData class="sub_but_item" @click="subClickHandler('software', 2)">获取每日已审核的应用</button>
        </div>
      </transition>
    </div>
  </div>
</template>

<style scoped>
.category-container {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.title h1 {
  font-size: 30px;
  color: #333;
}

/* 主按钮容器 */
.main_but_container {
  position: relative; /* 子按钮相对它定位 */
}

/* 主按钮 */
.main_but {
  display: flex;
  gap: 10px;
  z-index: 1;
}

.main_but_item {
  background-color: #4a90e2;
  color: white;
  border: none;
  border-radius: 6px;
  padding: 10px 20px;
  font-size: 16px;
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

/* 子按钮 */
.subcategory {
  position: absolute;
  top: 100%;  /* 紧贴主按钮下方 */
  left: 0;
  display: flex;
  gap: 8px;
  background: #fff;
  padding: 8px 0;
  border-radius: 6px;
  z-index: 0;
}

.sub_but_item {
  background-color: #ffffff;
  color: #4a90e2;
  border: 2px solid #4a90e2;
  border-radius: 6px;
  padding: 8px 12px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.25s ease;
}

.sub_but_item:hover {
  background-color: #e8f0fe;
}

.sub_but_item:active {
  background-color: #d0e0fc;
  border-color: #3570b3;
  color: #3570b3;
}

/* 动画 */
.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
.fade-slide-enter-to,
.fade-slide-leave-from {
  opacity: 1;
  transform: translateY(0);
}
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.3s ease;
}
</style>
