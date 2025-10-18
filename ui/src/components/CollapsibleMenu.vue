<script setup>
import { ref, defineProps } from 'vue';

// 是否折叠
const isCollapsiable = ref(true)

const changeMenuStatus = () => {
  isCollapsiable.value = !isCollapsiable.value
}

const props = defineProps({
  MenuItemData: {},
  changeMenu: Function
})

const activateMenu = (subMenu) => {
  props.changeMenu(props.MenuItemData.main, subMenu)
}

</script>

<template>
  <div class="menu-main">

    <div class="menu-main-con" @click="changeMenuStatus">
      <div class="menu-main-label">
        <span class="menu-main-lable-text">
          {{ props.MenuItemData.main.label }}
        </span>
        <span :class="{
          'menu-main-lable-icon': true,
          'menu-main-lable-icon-re': !isCollapsiable
        }">
          <svg t="1760603323286" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
            p-id="9204" width="20" height="20">
            <path
              d="M648.533333 334.506667a204.8 204.8 0 0 1 0 354.986666l-273.066666 157.422934a204.8 204.8 0 0 1-307.2-177.493334V354.577067A204.8 204.8 0 0 1 375.466667 177.493333z"
              fill="#ffffff" p-id="9205"></path>
          </svg>
        </span>
      </div>
    </div>

    <div class="menu-main-sub" v-show="!isCollapsiable">
      <div class="menu-main-sub-item" v-for="item in props.MenuItemData.sub" @click="activateMenu(item)">
        <div class="menu-main-sub-item-label">
          {{ item.label }}
        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>
.menu-main {
  display: inline-block;
  font-weight: 400;
  user-select: none;
  width: 120px;
}

.menu-main-con {
  display: flex;
  background-color: var(--btn-primary-bg);
  font-size: 14px;
  font-weight: 600;
  user-select: none;
}

.menu-main-con:hover {
  background-color: var(--btn-primary-hover);
}

.menu-main-label {
  /* 1. 启用 Flex 布局 */
  display: flex;

  /* 2. 垂直居中对齐：这是确保文字和图标高度对齐的关键 */
  align-items: center;

  /* 3. 设置一些基础样式 (例如，如果这是个菜单项) */
  color: #ffffff;
  /* 假设文字颜色 */
  padding: 10px 15px;
  /* 菜单项的内边距 */
  cursor: pointer;
  font-size: 16px;
  color: white;
  font-weight: 600;
}

.menu-main-lable-text {
  margin-right: 4px;
}

.menu-main-lable-icon {
  display: flex;
  align-items: center;
  line-height: 1;
  bottom: 0;
  left: 0;
}

/* 图标旋转 */
.menu-main-lable-icon-re {
  transform: rotateZ(90deg);
  transition: all 0.3s ease-in-out;
}

.menu-main-sub {
  display: block;
  text-align: center;
}

.menu-main-sub-item {
  font-size: 14px;
  padding: 5px 0;
  border: 2px solid;
  border-color: var(--btn-primary-bg);
  background-color: transparent;
  color: var(--btn-primary-bg);
  cursor: pointer;

}

.menu-main-sub-item:not(:first-child) {
  border-top: none;
}

.menu-main-sub-item:hover {
  background-color: var(--btn-primary-bg);
  color: #ffffff;
}
</style>
