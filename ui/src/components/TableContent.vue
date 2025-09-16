<template>
  <div class="content_con">
    <div class="title">
      <h1>获取到的内容</h1>
      <p>(⚠️获取到的数据仅作为辅助手段，请认真核查每条数据)</p>
    </div>
    <div class="table-wrapper">
      <!-- 复制按钮 -->
      <CopyButton v-show="!isLoadingData && data.length > 0" :getCopyText="setCopyContent" /> 
      
      <table class="data-table" v-show="data.length > 0">
        <thead>
          <tr>
            <th>标题</th>
            <th>作者</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(d, index) in data" :key="index">
            <td>{{ d.title }}</td>
            <td>{{ d.nickname }}</td>
          </tr>
        </tbody>
      </table>
      <!-- 使用 LoadingOverlay -->
      <LoadingOverlay :show=isLoadingData />
    </div>
    <div class="content_other">
        <p>共计：{{ data.length }} 条数据</p>
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps } from "vue";
import LoadingOverlay from './LoadingOverlay.vue'
import CopyButton from './CopyButton.vue'

const props = defineProps({
  data: Array,
  isLoadingData: Boolean
})


const setCopyContent = () => {
  if (props.data && props.data.length > 0) {
    return props.data.map(d => {
      return `${d.title}\t${d.nickname}`
    }).join("\n")
    }
  return ""
}

</script>

<style scoped>
.content_con {
  padding: 40px 0px 0px 0px;
}
.title {
  display: flex;
  align-items: center;
}
.title h1 {
  font-size: 30px;
  color: #1f2937;
}
.title p {
  color: red;
  margin-left: 10px;
}

/* 表格外层容器，固定高度并滚动 */
.table-wrapper {
  max-height: 60vh; /* 表格高度，可调整 */
  overflow-y: auto;
  min-height: 60vh;
  position: relative; 
}

/* 表格 */
.data-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0 8px; /* 行间距 */
}

.data-table th, .data-table td {
  padding: 12px 16px;
  text-align: left;
}

.data-table th {
  background-color: #f3f4f6;
  color: #1f2937;
  font-weight: 600;
  position: sticky;
  top: 0;
  z-index: 2;
}

.data-table tbody tr {
  background-color: #ffffff;
  transition: all 0.2s ease;
  border-radius: 8px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.05);
}

.data-table tbody tr:hover {
  background-color: #f9fafb;
  transform: translateY(-1px);
}

.data-table td {
  color: #374151;
  border-bottom: 1px solid #e5e7eb;
}

/* 移动端响应式 */
@media (max-width: 600px) {
  .data-table th, .data-table td {
    padding: 10px 8px;
  }
}

.content_other {
  text-align: right;
}

</style>
