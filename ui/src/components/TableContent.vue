<template>
  <div class="table-main">
    <div class="table-wrapper">
      <table class="data-table" v-show="data.length > 0">
        <thead>
          <tr>
            <th v-for="item in tableHeader" :key="item">{{ item }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(d, index) in data" :key="index">
            <td v-for="k_name in Object.keys(d)">
              <div v-if="k_name != 'price'">{{ d[k_name] }}</div>
              <input v-else :value="d[k_name]" type="number" />
            </td>
          </tr>
        </tbody>
      </table>
      <!-- 使用 LoadingOverlay -->
      <LoadingOverlay :show=isLoadingData />
    </div>
    <div class="table-botton" v-show="data?.length">
      <span>共计：{{ data.length }} 条数据</span>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from "vue";
import LoadingOverlay from './LoadingOverlay.vue'

const props = defineProps({
  tableHeader: Array,
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
.table-main {
  height: 100%;
  display: flex;
  flex-direction: column;
}


/* 表格外层容器，固定高度并滚动 */
.table-wrapper {
  flex: 1;
  /* 表格高度，可调整 */
  overflow-y: auto;
  position: relative;
}

/* 表格 */
.data-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0 8px;
  /* 行间距 */
}

.data-table th,
.data-table td {
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
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.data-table tbody tr:hover {
  background-color: #f9fafb;
}

.data-table tbody tr td:first-child div {
  max-width: 300px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.data-table tbody tr td input {
  max-width: 100px;
  padding: 5px 0 5px 10px;
  border: none;
  background-color: transparent;
}

.data-table tbody tr td input:focus {
  border: var(--btn-primary-hover);
}

.data-table td {
  color: #374151;
  border-bottom: 1px solid #e5e7eb;
}

/* 移动端响应式 */
@media (max-width: 600px) {

  .data-table th,
  .data-table td {
    padding: 10px 8px;
  }
}

.table-botton {
  padding-top: 10px;
  height: 40px;
  text-align: right;
}

.table-botton span {
  margin: 0 0 0 10px;
}

/* Chrome、Safari、Edge（WebKit 内核）*/
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Firefox */
input[type="number"] {
  -moz-appearance: textfield;
}
</style>
