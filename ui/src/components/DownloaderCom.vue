<script setup>
import { ref, watch } from 'vue';

const EMPTYREF = ref()
const DOWNLOADCONREF = ref()
const increaseNum = ref(1)
const curScaleNume = ref(1)
const isLoading = ref(false)

const props = defineProps({
  sumNum: Number,
  clickCallback: Function,
  isLoading: Boolean
})

const increaseCallback = () => {
  if (!EMPTYREF.value) return
  console.log(111)
  EMPTYREF.value.style.transform = `translate(-50%, 0%) scaleX(${curScaleNume.value})`
  curScaleNume.value += increaseNum.value
}

watch(() => props.sumNum, (newvalue) => {
  if (DOWNLOADCONREF.value && EMPTYREF.value) {
    const fillWidth = DOWNLOADCONREF.value.getBoundingClientRect().width
    const curWidth = EMPTYREF.value.getBoundingClientRect().width
    console.log(fillWidth, curWidth, props.sumNum)
    const secIncreaseCount = fillWidth / curWidth / (newvalue ?? 1)
    increaseNum.value = secIncreaseCount
  }
  console.log(increaseNum.value)
})

watch(() => props.isLoading, (newvalue) => {
  isLoading.value = newvalue
})

const clickFunc = () => {
  if (!EMPTYREF.value) return
  EMPTYREF.value.style.opacity = 1
  props.clickCallback()
}

defineExpose({
  "increaseCallback": increaseCallback
})

</script>

<template>
  <div class="download-con" ref="DOWNLOADCONREF">
    <button @click="clickFunc" :disabled="isLoading">下载图片</button>
    <span class="empty" ref="EMPTYREF">下载图片</span>
  </div>
</template>

<style scoped>
.download-con {
  width: 100%;
  height: 250px;
  background-color: var(--btn-secondary-bg);
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;
}

.download-con button {
  font-size: 16px;
  font-weight: bold;
  padding: 13px 40px;
  border-radius: 30px;
  background-color: var(--btn-secondary-hover);
  color: black;
  border: none;
  cursor: pointer;
  position: relative;
  z-index: 2;
}

.empty {
  font-size: 16px;
  font-weight: bold;
  background-color: var(--btn-secondary-hover);
  color: var(--btn-secondary-hover);
  height: 100%;
  padding: 0px 40px;
  position: absolute;
  left: 50%;
  transform-origin: center center;
  /* 或者简写为 center */
  transform: translate(-50%, 0%) scale(1);
  border: none;
  transition: transform 0.2s ease;
  opacity: 0;
}

.download-con button:disabled,
.download-con button:disabled:hover,
.download-con button:disabled:active {
  background-color: var(--btn-secondary-hover);
  cursor: not-allowed;
}

.download-con button:hover {
  background-color: var(--btn-secondary-active);
}
</style>
